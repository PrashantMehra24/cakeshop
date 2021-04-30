from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import *
from .serializers import cakeSerializer,userSerializer,cartSerializer,orderSerializer

class cakeView(viewsets.ModelViewSet):
    queryset=cake.objects.all()
    serializer_class = cakeSerializer

class userView(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class = userSerializer

class cartView(viewsets.ModelViewSet):
    queryset=cart.objects.all()
    serializer_class = cartSerializer

class orderView(viewsets.ModelViewSet):
    queryset=order.objects.all()
    serializer_class = orderSerializer

class searchcakes(APIView):
    def get(self,request,cakes):
        if request.method == 'GET':
            queryset = cake.objects.all().filter(name__icontains=cakes)
            serializer = cakeSerializer(queryset,context={'request':request},many=True)
            return Response({"data":serializer.data},status=status.HTTP_201_CREATED)

class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id,
            'email': user.email,
            'username':user.username
        })

