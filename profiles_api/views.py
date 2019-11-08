from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProfileAPIView(APIView):
    '''testing api views'''
    def get(self, request, format=None):
        '''testing get method for api '''
        an_api=[
            'This is first time I am using api',
            'Another List Item',
            'One more added'
        ]
        return Response({'Hello':'Hello Api View','an_api':an_api})
