import pickle
import numpy as np
from itertools import combinations
import scipy.io as sio
from numpy import random
import os

labels=np.load('labels_data.npy',allow_pickle='TRUE').item()
partition=np.load('partition.npy,allow_pickle='TRUE').item()

# Function to load file corresponding to ‘ID_val’. Enter your file_path. For example to load a mat file

def get_input(ID_val):
   aa=sio.loadmat(file_path, ID_val+'.mat')
   return( aa )
# Function to load output label corresponding to ‘ID_val’ from dictionary of labels
def get_output( ID_val, label_file ):
   ID_labels = label_file[ID_val] 
   return(ID_labels)
#****************Main code for train generator******************
def image_generator(list_IDs, label_file, batch_size ):
  # INPUT: list_IDs- list containing all the instants used for   training. 
  #OUTPUT-Instants equal to ‘batch_size’ will be provided by this   generator during completion of each epoch
 a=np.arange(0,len(list_IDs),1)
 a_hat=a
 while True:
    batch_path=np.random.choice(a_hat,size=batch_size,replace=False)
    list_IDs_temp = [list_IDs[k] for k in batch_path]
    batch_input = []
    batch_output = []
    # Read each ID, and get labels
    for i, ID in enumerate(list_IDs_temp):
       inp = get_input(ID )
       out_label = get_output(ID,label_file )
       batch_input += [ inp ]
       batch_output += [ out_label ]
    # Return a tuple of (input, output) to feed the network
    batch_x = np.array( batch_input)
    batch_y = np.array( batch_output)
    rem_sample=np.setdiff1d(a_hat,batch_path)
    a_hat=rem_sample
    # The last statement is placed to reset the vector a_hat to #original length. The yield function remembers the state of #variables. So at the end of a iteration, when (size of training #data/batch size) inner epochs will be completed, we need to reset #the vector back to original state for new iteration.If this #condition is missed, you might see that network is trained only for #one iteration.
    if len(rem_sample)<1:
       a_hat=a
    del batch_path
    del list_IDs_temp
    yield( np.asarray(batch_x),to_categorical(batch_y,num_classes=2))
# to_categorical will convert labels into one-hot encoding vector
# **************MAIN code for test generator****************
def image_generator_test(list_IDs, label_file, batch_size ):
  start_id=0
  while True:
    stop_id=start_id+batch_size
    # Select files (paths/indices) for the batch
    batch_path=np.arange(start_id,stop_id)
    list_IDs_temp = [list_IDs[k] for k in batch_path]
    #You can use print(list_IDs_temp) and print(batch_path) to check
    batch_input = []
    batch_output = []
    # Read in each input, perform preprocessing and get labels
    for i, ID in enumerate(list_IDs_temp):
       inp = get_input(ID )
       out_label = get_output(ID,label_file )
       # input = preprocess_input(image=input)
       batch_input += [ inp ]
       batch_output += [ out_label ]
    # Return a tuple of (input, output) to feed the network
    batch_x = np.array( batch_input )
    batch_y = np.array( batch_output )
    start_id=stop_id
    if(stop_id>len(list_ID)-1):
       start_id=0
    del batch_path
    del list_IDs_temp
    yield( np.asarray(batch_x), to_categorical(batch_y, num_classes=2) )
