# bitiex/views.py

from __future__ import unicode_literals # for py2

import math

from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from pyecharts import Line, Pie, Page, Bar, Line3D
from pyecharts.constants import DEFAULT_HOST

from django_echarts.views.backend import EChartsBackendView
from django_echarts.views.frontend import EChartsFrontView
from django_echarts.datasets.fetch import fetch

from .models import Bitoex

from django.template import loader

from .demo_data import *


def create_bitoex_line():
    time = [ t[0] for t in Bitoex.objects.values_list('timestamp').reverse()]
    bitoex_sell = [ b[0] for b in Bitoex.objects.values_list('buy').reverse()]
    line = Line('Bitoex buy price')
    line.add('買價', time, bitoex_sell, is_smooth=True)
    return line


ECHARTS_DICT = {
    'bar': create_simple_bar,
    'kine': create_simple_kline,
    'map': create_simple_map,
    'pie': create_simple_pie,
    'line': create_bitoex_line
}


class IndexView(TemplateView):
    template_name = 'bitoex/index.html'


class FrontendEchartsTemplate(TemplateView):
    template_name = 'bitoex/frontend_charts.html'


class BackendEChartsTemplate(EChartsBackendView):
    template_name = 'bitoex/backend_charts.html'

    def get_echarts_instance(self, *args, **kwargs):
        name = self.request.GET.get('name', 'bar')
        if name not in ECHARTS_DICT:
            name = 'bar'
        return ECHARTS_DICT[name]()



