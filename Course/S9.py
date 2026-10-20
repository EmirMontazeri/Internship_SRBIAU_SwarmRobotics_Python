import json

A = {
    'BMW':'M5',
    'Porsche':'918'
}
y = json.dumps(A)
print(y)
print(json.dumps(y, indent = 4))

import re
txt = 'My car leak oil'
x = re.search('oil$', txt)
if x:
    print('It needs a service')
else:
    print('All good')

print(dir(re))
