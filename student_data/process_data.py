import pickle
import sys
import MySQLdb
import re
from datetime import timedelta 

printDicOne = False
printDicTwo = False
printDicThree = True

data = pickle.load(open('pkl/student_answer.pkl','rb'))

week_usr = 0
problem_usr = 0
part_usr = 0
if len(sys.argv) >= 4:
  part_usr = sys.argv[3]
if len(sys.argv) >= 3:
  problem_usr = sys.argv[2]
if len(sys.argv) >= 2:
  week_usr = sys.argv[1]

attempt = {}
for line in data:
  if line['timestamp'] == 'null':
    continue
  answer = [line['timestamp'],line['attempt'],line['score'],line['answer']]
  key = (line['set_id'],line['problem_id'],line['part_id'])
  if key not in attempt:
    attempt[key] = {}
  student_key = (str(line['user_id']).replace('L',''),line['username'])
  if student_key not in attempt[key]:
    attempt[key][student_key] = []
  attempt[key][student_key].append(answer)

#-----------------part 1 attempt for each problem------------------#
if printDicOne:
  for problem in attempt:
    id = 1
    if (week_usr != 0 and problem[0] != str(week_usr)) or (problem_usr != 0 and problem[1] != str(problem_usr)) or (part_usr != 0 and problem[2] != str(part_usr)):
      continue 
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print problem
    for student in attempt[problem]:
      print('No:' + str(id) +'---------------------------------------' +  ' week:' + problem[0] + ' problem:' + problem[1] + ' part:' + problem[2])
      id += 1
      print(student)
      for ans in attempt[problem][student]:
        if ans[1] == 'null' or ans[1] == '' or ans[2] == 'null':
          continue
        print(ans)

#------------------part 2: total attempt-------------------#
if printDicTwo:
  print('Total attempt number for each problem part')
  for problem in attempt:
    total_attempt_number = 0
    for student in attempt[problem]:
      for ans in attempt[problem][student]:
        if ans[2] == '0':
          total_attempt_number += 1
        elif ans[2] == '1' or ans[2] == '2':
          break
    print('week:' + problem[0] + ' problem:' + problem[1] + ' part:' + problem[2] + ' total attempts:' +str(total_attempt_number))

#-------------------part 3: hint-------------------------#
if printDicThree == False:
  exit(0)

hint_data = pickle.load(open('pkl/student_hint.pkl','rb'))

#combine two dic
for problem in attempt:
  for student in attempt[problem]:
    if problem in hint_data and student in hint_data[problem]:
      for hint_content in hint_data[problem][student]:
        attempt[problem][student].append(hint_content)
      attempt[problem][student].sort()

for problem in attempt:
    id = 1 
    if (week_usr != 0 and problem[0] != str(week_usr)) or (problem_usr != 0 and problem[1] != str(problem_usr)) or (part_usr != 0 and problem[2] != str(part_usr)):
      continue 
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print problem
    for student in attempt[problem]:
      print('No:' + str(id) +'---------------------------------------' +  ' week:' + problem[0] + ' problem:' + problem[1] + ' part:' + problem[2])
      id += 1
      print(student)
      for ans in attempt[problem][student]:
        if ans[1] == 'null' or ans[1] == '' or ans[2] == 'null':
          continue
        print(ans)
          
