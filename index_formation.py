def index_formation(id_arr,FLAG):
  #INPUT:id_arr :list containing indices of subjects.
  #       FLAG: str containing name of class
  #OUTPUT: id_list: list containing name of subjects in form of #SubjectNumber_ClassName. Ex: 2nd subject from class NORMAL will be named as 2_NOR
 id_list=[]
 if FLAG==’NOR’:
  # convert to desired format for NORMAL
  for i in range(len(id_arr)):
    id_int=id_arr[i]
    id_str=str(id_int)+’NOR’
    id_list.append(id_str)
 if FLAG==’AB’:  
  # convert to desired format for ABNORMAL
   for i in range(len(id_arr)):
      id_int=id_arr[i]
      id_str=str(id_int)+’_AB’
      id_list.append(id_str)
return id_list
