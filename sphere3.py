import math
from xml.dom.minidom import Element
import plotly.express as px

rayon_Vdw_s = {"C": 2.3, "O":2.12,"N":2.15,"S":2.4,"CU":2.0,"CL":2.1}

def fibonacci_sphere(samples=100):
    global rayon_Vdw_s
    coords = data_df.loc[num_atom, ["x", "y", "z"]]
    element = 
    
    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # nombre d'or
    sx =[]
    sy =[]
    sz =[]
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2

        radius = math.sqrt(1 - y * y)  # radius at y
        theta = phi * i  # golden angle increment
        x = math.cos(theta) * radius
        z = math.sin(theta) * radius
        rayon=1.7
        sx.append(rayon * x + 32.465)
        sy.append(rayon * y + 55.196)
        sz.append(rayon * z + 24.877)
        points.append((sx, sy, sz,)) 
    return sx,sy,sz



df=fibonacci_sphere()
fig = px.scatter_3d(df, x=df[0], y=df[1], z=df[2])
fig.show()