import MySQLdb
import sys,json
import pickle

def weekly_data(input_week_id):
  sys.path.insert(0,'/home/edxdeveloper/zyli')
  from generate_answer import generate_answer

 #if len(sys.argv) < 2:
  #  print 'Usage: week_id eg: 2'
  #  exit(0)
  print "generating weekly data"

  print "grabbing from database"
  conn = MySQLdb.connect(host='localhost', user='root', passwd='')
  cursor = conn.cursor()

  cursor.execute(
  "select ch.id, ch.state, c.id as studentmodule_id, c.student_id, a.username from edxapp_csmh.coursewarehistoryextended_studentmodulehistoryextended ch, edxapp.courseware_studentmodule c,edxapp.auth_user a where ch.student_module_id = c.id and a.id = c.student_id and c.module_id like '%problem%' order by c.student_id")

  res = {}
  locationDict = {}

  with open('../locationToProblem.txt', 'r') as f:
    for line in f:
      s=line.strip().split(' ')
      locationDict[s[0]]=[s[1],s[2]]

  print "generating weekly data dict"
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
	
	if week_id != input_week_id:
	  break
	key = (problem_id,str(part_id))
	if 'last_submission_time' not in state:
	  continue
	last_submission_time = state['last_submission_time']
	last_submission_time = last_submission_time.replace('T',' ')
	last_submission_time = last_submission_time.replace('Z','')
	seed = state['seed'] if 'seed' in state else 'null'
	attempt = state['student_answers'][pkey]
	if attempt == '':
	  continue
	if 'correct_map' in state and pkey in state['correct_map']:
	  if state['correct_map'][pkey]['correctness'] == 'incorrect':
	    pts = '0' 
	  else:
	    pts = str(state['correct_map'][pkey]['npoints'])
	else:
	    pts = 'null'
	    continue
	#invalid problem 
	if (week_id == '4' and problem_id == '7' and part_id == 4) or (week_id == '3' and problem_id == '5' and part_id == 2):
	  continue;

	if seed != 'null' and week_id > '2':
	   answer = generate_answer(int(seed),int(week_id),int(problem_id),part_id)
	else:
	   answer = 'null'
	var = [] # leave it blank
	if key not in res:
	  res[key] = []
	res[key].append({'answer':answer, 'attempt':attempt, 'part_id':str(part_id), 'problem_id':problem_id, 'score':pts, 'set_id':'Week' + week_id,'timestamp':last_submission_time, 'user_id':username, 'var':var})

  print "saving to pkl file\n"
  path = 'weekly_pkl/'
  file_name = path + 'Week' + input_week_id + '_data.pkl'
  f = open(file_name,'wb')
  pickle.dump(res,f)
  f.close()

