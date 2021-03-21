from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html' , redirect_authenticated_user=True ),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    # path('signup/',views.signup_FUNCTIONBASED,name='signup'),
    path('signup/',views.signup_CLASSBASED.as_view(),name='signup'),

    # path("comunity/", views.community_FUNCTIONBASED, name="community"),
    path("comunity/", views.community_CLASSBASED.as_view(), name="community"),

    path("comunity/<pk>", views.s_post, name="s_post"),

]