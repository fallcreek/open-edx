#!/usr/bin/python
import MySQLdb
import sys,json
import pickle
import re
from datetime import timedelta
sys.path.insert(0,'/home/edxdeveloper/zyli')
from generate_answer import generate_answer

conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()

cursor.execute(
"select ch.id, ch.state, c.id as studentmodule_id, c.student_id, a.username from edxapp_csmh.coursewarehistoryextended_studentmodulehistoryextended ch, edxapp.courseware_studentmodule c,edxapp.auth_user a where ch.student_module_id = c.id and a.id = c.student_id and c.module_id like '%problem%' order by c.student_id")

res = []
locationDict = {}

with open('/home/edxdeveloper/zyli/student_data/locationToProblem.txt', 'r') as f:
  for line in f:
    s=line.strip().split(' ')
    locationDict[s[0]]=[s[1],s[2]]

for line in cursor.fetchall():
    state,student_id,username = line[1],line[3],line[4]
    state=json.loads(state)
    
    if 'student_answers' not in state:
      continue
    for pkey in state['student_answers']:
      pid, part_id = pkey.split('_')[0], int(pkey.split('_')[1])-1
      if pid not in locationDict:
        break
      [week_id, problem_id] = locationDict[pid]
      if 'last_submission_time' not in state:
        continue
      last_submission_time = state['last_submission_time']
      last_submission_time = last_submission_time.replace('T',' ')
      last_submission_time = last_submission_time.replace('Z','')
      seed = state['seed']
      attempt = state['student_answers'][pkey]
      if attempt == '' or attempt == "no attempt":
        continue
      if 'correct_map' in state and pkey in state['correct_map']:
        if state['correct_map'][pkey]['correctness'] == 'incorrect':
          pts = '0' 
        else:
          pts = str(state['correct_map'][pkey]['npoints'])
      else:
          continue
          pts = 'null'
      #invalid problem 
      if (week_id == '4' and problem_id == '7' and part_id == 4) or (week_id == '3' and problem_id == '5' and part_id == 2):
        continue;
      #print week_id + problem_id + str(part_id)
      if seed != 'null' and week_id > '2':
         answer = generate_answer(int(seed),int(week_id),int(problem_id),part_id)
      else:
	 answer = 'null'
      res.append({'answer':answer, 'attempt':attempt, 'part_id':str(part_id), 'problem_id':problem_id, 'score':pts, 'set_id':week_id,'timestamp':last_submission_time,'user_id':student_id, 'username':username})

path = '/home/edxdeveloper/zyli/student_data/pkl/'
f = open(path+'student_answer.pkl','wb')
pickle.dump(res,f)
f.close()

# generate_hint_data
student_dic = {}
cursor.execute("select u.id,u.username from edxapp.auth_user as u")

for line in cursor.fetchall():
  student_dic[line[1]] = str(line[0])

cursor.execute("select h.id,h.problem_name,h.problem_part,h.student_username,h.hint_content,h.attempt,h.time_clicked from ucsd_cse103.hint_log as h")

hint_count = 0
hint_data = {}
for line in cursor.fetchall():
  student_name = line[3]
  if student_name == '':
    continue
  week_id = re.search('Week(.+?)_', line[1]).group(1)
  problem_id = re.search('Problem(.+?)', line[1]).group(1)
  part_id = line[2]
  hint_obj = re.search('Hint: (.+?)</font>',line[4])
  if hint_obj:
    hint = hint_obj.group(1)
  else:
    hint = line[4]
  attempt_hint = line[5]
  time = str(line[6]+timedelta(hours=7))
  student_id = student_dic[student_name].replace('L','')

  problem_key = (week_id,problem_id,part_id)
  student_key = (student_id,student_name)
  value = [time,attempt_hint,hint,'Hint']
  if problem_key not in hint_data:
    hint_data[problem_key] = {}
  if student_key not in hint_data[problem_key]:
    hint_data[problem_key][student_key] = []
  hint_data[problem_key][student_key].append(value)
  hint_count += 1
	#print hint_count
  #print problem_key
  #print student_key

#print hint_count
f = open(path+'student_hint.pkl','wb')
pickle.dump(hint_data,f)
f.close()
