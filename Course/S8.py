class Car:
    def __init__(self, make, orgin):
        self.maker = make
        self.org = orgin
    
class Model(Car):
    def __init__(self, make, orgin, trim):
        super().__init__(make, orgin)
        self.tri = trim

    def whatcar(self):
        print('This car is a ' + self.maker + ' ' + self.tri + ', made in ' + self.org)

x = Model('Mercedes Bens','Germany','500E')
x.whatcar()  


class Countdown:
     def __iter__(self):
      self.a = 20
      return self
    
     def __next__(self):
        if self.a >= 0:
            x = self.a
            self.a -= 1
            return x
        else:
            raise StopIteration        
counter = iter(Countdown())
for x in counter:
    if x > 0:
        print (x)
    else:
        print('Lift Off')

import platform
A = dir(platform)
print(A)

import math as mat
X = min(2,5,9)
print(X)