import numpy as np
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from plotly.offline import plot

# Create your views here.


class Index(View):
    def get(s, r):
        a = np.random.random((100, 2))
        x, y = a[:, 0], a[:, 1]
        plots = [
            px.scatter(x=x, y=y),
            px.histogram(x=x),
            px.box(x=x),
            px.area(x=x, y=y),
        ]
        return render(
            r,
            "app/offline.html",
            {
                x: y
                for x, y in zip(
                    "abcde",
                    [
                        plot(x, output_type="div")
                        for x in plots
                    ],
                )
            },
        )


class Second(View):
    def get(s, r):
        a = np.random.random((150, 2))
        x, y = a[:, 0], a[:, 1]
        plots = [
            px.scatter(x=x, y=y),
            px.violin(y=x),
            px.scatter(x=x * 5, y=y),
            px.ecdf(y=y),
        ]
        return render(
            r,
            "app/full.html",
            {
                x: y
                for x, y in zip(
                    "abcde",
                    [
                        x.to_html(full_html=False)
                        for x in plots
                    ],
                )
            },
        )
