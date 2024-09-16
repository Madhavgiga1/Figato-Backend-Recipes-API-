from rest_framework import serializers

from core.models import Recipe

#here we have not overridden the create and update methods
#this is because the create and update methods are already defined in the ModelSerializer class and we dont need to define custom methods
class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        #meta is inside the class to define the metadata for the serializer
        model=Recipe
        fields=['id','title','time_minutes','price','link']
        read_only_fields=['id']

class RecipeDetailSerializer(RecipeSerializer):
    #overriding the fields to add the description
    #meta is used to add the fields to the serializer   
    class Meta(RecipeSerializer.Meta):
        #fields is inherited from the parent class serializer
        fields=RecipeSerializer.Meta.fields+['description']

