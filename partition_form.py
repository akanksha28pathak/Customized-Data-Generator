import numpy
from numpy import random


def index_formation(id_arr,FLAG):
  #INPUT:id_arr :list containing indices of subjects.
  #       FLAG: str containing name of class
  #OUTPUT: id_list: list containing name of subjects in form of SubjectNumber_ClassName. Ex: 2nd subject from class NORMAL will be named as 2_NOR
 id_list=[]
 if FLAG=='NOR’:
  # convert to desired format for NORMAL
  for i in range(len(id_arr)):
    id_int=id_arr[i]
    id_str=str(id_int)+'NOR’
    id_list.append(id_str)
 if FLAG=='AB’:  
  # convert to desired format for ABNORMAL
   for i in range(len(id_arr)):
      id_int=id_arr[i]
      id_str=str(id_int)+'_AB’
      id_list.append(id_str)
return id_list

partition={}     # initialize dictionary
# generate sequence of original instants in each class
num_normal=np.arange(1,100,1) # 100 refers to number of instants of NORMAL
num_ab=np.arange(1,100,1)
# number of instants for testing from both class
normal_test=20
ab_test=20
# number of instants for validation from both class
normal_valid=20
ab_valid=20
# number of instants for training from both class
normal_train=60
ab_train=60
# initialize empty list
test_id_list=[]
train_id_list=[]
valid_id_list=[]
# select test id without replacement
test_id_nor=np.random.choice(num_normal,normal_test,replace=False)
test_nor_list=index_formation(test_id_nor,'NOR')
test_id_list.extend(test_nor_list)
del test_nor_list
test_id_ab=np.random.choice(num_ab,ab_test,replace=False)
test_ab_list=index_formation(test_id_ab,'AB')
test_id_list.extend(test_ab_list)
del test_ab_list
# collect remaining indices for validation and trainig
valid_train_nor=np.setdiff1d(num_normal, test_id_nor)
valid_train_ab=np.setdiff1d(num_ab,test_id_ab)
# select train index from remaining indices
train_id_nor=np.random.choice(valid_train_nor,normal_train,replace=False)
train_nor_list=index_formation(train_id_nor,'NOR')
train_id_list.extend(train_nor_list)
del train_nor_list
train_id_ab=np.random.choice(valid_train_ab,ab_train,replace=False)
train_ab_list=index_formation(train_id_ab,'AB')
train_id_list.extend(train_ab_list)
del train_ab_list
# collect remaining indices for validation
valid_rem_nor=np.setdiff1d(valid_train_nor,train_id_nor)
valid_id_nor=np.random.choice(valid_rem_nor,normal_valid,replace=False)
valid_nor_list=index_formation(valid_id_nor,'NOR')
valid_id_list.extend(valid_nor_list)
del valid_nor_list
del valid_id_nor
valid_rem_ab=np.setdiff1d(valid_train_ab,train_id_ab)
valid_id_ab=np.random.choice(valid_rem_ab,ab_valid,replace=False)
valid_ab_list=index_formation(valid_id_ab,'AB')
valid_id_list.extend(valid_ab_list)
del valid_ab_list
del valid_id_ab
partition['test']= test_id_list
partition['train']= train_id_list
partition['validation']= valid_id_list
#save the dictionary in form of numpy file
np.save('partition.npy', partition) 
