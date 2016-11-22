import random
def answer(seed):
  random.seed(seed)
  import numpy as np
  
  X_vals=np.array([1,2,3])
  Y_vals=np.array([1,2,3])
  
  # this imd can generate a number of different problems, each for a different matrix
  # the matrices are specified here:
  
  matrices={'dep_corr1':np.array([[1./3,0,0],[0,1./3,0],[0,0,1./3]]),
            'indep_uncor': np.array([[.1,0,.4],[0,0,0],[.1,0,.4]]),
            'dep_uncor': np.array([[.2,0,.2],[0,.2,0],[.2,0,.2]])
            }
  
  matrices_str = {
  'dep_corr1':np.array([["1/3","0","0"],["0","1/3","0"],["0","0","1/3"]]),
  'indep_uncor': np.array([["0.1","0","0.4"],["0","0","0"],["0.1","0","0.4"]]),
  'dep_uncor': np.array([["0.2","0","0.2"],["0","0.2","0"],["0.2","0","0.2"]])
            }
  
  joint=matrices['dep_corr1']
  joint_str = matrices_str['dep_corr1']
  
  joint00 = joint_str[0,0]
  joint01 = joint_str[0,1]
  joint02 = joint_str[0,2]
  joint10 = joint_str[1,0]
  joint11 = joint_str[1,1]
  joint12 = joint_str[1,2]
  joint20 = joint_str[2,0]
  joint21 = joint_str[2,1]
  joint22 = joint_str[2,2]
  
  
  marginal_X = np.sum(joint,axis=0)
  marginal_Y = np.sum(joint,axis=1)
  
  mean_X=np.dot(marginal_X,X_vals)
  mean_Y=np.dot(marginal_Y,Y_vals)
  
  X_Nvals=X_vals-mean_X
  Y_Nvals=Y_vals-mean_Y
  
  var_X=np.dot(marginal_X,X_Nvals**2)
  var_Y=np.dot(marginal_Y,Y_Nvals**2)
  
  xy=np.outer(Y_vals,X_vals)
  Nxy=np.outer(Y_Nvals,X_Nvals)
  
  Cov = np.sum(np.multiply(Nxy,joint))
  Exy = np.sum(np.multiply(xy,joint))
  
  #print Exy, Cov, Cov/np.sqrt(var_X*var_Y)
  independent = 0.01 > np.sum((np.outer(marginal_Y,marginal_X)-joint)**2)
  
  # Dist of X
  solution1="+".join(joint_str[:,0])
  solution2="+".join(joint_str[:,1])
  solution3="+".join(joint_str[:,2])
  marginal_X_str = [solution1, solution2, solution3]
  solution4="+".join(["((%s) * (%.2f))"%(marginal_X_str[i],X_vals[i]) for i in range(len(X_vals))])
  solution5="+".join(["((%s) * ((%.2f)^2))"%(marginal_X_str[i],X_Nvals[i]) for i in range(len(X_vals))])
  
  # Dist of Y
  solution6="+".join(joint_str[0,:])
  solution7="+".join(joint_str[1,:])
  solution8="+".join(joint_str[2,:])
  marginal_Y_str = [solution6, solution7, solution8]
  solution9="+".join(["((%s) * (%.2f))"%(marginal_Y_str[i],Y_vals[i]) for i in range(len(Y_vals))])
  solution10="+".join(["((%s) * ((%.2f)^2))"%(marginal_Y_str[i],Y_Nvals[i]) for i in range(len(Y_vals))])
  
  #Interactions between X and Y
  flat_xy=xy.flatten()
  flat_joint=joint_str.flatten()
  solution11="+".join(["((%s) * (%.2f))"%(flat_joint[i],flat_xy[i]) for i in range(len(flat_xy))])
  solution12="{0}-({1}*{2})".format(Exy,mean_X,mean_Y)
  solution13="{0}/sqrt({1}*{2})".format(Cov,var_X,var_Y)
  solution14=str(1*independent)
  solutions=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8,solution9,solution10,solution11,solution12,solution13,solution14]
  return solutions
