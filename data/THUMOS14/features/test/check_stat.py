import numpy as np
import os

folder_path = 'rgb'

f_lst = os.listdir(folder_path)
avg_len=0
min_len=10000
max_len=0

for item in f_lst:
    tmp = np.load(os.path.join(folder_path, item))
    num_seg = tmp.shape[0]
    avg_len += float(num_seg) / len(f_lst)
    if num_seg < min_len:
        min_len = num_seg
    if num_seg > max_len:
        max_len = num_seg

print("avg:{}, min:{}, max:{}".format(avg_len,min_len,max_len))
