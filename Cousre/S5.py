A = {
    'BMW':'M5',
    'Porsche':'918'
}

print(A['BMW'])

(a,b) = list(A.items())[1]
print(a,b)

NewA = dict(BMW='M5',Code='E39')
print(NewA)

SuperDict = {
    'Brand':'BMW',
    'Class':'5 Series',
    'Gen':'E39',
    'Model':'M5'
}
SuperDict.update({'Year':'1999'})
SuperDict['Color'] = 'Deep Blue'
print(SuperDict)
print(SuperDict['Model'])

if SuperDict.__hash__:
    print('Hashable')
else:
    print('NOPE!')