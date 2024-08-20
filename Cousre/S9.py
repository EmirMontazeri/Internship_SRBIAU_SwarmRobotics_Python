import json

A = {
    'BMW':'M5',
    'Porsche':'918'
}
y = json.dumps(A)
print(y)
print(json.dumps(y, indent = 4))