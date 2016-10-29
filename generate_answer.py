from pydoc import locate
def generate_answer(seed, week_id, problem_id, part_id):
  try:
    seed = int(seed)
  except Exception as e:
    print 'Seed incorrect.'
    raise e
  f=locate('solutions.Week{}.p{}'.format(week_id, problem_id))
  if f == None:
    return 'week or problem invalid.'
  return f.answer(seed)[part_id-1]
