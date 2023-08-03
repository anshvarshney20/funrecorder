from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('display/', views.display, name='display'),
    path('update/<int:id>/', views.update, name='update'),
    path('drop/<str:pk>/', views.drop, name='drop'),
    path('modify/<str:pk>/', views.modify, name='modify'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('post/', views.post, name='post'),
    

]
