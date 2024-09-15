from rest_framework import serializers

from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        #model is the model that needs to be serialized
        model = get_user_model()
        #fields is a list of fields that need to be serialized
        fields=['email','password','name']
        #extra_kwargs is a dictionary of extra keyword arguments that need to be passed to the serializer
        extra_kwargs={
            'password':{
                'write_only':True,
                'min_length':5
            }
        }
        #noticer how you have a dictiory with mapps of extra_kwargs: dict[str, dict[str, Any]]
        #this is a dictionary with keys as the field name and values as the dictionary of extra keyword arguments for that field


    def create(self,validated_data):
        #serializer takes the input data and validates it according to the rules defined in the serializer
        #overriding this method for providing custom behavior for creating objects in database from json data received from api
        #this method is called when a POST request is made to the api and returns a user object
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

        return user


###serializers.Serializer, which is a basic serializer class in Django REST Framework. Unlike ModelSerializer, this doesn't automatically create fields based on a model.
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    #Serializer for the user auth token.
    #this is a serializer for the user auth token, it is used to validate the user credentials and return the user object
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        #authenticate is a function that takes the request, username and password and returns the user if the credentials are correct
        #if the credentials are not correct, it returns None
        if not user:
            #if not user, it means the credentials are not correct which means user has value of None
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
        #attrs is a dictionary that contains the validated data, you pass the same in the overriden create method




