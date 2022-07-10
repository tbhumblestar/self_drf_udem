from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={'input_type':'password'})
    #input_type : 확인 필요함.. 왜 쓰는지???
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'P1 and P2 should be same'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)#User모델에 있는 메서드. password를 암호화시켜줌
        account.save()
        
        return account        

        