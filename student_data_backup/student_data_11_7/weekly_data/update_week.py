from generate_weekly_data import weekly_data
from generate_weekly_correctness_data import weekly_correctness
import sys

if len(sys.argv) < 2:
	print "Please enter week number. eg: 2"
	sys.exit(1)
else:
	week_id = sys.argv[1]

weekly_data(week_id)
weekly_correctness(week_id)
