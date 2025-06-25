from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password': {'write_only':True}
        }

    def save(self):

        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'error':'Password must be same'})
        query=User.objects.filter(email=self.validated_data['email'])
        if query.exists():
            raise serializers.ValidationError({'error':'Email Already Exists'})
        
        account=User(username=self.validated_data['username'],email=self.validated_data['email'])
        account.set_password(self.validated_data['password'])
        account.save()

        return account
