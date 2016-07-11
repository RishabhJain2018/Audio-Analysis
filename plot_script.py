import pandas as pd
import numpy as np 
import plotly.plotly as py 
import plotly.graph_objs as go
import sys, argparse, csv


time=[]
energy=[]

with open('emphasis.csv', 'rb') as csvfile:

	for line in csvfile.readlines():
		array = line.split(',')
		time.append(array[1])
		array1 = array[2].split('\n')
		energy.append(array1[0])

trace1 = go.Scatter(
	x=time, y=energy,
	mode='lines', name='energy'
	)

layout = go.Layout(title='Energy plot', plot_bgcolor='rgb(230, 230, 230)')
fig = go.Figure(data=[trace1], layout=layout)
py.sign_in('RishabhJain1995', '4udghfc3wf')
py.iplot(fig, filename='Emphasis')