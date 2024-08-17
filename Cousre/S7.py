x = lambda a : a*4 + 2
print(x(2))

class Car:
  def __init__(make, model, trim):
    make.model = model
    make.trim = trim

  def myfunc(make):
    print('This car is ' + make.model + ' ' + str(make.trim))

p1 = Car('Porsche', 959)
p1.myfunc()
