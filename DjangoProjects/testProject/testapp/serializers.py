from .models import User,Todo

from rest_framework import serializers


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name","date_of_birth"]
        # fields = "__all__"


class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name","description","user","priority"]
