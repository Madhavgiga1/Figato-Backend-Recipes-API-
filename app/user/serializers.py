from rest_framework import serializers

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        #model is the model that needs to be serialized
        model = get_user_model()
        #fields is a list of fields that need to be serialized
        fields=['email','password','name']
        #extra_kwargs is a dictionary of extra keyword arguments that need to be passed to the serializer
        extra_kwargs={
            'password':{
                'write_only':True,'min_length':5
            }
        }


    def create(self,validated_data):
        #serializer takes the input data and validates it according to the rules defined in the serializer
        #overriding this method for providing custom behavior for creating objects in database from json data received from api
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance,validated_data):
        #overriding this method for providing custom behavior for updating objects in database from json data received from api
        #instance is the existing object in the database that needs to be updated
        #validated_data is the new data that needs to be updated

        password = validated_data.pop('password')
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()




