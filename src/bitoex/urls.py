# bitoex/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^frontend_chart_list/$', views.FrontendEchartsTemplate.as_view(), name='frontend_chart_list'),
    #url(r'^backend_chart_list/$', views.FrontendEchartsTemplate.as_view(), name='backend_chart_list'),
    url(r'^backend_chart_list/$', views.BackendEChartsTemplate.as_view(), name='backend_chart_list'),
    #url(r'^line_demo_page/$', views.line, name='line_demo_page')   
]