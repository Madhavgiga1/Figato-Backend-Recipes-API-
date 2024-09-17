
from rest_framework import viewsets
from recipes import serializers
from core.models import Recipe,Tag,Ingredient
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
class RecipeViewSet(viewsets.ModelViewSet):
    # is an instance of the serializer class defined for this view.
    serializer_class=serializers.RecipeDetailSerializer
    queryset=Recipe.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        #if the action is list then we want to return the RecipeDetailSerializer 
        #the list action is used to get the list of the recipes
        if self.action=='list':
            return serializers.RecipeSerializer
        #For the other actions we want to return the RecipeDetailSerializer
        #action is the action that is being performed like retrieve,update,destroy etc
        return self.serializer_class
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
       
       
        #in the recipe model we have a user field which is a foreign key to the user model
        #ensures that when a new recipe is created, it's associated with the user who made the request
        #Flow:
        #API request comes in -> View's create method is called
        #Serializer validates data
        #perform_create is called by the view
        #perform_create calls serializer.save() with the additional user data
        #save is the method that is used to save the data to the database
        #self.request.user is the user that is authenticated
        #the user is the user that is authenticated


#class TagViewSet(APIView,mixins.listmodelmixins):
class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class=serializers.TagSerializer
    queryset=Tag.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
class IngredientViewSet(mixins.ListModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class=serializers.IngredientSerializer
    queryset=Ingredient.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
    

  
