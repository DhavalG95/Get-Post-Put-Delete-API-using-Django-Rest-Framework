from rest_framework import serializers
from .models import *



class ClientData(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ProjectData(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"