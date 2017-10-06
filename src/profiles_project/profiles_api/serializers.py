from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name=serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile."""

    class Meta:
        model=models.UserProfile()
        fields=('id','email','name','password')
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validates_data):
        """Create and return new user."""

        user=models.UserProfile(
        email=validates_data['email'],
        name=validates_data['name']
        )

        user.set_password(validates_data['password'])
        user.save()

        return user
