# HeatSim
This package helps you solve time-dependent heat equation for any 2d square, at any given time and plots found solutions as 3d surface.

It produces solutions by separating variables, finding simple solutions and after that compining them in one final solution that would satisfy boundary conditions.

Integration is being done by Simpson's rule for numerical integration

You can specify dimensions of the square, boundary conditions and time intervals.
# Installation
```
pip install heatpy
```
# Tutorial
```python
from heatpy import plot

def fn1(x,y):

  return x+y # initial condition

plot(b,d,C,t,x1,y1,x2,y2,fn=fn1, show_solution=True) # b, d are boundary conditions (for more information look into References
```

# References



# Requirements
