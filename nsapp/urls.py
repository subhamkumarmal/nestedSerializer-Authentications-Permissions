from django.contrib.auth.views import LoginView
from django.urls import path,include
from . import  views
from django.contrib.auth.views import LoginView,LogoutView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('song',views.SongsView)
urlpatterns=[
    path('',include(router.urls)),
    path('listview',views.ViewsList, name='listview'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/',LogoutView.as_view(next_page='/songs/'),name="logout"),
    path('singer',views.SingerView.as_view(),name='singer'),
    path('writer',views.WriterView.as_view(),name='writer'),

    path('accounts/',include('django.contrib.auth.urls'))
]