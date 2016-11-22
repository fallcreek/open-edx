This dictionary contains the following files/dictionaries :
auto_run.sh  combined.pkl  cronerror  cronlog  student_answer.pkl  student_hint.pkl  TA_repo

TA_repo :  local copy of a repository in github, and push new update every three hours.
student_answer.pkl & student_hint.pkl : data that will be updated every three hours(by a crontab -e job: auto_run.sh, it first run the python script - generate_all_date.py).
combined.pkl : the combination of student_answer.pkl and student_hint.pkl
auto_run.sh : a crontab job that will be executed every three hours.
	      This shell script do the following things:
		  1. run python script to updat pkl from database
		  2. pull TA_repo from github
                  3. copy student_answer.pkl and student_hint.pkl to TA_repo
                  4. commit the update and push
cronerror & cronlog : the run log and error log of this cron job - auto_run.sh.


