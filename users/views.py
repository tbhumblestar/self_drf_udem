from rest_framework                   import status
from rest_framework.decorators        import api_view
from rest_framework.response          import Response
from rest_framework_simplejwt.tokens  import RefreshToken

from users.serializers import RegistrationSerializer

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    
    if serializer.is_valid():
        account = serializer.save()
        data['username'] = account.username
        data['password'] = account.email
        data['message']  = "success!"
        
        #jwt
        refresh = RefreshToken.for_user(account)
        data['jwt'] = {
            'refresh' : str(refresh),
            'access'  : str(refresh.access_token),
        }
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data = serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
#logout은 필요없음(jwt삭제)