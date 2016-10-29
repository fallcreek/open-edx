import MySQLdb
import sys,json
import pickle
import re
from datetime import timedelta

conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()

student_dic = {}
cursor.execute("select u.id,u.username from edxapp.auth_user as u")

for line in cursor.fetchall():
  student_dic[line[1]] = str(line[0])

cursor.execute("select h.id,h.problem_name,h.problem_part,h.student_username,h.hint_content,h.attempt,h.time_clicked from ucsd_cse103.hint_log as h")

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
    continue
  attempt_hint = line[5]
  if attempt_hint == "no attempt":
    continue
  time = str(line[6]+timedelta(hours=7))
  student_id = student_dic[student_name].replace('L','')

  problem_key = (week_id,problem_id,part_id)
  student_key = (student_id,student_name)
  value = [time,attempt_hint,hint]
  if problem_key not in hint_data:
    hint_data[problem_key] = {}
  if student_key not in hint_data[problem_key]:
    hint_data[problem_key][student_key] = []
  hint_data[problem_key][student_key].append(value)

path = 'pkl/'
f = open(path+'student_hint.pkl','wb')
pickle.dump(hint_data, f)
f.close()
