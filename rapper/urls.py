from django.urls import path , include
from . import views

app_name="rapper"

urlpatterns = [


    # path("", views.home_FUNCTIONBASED, name="home"),
    path("", views.home_CLASSBASED.as_view(), name="home"),


    # path("meet-us/", views.meet_FUNCTIONBASED, name="meet"),
    path("meet-us/", views.meet_CLASSBASED.as_view(), name="meet"),

    # path("search/", views.search_FUNCTIONBASED, name="search"),
    path("search/", views.search_CLASSBASED.as_view(), name="search"),

    # path("rapper/<pk>", views.v_rapper_FUNCTIONBASED, name="v_rapper"),
    path("rapper/<pk>", views.v_rapper_CLASSBASED.as_view(), name="v_rapper"),

    # path("article/<pk>", views.v_article_FUNCTIONBASED, name="v_article"),
    path("article/<pk>", views.v_article_CLASSBASED.as_view(), name="v_article"),
]