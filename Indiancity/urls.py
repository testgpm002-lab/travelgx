from django.urls import path
from .views import CityList, City_Detail, Indiancitylist
from .import views

urlpatterns =  [
    path('List/', CityList),
    #path('Detail/<int:pk>', City_Detail),
    path('detail/<int:id>/', City_Detail.as_view()),
    path('', views.index, name="Indiancity"),
]