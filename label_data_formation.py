#code: Create dictionary 'label_data'
import numpy as np
num_abnormal=100
labels1 = {}
for j in range(1,num_abnormal+1):
 id_j=str(j)+'_AB’
 labels1[id_j] = 1
 del num_abnormal
num_normal=100
labels2={}
for j in range(1,num_normal+1):
  id_j=str(j)+'_NOR’
  labels2[id_j] =0
# merge two dictionary
labels2.update(labels1)
# Save as numpy file
np.save(‘labels_data.npy’, labels2)
