from rest_framework import serializers
from .models import cake,user,cart,order


class cakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=cake
        fields=('id','name','price','flavour','eggless','weight','image','category','description')

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields = ('id','username','email','password')

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields = '__all__'