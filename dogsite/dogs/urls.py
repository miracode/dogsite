from django.conf.urls import patterns, url
from dogs import views

urlpatterns = patterns('',
    url(r'^dog/create/', views.DogCreateView.as_view(), name='dog-create'),
    url(r'^$', views.index, name='index'),
    url(r'^dog/success/(?P<dog>\w+)/$', views.success, name='dog-success'),
    url(r'^dog/all', views.DogListView.as_view(), name='dog-list'),
    url(r'^dog/(?P<pk>\d+)/$', views.DogDetailView.as_view(), name='dog-detail'),
    url(r'^search-form/$', views.search_form, name="search-form"),
    url(r'^search/$', views.search, name="search"),
)
