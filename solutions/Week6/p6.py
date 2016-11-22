import random
def answer(seed):
  random.seed(seed)
  #cannot check answer
  mean = 24;
  sd = random.randrange(30, 50, 1)/10.0#random(3,5,.1);
  k = random.randrange(2,3,1)
  record = 44
  a = k * sd
  b1 = mean - a
  b2 = mean + a
  
  solution1 = "(1-(1/{0}^2))*100".format(k) #{Compute("(1-(1/$k^2))*100")} %.
  solution2 = "0.5*1/(({0}-{1})/{2})^2".format(record, mean, sd)#{Compute("0.5*1/(($record-$mean)/$sd)^2")}
  
  solutions = [solution1, solution2]  
  return solutions
