import MySQLdb
import sys,json
import pickle

sys.path.insert(0,'/home/edxdeveloper/data')
from generate_answer import generate_answer

if len(sys.argv) < 2:
  print 'Usage: week_id eg: 2'
  exit(0)


conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()

cursor.execute("select c.student_id,a.username,c.state from edxapp.courseware_studentmodule c,edxapp.auth_user a where a.id = c.student_id and c.module_id like '%problem%' order by c.student_id")

res = {}
locationDict = {}

with open('locationToProblem.txt', 'r') as f:
  for line in f:
    s=line.strip().split(' ')
    locationDict[s[0]]=[s[1],s[2]]

pre_username = ''

for line in cursor.fetchall():
    state,student_id,username = line[2],line[0],line[1]
    state=json.loads(state)
    
    if 'student_answers' not in state:
      continue
    for pkey in state['student_answers']:
      pid, part_id = pkey.split('_')[0], int(pkey.split('_')[1])-1
      if pid not in locationDict:
        break
      [week_id, problem_id] = locationDict[pid]
      if week_id != sys.argv[1]:
        break
      problem_key = (problem_id,str(part_id))
      
      last_submission_time = state['last_submission_time'] if 'last_submission_time' in state else 'null'
      last_submission_time = last_submission_time.replace('T',' ')
      last_submission_time = last_submission_time.replace('Z','')
      attempt = state['student_answers'][pkey]
      problem_value = [attempt,last_submission_time]
      if username != pre_username:
        if pre_username != '':
          res[pre_username] = d
        pre_username = username
        d = {}
 
      d[problem_key] = problem_value
      if 'correct_map' in state and pkey in state['correct_map']:
        if state['correct_map'][pkey]['correctness'] == 'incorrect':
          break 
      else:
          break

file_name = 'Week' + sys.argv[1] + '_correct_timestamp.pkl'
f = open(file_name,'wb')
pickle.dump(res,f)
f.close()


