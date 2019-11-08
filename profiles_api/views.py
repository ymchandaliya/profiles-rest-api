from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api.serializers import ProfileSerializer
from rest_framework import status
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
