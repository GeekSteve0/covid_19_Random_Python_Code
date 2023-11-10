#import datetime

#x = datetime.datetime.now()
#print(x)

#import datetime

#x = datetime.datetime.now()

#print(x.year)
#print(x.strftime("%A"))

import datetime

x = datetime.datetime.now()

print(x.strftime("%c"))

y=3
z=677
bebe=(y is z)
print(bebe)

condition= y<10 and z>1000
print(condition)

t={2, 4, 8, 16, 309, 576, 93}
tech= 93 in t
print(tech)

a = 142
print(a)
a = a << 2
print(a)

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

class myclass():
   def _len_ (self):
    return 1

myobj = myclass()
print(bool(myobj))


