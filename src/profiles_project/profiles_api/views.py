from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloAPIView(APIView):
    """Test APIView."""

    serializer_class=serializers.HelloSerializer

    def get(self,resquest,format=None):
        """Resturns a list of APIView features."""

        an_apiview=[
        'Uses HTTP methods as functions(get, post, put, patch, delete)',
        'It  is similar to django views.',
        'Gives full control over your logic.',
        'Is mapped manually to URLs.'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,resquest):
        """Create a hello message with our name."""

        serializer=serializers.HelloSerializer(data=resquest.data)


        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUESTS)


    def put(self,resquest,pk=None):
        """Handles updating an object."""

        return Response({'method':'put'})



    def patch(self,resquest,pk=None):
        """Patch resquest, only updates fields provided n the request."""


        return Response({'method':'patch'})


    def delete(self,resquest,pk=None):
        """Deletes an object."""


        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test APIViewSet"""

    def list(self,request):
        """Return a hello message"""

        a_viewset=[
        'Uses actions(list,create,retrieve,update,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionaliry with less code'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Create new hello message"""


        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format('name')

            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUESTS)



    def retrieve(self,request,pk=None):
        """Handles getting an object by it ID."""


        return Response({"http_method":'GET'})

    def update(self,request,pk=None):
        """Handles getting an object by it ID."""


        return Response({"http_method":'PUT'})

    def partial_update(self,request,pk=None):
        """Handles getting an object by it ID."""


        return Response({"http_method":'PATCH'})

    def destroy(self,request,pk=None):
        """Handles getting an object by it ID."""


        return Response({"http_method":'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles."""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
