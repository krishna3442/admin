from django.conf.urls import url
from one import views



app_name = 'one'

urlpatterns=[
    #url(r'^update/$',views.update,name='update'),
    url(r'^(?P<pk>\d+)/$',views.detail.as_view(),name='detail'),
    url(r'^$',views.userlogin.as_view(),name='list'),
    url(r'^update/(?P<pk>\d+)/$',views.update.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.delete.as_view(),name='delete'),
    url(r'^appointment$',views.appointment,name='appointment'),
    url(r'^doctor_list$',views.doctor_list,name='doctor_list'),
    url(r'^detail$',views.details,name='detail'),
    url(r'^booking$',views.booking,name='booking'),



]
