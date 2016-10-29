import MySQLdb
import sys,json
import pickle
import re

conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()

student_dic = {}
cursor.execute("select u.id,u.username from edxapp.auth_user as u")

for line in cursor.fetchall():
  student_dic[line[1]] = str(line[0])

#cursor.execute("select h.id,h.problem_name,h.problem_part,h.student_username,h.hint_content,h.attempt,h.time_clicked,u. from ucsd_cse103.hint_log as h,edxapp.auth_user as u ")

hind_data = {}
#for line in cursor.fetchall():
#  week_id = re.search('Week(.+?)_', line[1]).group(1)
#  problem_id = re.search('Problem(.+?)', line[1]).group(1)
#  part_id = line[2]
#  key = (week_id,problem_id,part_id)
#  username = line[3]

with open('show_hint.log','r') as f:
  res = {}
  for line in f.readlines():
    if 'student_name' and '</font>' in line:
      student_name_matchobj = re.search('student_name ([^,]+?),',line)
      if student_name_matchobj:
        student_name = student_name_matchobj.group(1)
      else:
        continue
      week_id = re.search('week(.+?)problem',line).group(1)
      week_sign = "week" + week_id
      problem_id = re.search(week_sign + 'problem(.+?)part',line).group(1)
      part_id = re.search('part(.+?),',line).group(1)
      hint = re.search('Hint: (.+?)</font>',line).group(1)
      attempt = re.search('attempt(.+?).',line).group(1)
      time = re.search('(.+?),',line).group(1)
      student_id = student_dic[student_name].replace('L','')
      problem_key = (week_id,problem_id,part_id)
      student_key = (student_id,student_name)
      value = (time,attempt,hint)
      if problem_key not in res:
        res[problem_key] = {}
      if student_key not in res[problem_key]:
        res[problem_key][student_key] = []
      res[problem_key][student_key].append(value)






