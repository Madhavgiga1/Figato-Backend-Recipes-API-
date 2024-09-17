from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
import uuid
import os 

#instance parameter represents the instance of the model where the file is being attached. In this context, it would be an instance of the Recipe model
#filename: This parameter represents the original name of the file being uploaded.
#os.path.splitext(filename):
#  This function splits the filename into a tuple (root, ext), where root is the filename without the extension and ext is the file extension.
#uuid.uuid4(): 
# This generates a random UUID (Universally Unique Identifier). UUIDs are used to ensure that the filename is unique.
#f'{uuid.uuid4()}{ext}': This is an f-string, a way to format strings in Python. It combines the UUID and the file extension to create a new, unique filename.
def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)
# When a new image is uploaded for a recipe, this function will generate a unique file path for the image. For example, 
# if the original filename is image.jpg, the function might generate a path like uploads/recipe/123e4567-e89b-12d3-a456-426614174000.jpg.

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have an email address')
        #**extra_fields s to provide any number of keyword arguments
        #BaseUserManager inherits from models.Manager, which handles database operations.self._db is typically set in the BaseUserManager constructor.
        #Purpose:
        #It specifies which database to use when saving the user object.
        #The actual database connection is managed by Django's ORM.

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'

class Recipe(models.Model):
    #if user is deleted then related recipes will be deleted too
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title= models.CharField(max_length=255)
    description=models.TextField(blank=True)
    time_minutes=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    link=models.CharField(max_length=255,blank=True)
    tags=models.ManyToManyField('Tag')
    ingredients=models.ManyToManyField('Ingredient')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    def __str__(self):
        return self.title 

class Tag(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

class Ingredient(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name