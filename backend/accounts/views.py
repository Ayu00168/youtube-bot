from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserLoginSerializer, ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginUserView(APIView):
    authentication_classes = []
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.save()
            
            data = {
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'name': user.name,
                    'phone': user.phone,
                    'role': user.role
                }
            }
            
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LogoutUserView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": 'Successfully logged out'}, status=status.HTTP_204_NO_CONTENT)
    
    
class ChangePasswordView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            if user.check_password(serializer.validated_data['old_password']):
                if serializer.validated_data['old_password'] == serializer.validated_data['new_password']:
                    return Response({"error": "New password cannot be the same as old password"}, status=status.HTTP_400_BAD_REQUEST)
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)