from django.urls import path
from voting import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('vote', views.voting, name='voting'),
    path('submit', views.submit, name='submit'),
    path('thanks', views.thanks, name='thanks'),
    path('count',views.count,name='count'),
]
