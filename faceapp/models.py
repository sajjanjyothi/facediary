from django.db import models

# Create your models here.

class Video(models.Model):
    user_id = models.CharField('user id',max_length=20)
    pub_date = models.DateField('date of video')
    video_path = models.CharField('video file path', max_length=255, default="")
