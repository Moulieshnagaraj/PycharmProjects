
# import random -->
#--> random.randint(0,10) (start<= N <=end)
#        prints the random integer number [eg..4]



#--> random.uniform(1,111) (start<= N <=end)
#        prints the random float number [eg..345.345176761653]



#--> random.random() (0.0<= N < 1.0)
#        prints the random float number between 0.0 to 1

'''
list=[1,2,3,4,5]
print(random.shuffle(list))--> [3,4,1,5,2] #may vary

list=[3,5,8,9]
print(random.choice(lis))--> 9
'''
# import time
# currenttime=time.clock()
# print(currenttime)
#
# import math
# ss=math.floor(3.97) # -->3
# # math,ceil()
# # s=math.factorial(5.1)
# # # math.exp()
# # math.sqrt()
# print(ss)

# s='predeccesor'
# s[0]='s'
# print(s)

import numpy as np
# num=np.array([[10,20,30],[40,50,60]])
# res1=np.asarray(num,dtype='int',order='f')
s=b'hello world'
# for i in np.nditer(res1):
#     print(i)
c=np.frombuffer(s,dtype='S1',count=4,offset=1)
print(c)