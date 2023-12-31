import numpy as np

np.arange(5) #[0. 1. 2. 3. 4.]
np.arange(1, 5) #[1. 2. 3. 4.]
np.arange(1, 10, 2) #[1. 3. 5. 7. 9.]

arr = np.arange(4) # [0. 1. 2. 3.]
arr.reshape((2, 2)) 
# [[0,1]
#  [2,3]]

arr2 = np.arange(9) # [0. 1. 2. 3. 4. 5. 6. 7. 8.]
arr2.reshape((3,3))
#[[0. 1. 2.]
# [3. 4. 5.]
# [6. 7. 8.]]


np.zeros(3)  
# [0., 0., 0.]

np.zeros((2,3))
#[[0., 0., 0.],
# [0., 0., 0.]]


a = np.array([[1,0,0], [0,2,0], [1,1,0]])
idx = np.nonzeros(a)  
# 第一个数组表示非零元素的行索引,第二个数组表示非零元素的列索引。
# ([0, 1, 2, 2], 
# [0, 1, 0, 1]) 

a[idx] 
# 返回非零元素的值
# [1,2,1,1]


a = np.eye(3)
#[[1. 0. 0.] 
# [0. 1. 0.] 
# [0. 0. 1.]]

a = np.eye(3,2)
#[[1. 0.] 
# [0. 1.] 
# [0. 0.]]

#也可以通过设置k参数,来构造一个主对角线之外的对角线为1的矩阵
a = np.eye(3,k=1)
# k=1表示主对角线右上方一位为1
#[[0. 1. 0.]
# [0. 0. 1.]
# [0. 0. 0.]]


np.random.rand(3, 3)
#[[0.3412401  0.75793446 0.73821231]
# [0.73567422 0.66104655 0.62892359]
# [0.93455608 0.65246547 0.61814169]]


np.random.random(3)
# [0.33624381 0.96582921 0.88196345]


np.random.randn(3, 3)
#[[-0.00884917  0.30352057 -1.6507589 ]
# [-1.56816702  1.26553868 -0.49313447]
# [ 0.53054383 -0.54938674  0.26032079]]


np.random.randint(0,10,size=(3,3))
#[[8 1 2]
# [9 7 9]
# [0 4 5]]


np.random.choice([1,2,3,4], size=(3,3))
#[[1 3 4]
# [2 2 3]
# [1 3 3]]
