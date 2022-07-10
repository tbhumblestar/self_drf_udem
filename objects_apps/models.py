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
    
class WatchList(models.Model):
    #앞에께 실제로 DB에 들어가는 데이터
    #뒤에께 인간이 잘 인식할 수 있게 한 것
    #여기 적힌거 외에 다른 값은 들어올 수 없다? 체크 필요
    watchlist_type = [
        ('Mv','Movie'),
        ('TvS','Tv SHOW')
    ]
    
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=15,choices=watchlist_type)
    platform = models.ForeignKey('StreamPlatform',on_delete=models.CASCADE,related_name='watchlists')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.title)


class Review(TimeStampedModel):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey('WatchList',on_delete = models.CASCADE,related_name='reviews')
    
    def __str__(self):
        return f"{str(self.review_user.name)}'s review on{str(self.watchlist.title)}"