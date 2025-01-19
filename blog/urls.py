

#urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
   # path('<slug:slug>/', views.post_detail, name='post_detail'),
#]


#urlpatterns = [
    #path('', views.EventsList.as_view(), name='home'),
    #path("", views.event_detail, name="event_detail") ]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventsList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
]
