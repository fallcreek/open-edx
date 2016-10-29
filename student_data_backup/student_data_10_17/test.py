import sys

#sys.path.insert(0,'/home/edxdeveloper/data')
#from generate_answer import generate_answer

#print generate_answer(1,3,2,1)

import pickle

#data = pickle.load(open('Week3_data.pkl','rb'))
data = {}
correct_data = pickle.load(open('Week3_correct_timestamp.pkl','rb'))
#correct_data = {}

#for line in  data[('6','1')]:
#  print line

for name in correct_data:
  print '---------------------------------'
  print name
  for line in correct_data[name]:
    print line 
    print correct_data[name][line]

