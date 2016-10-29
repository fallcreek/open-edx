import pickle
import sys

data = pickle.load(open('student_answer.pkl','rb'))

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
  answer = [line['timestamp'],line['attempt'],line['score']]
  key = (line['set_id'],line['problem_id'],line['part_id'])
  if key not in attempt:
    attempt[key] = {}
  student_key = (str(line['user_id']).replace('L',''),line['username'])
  if student_key not in attempt[key]:
    attempt[key][student_key] = []
  attempt[key][student_key].append(answer)

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
      print(ans)


print('Total attempt number for each problem part')
for problem in attempt:
  total_attempt_number = 0
  for student in attempt[problem]:
    total_attempt_number += len(attempt[problem][student])
  print('week:' + problem[0] + ' problem:' + problem[1] + ' part:' + problem[2] + ' total attempts:' +str(total_attempt_number))
