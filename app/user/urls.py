#urls.py is used to define the urls for the api
from django.urls import path 
#importing the views from the views.py file
from user import views
#importing the CreateUserView from the views.py file


urlpatterns= [
    #path is used to define the url for the api
    #'create/' is the url for the api
    #views.CreateUserView.as_view() is the view for the api
    #name='create' is the name of the url
    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
