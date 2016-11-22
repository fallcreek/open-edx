import pickle

student_answer = pickle.load(open('pkl/student_hint.pkl','r'))
for line in student_answer:
    if line[0] == '5':
	print student_answer[line]

