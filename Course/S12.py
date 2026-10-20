# x = input('enter pass')

# if int(x) == 5:
#     try:
#         print(y)
#     except:
#         print('No y available')
#         print('x is ',x)

#     txt = f'the number was {5:.2f}'
#     print(txt)    

#     a = False
#     if a == False:
#         raise Exception('no y was found')

# else:
#     print('wrong number')


# car = 'Mercedes Benz'
# model = 'CLK GTR'
# year = '1999'
# text = 'this car is {0} {1}, from {2}'
# print(text.format(car, model, year))

# f = open('testfile.txt', 'w')
# # print(f.read())
# # for a in f:
# #     print(a)

# f.write('BOOM')
# f.close()
# f = open('testfile.txt', 'r')
# print(f.read())

# import os 
# walk = os.walk('\\')

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.ndim)
print(a[1, 1])