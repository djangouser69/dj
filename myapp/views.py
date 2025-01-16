from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

import plotly.express as px
import numpy as np

# Create your views here.


def index(r):
    return render(r, "app/index.html")


def test(r):
    return HttpResponse("Test endpoint!")


class About(View):
    def get(s, r):
        return render(r, "app/about.html")


def stuff(r):
    s = np.random.random((100, 2))
    x, y = s[:, 0], s[:, 1]
    c = {
        "plot": px.scatter(x=x, y=y),
        "plot2": px.scatter(x=x * 2, y=y * 0.5),
    }

    c = {
        x: y.to_html(full_html=False)
        for x, y in c.items()
    }
    return render(r, "app/stuff.html", c)


def plot(r):
    i = np.random.random((150, 2))
    x, y = i[:, 0], i[:, 1]
    names = ["plot"]
    plots = [px.scatter(x=x, y=y)]
    context = {
        x: y.to_html(full_html=False)
        for x, y in zip(names, plots)
    }
    return render(r, "app/plot.html", context)


class Gh(View):
    def get(s, r):
        return render(r, "app/gh.html")
