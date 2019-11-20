from sympy import symbols
from sympy.plotting import plot3d
from sympy.plotting import plot
from sympy.functions import exp
from sympy.functions import acos

x,y = symbols('x,y')
#delete the "#" before codes down here
#plot3d(5.3269/(6.28*(1/1.56-1/x)**2+y**2)**0.5, 5.3269/(6.28*(1/1.56-1/x)**2+(0.0604)**2)**0.5, (x,0.1,3), (y,0.0001,0.1))
#plot((5.3269*1.56**2)/(1.56*(1-x)**2+4*1.56**4*x**2*(0.0604)**2)**0.5,(x,0.5,1.5))
#plot3d(-acos((1-x**2)/((1-x**2)**2+4*1.56**2*x**2*y**2)**0.5,), (x,0.1,2), (y,0.0001,0.1))
#plot(-acos((1-x**2)/((1-x**2)**2+4*1.56**2*x**2*0.0604**2)**0.5,), (x,0.1,2))