from django.urls import path,include
from rest_framework.routers import DefaultRouter
from recipes import views

#router is used to register the viewsets with the router
router=DefaultRouter()
router.register('recipes',views.RecipeViewSet)

#app_name is used to create urls for the recipes app we add this because we have multiple apps and we want to avoid conflicts
app_name='recipes'

urlpatterns=[
    #'' here is the base url for the recipes app
    path('',include(router.urls))
]

