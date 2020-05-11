import numpy as np
c = np.arange(1,4).reshape(1,3)
d = np.arange(4,7).reshape(1,3)
# print(c*2)
# print(d*10)

e = np.arange(1,10).reshape(3,3)
f = np.arange(11,27).reshape(4,4)

# print(e.min(axis=1))
# print(e.min(axis=0))
# print(f.min(axis=1))
# print(f.min(axis=0))

# print(c.dot(e))
# print(d.dot(e))

g = np.arange(1,4,1,dtype='int').reshape(1,3)
h = np.arange(1,2.5,0.5,dtype='float').reshape(1,3)
# print(g*2.5)
# print(h*2.5)

i = np.arange(0,180,30).reshape(2,3)
j = np.sin(i*np.pi/180)

k = np.arange(0,180,30).reshape(2,3)
l = np.cos(k*np.pi/180)

# print(j+l)

m = np.arange(10,100,10).reshape(3,3)
# for z in m.flat:
#     print(z)
# for x in m:
#     print(x)

n = np.arange(0,81).reshape(9,9) # 9*9 = 81, inne opcje to np. 3*27 = 81 
o = n.reshape(3,27)
p = n.reshape(27,3)

r = np.arange(1,12)
for x in r.flat:
    print(x)

s = x.reshape(3,4)

