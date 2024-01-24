# from http import server
# from traceback import print_tb
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer , LoginSerializer
from rest_framework import status


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)

            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    'data' : {},
                    'message' : 'your account is created'
                }, status=status.HTTP_201_CREATED)
            else:
                return Reponse({
                    'data' : serializer.errors,
                    'message' : 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message': 'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)
        
# class LoginView(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data=data)

            # if serializer.is_valid():
            #     user = authenticate(username=request.data['username'], password=request.data['password'])
            #     if user:
            #         refresh = RefreshToken.for_user(user)

            #         return Response({
            #             'message': 'Login success',
            #             'data' : {
            #                 'token' : {
            #                     'refresh' : str(refresh),
            #                     'access' : str(refresh.access_token),
            #                 }
            #             }
            #         })
            #     else:
            #         return Response({
            #             'message' : 'Invalid credentials',
            #             'data' : {}
            #         }, status=status.HTTP_401_UNAUTHORIZED)
                

            # if not serializer.is_valid():
            #     return Response({
            #         'data' : serializer.errors,
            #         'message' : 'something went wrong'
            #     }, status = status.HTTP_400_BAD_REQUEST)
            
            # response = serializer.get_jwt_token(serializer.data)
            # return Response(response, status = status.HTTP_200_OK)

            # if serializer.is_Valid():
            #     response = serializer.get_jwt_token(serializer.validated_data)
            #     return Response(response, status=status.HTTP_200_OK)
            # else:
            #     return Response({
            #         'data' : serializer.errors,
            #         'message' : 'something went wrong'
            #     }, status=status_400_BAD_REQUEST)
        
class LoginView(APIView):
     def post(self,request):
          data=request.data
          serializer = LoginSerializer(data = data)
          serializer.is_valid(raise_exception=True)
          response = serializer.get_jwt_token(serializer.data)
          return Response(response, status=status.HTTP_200_OK)
