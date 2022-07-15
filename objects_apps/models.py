from django.db import models
from core.models import TimeStampedModel
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'streamplatforms'

class WatchList(TimeStampedModel):

    #serializer에서 왼쪽값으로 받는지 테스트함.. 유효성 검사가 진행된다는 뜻
    #물론 db에는 그냥 들어갈 수 있음. Null=False, Blank=True 정도의 느낌?
    watchlist_type = [
        ('Mv','Movie'),
        ('TvS','Tv SHOW')
    ]
    
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=15,choices=watchlist_type)
    img_url = models.CharField(max_length=100,null=True)
    platform = models.ForeignKey('StreamPlatform',on_delete=models.CASCADE,related_name='watchlists')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'watchlists'

class Review(TimeStampedModel):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey('WatchList',on_delete = models.CASCADE,related_name='reviews')
    
    def __str__(self):
        return f"{str(self.review_user.username)}'s review about{str(self.watchlist.name)}"

    class Meta:
        db_table = 'reviews'