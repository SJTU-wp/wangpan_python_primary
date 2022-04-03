from django.db import models

# Create your models here.


class Comment(models.Model):

    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


# 酒店预定，入住日期，离开日期
class Event(models.Model):
    description = models.CharField(max_length=100)
    start = models.DateTimeField()
    finish = models.DateTimeField()


# 酒店预定，姓名，房间号，日期
class Event1(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    date = models.DateField()


class Account(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        'auth.User',
        related_name='accounts',
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False)


# 唱片和歌曲的模型类
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Track(models.Model):
    # related_name是不需要再去写track_set这个操作，为了序列化，必须写related_name
    album = models.ForeignKey(
        Album,
        related_name='tracks',
        on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
