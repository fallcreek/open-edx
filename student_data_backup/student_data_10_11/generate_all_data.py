import MySQLdb
import sys,json
import pickle

conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()

cursor.execute(
"select ch.id, ch.state, c.id as studentmodule_id, c.student_id, a.username from edxapp_csmh.coursewarehistoryextended_studentmodulehistoryextended ch, edxapp.courseware_studentmodule c,edxapp.auth_user a where ch.student_module_id = c.id and a.id = c.student_id and c.module_id like '%problem%' order by c.student_id")

res = []
locationDict = {}

with open('locationToProblem.txt', 'r') as f:
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
      last_submission_time = state['last_submission_time'] if 'last_submission_time' in state else 'null'
      attempt = state['student_answers'][pkey]
      if 'correct_map' in state and pkey in state['correct_map']:
        if state['correct_map'][pkey]['correctness'] == 'incorrect':
          pts = '0' 
        else:
          pts = str(state['correct_map'][pkey]['npoints'])
      else:
          pts = 'null'
      
      res.append({'attempt':attempt, 'part_id':str(part_id), 'problem_id':problem_id, 'score':pts, 'set_id':week_id,'timestamp':last_submission_time,'user_id':student_id, 'username':username})

f = open('student_answer.pkl','wb')
pickle.dump(res,f)
f.close()


#for line in res:
#    print line
