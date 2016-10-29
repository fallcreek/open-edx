import MySQLdb
import sys,json
import pickle

def weekly_correctness(input_week_id):
  sys.path.insert(0,'/home/edxdeveloper/zyli')
  from generate_answer import generate_answer

#if len(sys.argv) < 2:
#  print 'Please type in week_id. eg: 2'
#  exit(0)
  print "generating weekly correctness data"

  print "grabbing from database"

  conn = MySQLdb.connect(host='localhost', user='root', passwd='')
  cursor = conn.cursor()

  cursor.execute("select c.student_id,a.username,c.state from edxapp.courseware_studentmodule c,edxapp.auth_user a where a.id = c.student_id and c.module_id like '%problem%' order by c.student_id")

  res = {}
  locationDict = {}

  with open('../locationToProblem.txt', 'r') as f:
    for line in f:
      s=line.strip().split(' ')
      locationDict[s[0]]=[s[1],s[2]]

  pre_username = ''

  print "generating weekly correctness dict"
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
	if week_id != input_week_id:
	  break
	problem_key = (problem_id,str(part_id))
	
	if 'last_submission_time' not in state:
	  continue
	last_submission_time = state['last_submission_time']
	last_submission_time = last_submission_time.replace('T',' ')
	last_submission_time = last_submission_time.replace('Z','')
	attempt = state['student_answers'][pkey]
	if attempt == '':
	  continue
	problem_value = [attempt,last_submission_time]
	if username != pre_username:
	  if pre_username != '':
	    res[pre_username] = d
	  pre_username = username
	  d = {}
   
	d[problem_key] = problem_value
	if 'correct_map' in state and pkey in state['correct_map']:
	  if state['correct_map'][pkey]['correctness'] == 'incorrect':
	    continue 
	else:
	    break

  print "saving to pkl file\n"
  path = 'weekly_pkl/'
  file_name = path + 'Week' + input_week_id + '_correct_timestamp.pkl'
  f = open(file_name,'wb')
  pickle.dump(res,f)
  f.close()

