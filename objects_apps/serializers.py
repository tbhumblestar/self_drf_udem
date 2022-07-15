from rest_framework import serializers
from objects_apps.models import StreamPlatform,WatchList,Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('review_user','watchlist')

class WatchListSerializer(serializers.ModelSerializer):

    #얘를 쓰면, 해당 serializer를 쓰는 뷰는 write가 불가능하다. 값을 넣어줄 수가 없기 때문..
    #url_kwarg로 foreignkey를 받는다든가 하는 방법이 있을 수도 있음
    # platform = serializers.StringRelatedField()    
    
    #다음과 같이 이름이 원래 모델명의 foreignkey로 되어있으면, write할때 platform_id의 값을 줄 수가 없음
    # platform = serializers.CharField(source='platform.name',read_only=True)
    # platform_website = serializers.CharField(source='platform.website',read_only=True)
    
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    #model에서 related_to로 설정해준 이름과 동일해야 함
    #many=True 반드시 필요, read_only안해주면 쓰기 과정 watchlist의 내용도 채워줘야 함
    watchlists = WatchListSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'


        
