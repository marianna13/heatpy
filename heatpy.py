import numpy as np
def plot(b,d,C,t,x1,y1,x2,y2,fn, show_solution=False):
  '''
    This function finds solutions.
    b,d : boundary conditions,
    C : thermal diffusivity
    t : time
    x2-x1 : size of a square in X direction,
    y2-y1 : size of the square in Y direction,
    fn : initial condition
    '''
  import plotly.graph_objects as go

  def solve(b,d,C,t,x1,y1,x2=None,y2=None,fn=None):
  
    a=0

    c=0
    def f1(x,y):

      return x-y-2


    def f(x,y,m,n,fn):
      if fn!=None:
        return fn(x,y)*np.sin(m*np.pi/b*x)*np.sin(n*np.pi/d*x)
      return f1(x,y)*np.sin(m*np.pi/b*x)*np.sin(n*np.pi/d*x)


    def s(a,b,c,d,m,n,fn):

      s = (16*f((b+a)/2,(c+d)/2,m,n,fn)+4*f((b+a)/2,d,m,n,fn)+4*f((b+a)/2,c,m,n,fn)+4*f((b+a)/2,d,m,n,fn)+4*f(b,(d+c)/2,m,n,fn)+4*f(a,(d+c)/2,m,n,fn)+f(b,d,m,n,fn)+f(a,d,m,n,fn)+f(a,c,m,n,fn)+f(b,c,m,n,fn))*(b-a)*(d-c)/36
      return s


    def A(m,n, a,b,c,d,fn):
      '''
   This function finds coefficients A using double 
   Fourier transform
   '''
      return 4/(b*d)*s(a,b,c,d,m,n,fn)


    def u(a,b,c,d,C,t,X,Y,fn):
      '''
   This function finds 
   a general solution by summing partial solutions
   '''
      u=0
      for m in range(1,50):
        for n in range(1,50):
          mu = m*np.pi/b
          nu = n*np.pi/d
          lmn = C*np.sqrt(mu**2+nu**2)
          u+=(A(m,n,a,b,c,d,fn)*np.sin(mu*X)*np.sin(nu*Y)*np.exp(-lmn**2*t))
      return u


      if x2==None:
        return int(x1),int(y1),u(a,b,c,d,C,t,x1,y1,fn)

    X = np.linspace(x1,x2,2)
    Y = np.linspace(y1,y2,2)


    X,Y = np.meshgrid(X,Y)
    return X,Y,u(a,b,c,d,C,t,X,Y,fn)



  X,Y,ut = solve(b,d,C,t,x1,y1,x2,y2,fn=fn)
  if show_solution:
    print(ut)
  fig = go.Figure(data=[go.Surface(z=ut, x=X, y=Y)])
  fig.update_layout(title='', autosize=True,
          width=500, height=500,
          margin=dict(l=65, r=50, b=65, t=90))
  fig.show()
