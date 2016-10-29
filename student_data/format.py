import sys,json

res=[]
locationDict = {}

if len(sys.argv) < 3:
  print 'Usage: data_file location_dictionary_file'
  exit(0)

with open(sys.argv[2], 'r') as f:
  for line in f:
    s=line.strip().split(' ')
    locationDict[s[0]]=[s[1],s[2]]

with open(sys.argv[1],'r') as f:
  for line in f:
    fields=line.strip().split('\t')
    state,student_id,username = fields[1],fields[3],fields[4]
    state=json.loads(state)
    seed = state['seed']
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
          pts = state['correct_map'][pkey]['npoints']
      else:
          pts = 'null'
      if pts != '0' and pts != 'null':
        res.append(map(str, [pkey, username, attempt, seed, part_id, problem_id, week_id, pts, last_submission_time]))
      # print '\t'.join(map(str,[attempt, seed, part_id, problem_id, week_id, pts, last_submission_time, username, pkey]))

res=sorted(res, key=lambda x: x[0]+x[1])
for v in res:
  print '\t'.join(v)

# keys = ['attempt', 'pkey', 'score', 'timestamp', 'user_id']
# for i in res:
#   print '\t'.join([i[key] for key in keys])
