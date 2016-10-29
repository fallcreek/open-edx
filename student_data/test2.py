import pickle

student_answer = pickle.load(open('pkl/student_answer.pkl','r'))
for line in student_answer:
    print line

