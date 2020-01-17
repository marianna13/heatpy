from heatpy import plot
x1 = 0
x2 = 1
y1 = 0
y2 = 1
b = 1
d = 1
t = 4
C = 1.22
def fn1(x,y):
  return x+y
plot(b,d,C,t,x1,y1,x2,y2,fn, show_solution=True)
