# HeatPy
This package helps you solve time-dependent heat equation for any 2d square, at any given time and plots found solutions as 3d surface.

It produces solutioThis package helps you solve time-dependent heat equation for any 2d square, at any given time and plots found solutions as 3d surface.

It produces solutions by separating variables, finding simple solutions and after that combining them into one final solution that would satisfy boundary conditions.

Integration is being done by Simpson's rule for numerical integration.

You can specify dimensions of the square, boundary conditions and time intervals.ns by separating variables, finding simple solutions and after that compining them in one final solution that would satisfy boundary conditions.

Integration is being done by Simpson's rule for numerical integration

You can specify dimensions of the square, boundary conditions and time intervals.
# Installation
```
pip install heatpy
```
# Tutorial
C is a thermal diffusivity,
t is time,
x2-x1 is size of a square in X direction,
y2-y1 is size of the square in Y direction

```python
from heatpy import plot

def fn1(x,y):

  return x+y # initial condition

plot(b,d,C,t,x1,y1,x2,y2,fn=fn1, show_solution=True) # b, d are boundary conditions (for more information look up References)
```

# References

http://ramanujan.math.trinity.edu/rdaileda/teach/s12/m3357/lectures/lecture_3_6_short.pdf

https://plot.ly/python/3d-surface-plots/

# Requirements

Plotly >= 4.4

Numpy >= 1.10

Python >= 3.6
