from django.urls import path, re_path

from . import views

urlpattern = [
  path('article/2003', views.special_case2003),
  re_path(r'^articles/(?P<year>[0-9]{4})', views.year_archive),
  re_path(r'^articles/(?P<year>[0-9]{4})', views.month_archive),
  re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>)[0-9]{2}/(?P<slug>[\w-]+)/$', views.article_detail),
]