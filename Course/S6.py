i = 1
while i < 15:
    i += 1
    if i == 10:
        continue
    print('Current count is = ',i)

for x in range(1, 100, 10):
    print(x)

for a in [0,1,2]:
    break
print('ended')

def carfinder(*values):
    print('The '+ values[1] + ' of car')
carfinder('Color','Model')