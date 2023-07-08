from app.models import * 
from rest_framework import serializers


class Organizationserializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        #fields = ['Company', 'Image', 'Discription']
        fields='__all__'
        # widgets = {
        #     'description':forms.TextInput(attrs = {'class':'form-control'}),
        # }
