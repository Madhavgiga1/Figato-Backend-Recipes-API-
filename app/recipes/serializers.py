from rest_framework import serializers

from core.models import (Recipe,Tag,Ingredient)

#here we have not overridden the create and update methods
#this is because the create and update methods are already defined in the ModelSerializer class and we dont need to define custom methods
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name']
        read_only_fields=['id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','name']
        read_only_fields=['id']
        
class RecipeSerializer(serializers.ModelSerializer):
    #nested serializer is used to serialize the tags field which is a many to many field
    #nested serializer are serialiwe within serializers that are used to serialize to fields which are objects/model within themselves
    #nested serializers are read only by default which means we cannot create objects with help of nested serializers which means we can only used them to 
    #read from our database and serialise that to JSON but to make objects from incoming JSON Data from a POST request we override that method
    tags=TagSerializer(many=True,required=False)
    
    class Meta:
        #meta is inside the class to define the metadata for the serializer
        model=Recipe
        fields=['id','title','time_minutes','price','link','tags']
        read_only_fields=['id']
    
    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)
            
    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)

        return recipe

    def update(self, instance, validated_data):
        """Update recipe."""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance



class RecipeDetailSerializer(RecipeSerializer):
    #overriding the fields to add the description
    #meta is used to add the fields to the serializer   
    class Meta(RecipeSerializer.Meta):
        #fields is inherited from the parent class serializer
        fields=RecipeSerializer.Meta.fields+['description']




    

