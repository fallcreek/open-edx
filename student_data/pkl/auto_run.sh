#!/bin/bash
/usr/bin/python /home/edxdeveloper/zyli/student_data/generate_all_data.py
echo "update succeed!"

cd /home/edxdeveloper/zyli/student_data/pkl/TA_repo

echo "shell script run!!! `date`"
/usr/bin/git pull origin master


cp /home/edxdeveloper/zyli/student_data/pkl/student_answer.pkl /home/edxdeveloper/zyli/student_data/pkl/TA_repo/edX_data_notebook
cp /home/edxdeveloper/zyli/student_data/pkl/student_hint.pkl /home/edxdeveloper/zyli/student_data/pkl/TA_repo/edX_data_notebook



/usr/bin/git add *

/usr/bin/git commit -m "update pkl at `date`"

/usr/bin/git push origin master
