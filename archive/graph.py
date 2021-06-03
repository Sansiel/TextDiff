import plotly.offline as py
import plotly.graph_objs as go
import os

inp = open('en_out.txt')
x = []
y = []
i = 0
for line in inp:
    line = line.split(' ')
    x.append(i)
    y.append(float(line[1]))
    i += 1

inp.close()

trace = go.Scatter(x=x, y=y)
data = [trace]
layout = go.Layout(
    xaxis=dict(
        type='log',
        autorange=True
        )
)


fig = go.Figure(data=data, layout=layout)
# fig = go.Figure(data=data)

py.plot(fig)