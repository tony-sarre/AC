from django.db import models
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np



def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def generate_pie_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Classication of crimes')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.figure(figsize=(4, 4))
    image_file = buf.read()
    graph = base64.b64encode(image_file)
    graph = graph.decode('utf-8')
    buf.close()
    return graph
    #return buf

def plot_view(n):
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, bins=50, density=True, histtype='step', cumulative=-1)
    plt.figure(figsize=(5, 5))
    plt.title("Frequency of not sécurity")
    plt.plot(n)
    plt.xlabel('Title')
    plt.ylabel('Frequency')
    figfile =BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    return figdata_png
    #return render(request, 'plot.html', {'figdata_png':figdata_png})

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('Sensitive area')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Location')
    plt.ylabel('Title')
    plt.tight_layout()
    graph=get_graph()
    return graph


def get_plot2(X,Y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('Sensitive periode')
    plt.plot(X,Y)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Title')
    plt.tight_layout()
    graph=get_graph()
    return graph

