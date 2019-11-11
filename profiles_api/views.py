from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api.serializers import ProfileSerializer,UserProfileSerializer,ProfileFeedItemSerializer
from profiles_api import models,permissions
# Create your views here.

class ProfileAPIView(APIView):
    '''testing api views'''
    serializer_class = ProfileSerializer
    def get(self, request, format=None):
        '''testing get method for api '''
        an_api=[
            'This is first time I am using api',
            'Another List Item',
            'One more added'
        ]
        return Response({'Hello':'Hello Api View','an_api':an_api})

    def post(self, request):
        '''testing post api view'''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            data = serializer.validated_data.get('name')
            message = 'hello'+ ' ' + data
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Put APIView updates the whole object'''
        return Response({'Method':'Put'})

    def patch(self, request, pk=None):
        '''Patch Partially updates the object'''
        return Response({'Method':'Patch'})

    def delete(self, request, pk=None):
        '''It deletes the object'''
        return Response({'Method':'Delete'})


class ProfileViewSet(viewsets.ViewSet):
    '''Api Handling using viewset'''
    serializer_class = ProfileSerializer

    def list(self, request):
        '''Handles listing of objects'''
        a_view = [
            'It handles the api requests',
            'It is very useful'
        ]
        return Response({'message':'Hello-View','a_view':a_view})

    def create(self, request):
        '''Handles Post Method'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''handles Retrieving particular object'''
        return Response({'Http_Method':'GET'})

    def update(self, request, pk=None):
        '''It handles updating the object'''
        return Response({'Http_Method':'PUT'})

    def partial_update(self, request, pk=None):
        '''It handles partially updating the object'''
        return Response({'Http_Method':'PATCH'})

    def destroy(self, request, pk=None):
        '''It handles destroying the object'''
        return Response({'Http_Method':'Delete'})


class UserProfileViewset(viewsets.ModelViewSet):
    '''ViewSet to handle user Profiles'''
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ['email','name']

class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentication tokens'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''handles creating, reading and updating feed items'''
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        '''Sets the user profile to the logged in user'''
        serializer.save(user_profile = self.request.user)
