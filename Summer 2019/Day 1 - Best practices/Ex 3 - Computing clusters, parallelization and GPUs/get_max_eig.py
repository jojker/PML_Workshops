import numpy as np

def get_max_eig(chunk):
  idx=chunk[1] 
  arry=chunk[0]
  eigvals=np.linalg.eigvalsh(arry)
  #joint_output.put((eigvals.max(),idx))
  return (eigvals.max(),idx)