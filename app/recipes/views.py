"""
Views for the recipe APIs
"""
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
    Ingredient,
)
from recipes import serializers


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
        elif self.action == 'upload_image':
            return serializers.RecipeImageSerializer

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

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseRecipeAttrViewSet(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for recipe attributes."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database."""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()