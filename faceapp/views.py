from django.core.exceptions import ViewDoesNotExist
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404, render
from .models import Video
from datetime import datetime
from django.conf import settings
import time


def index(request):
    videos = Video.objects.filter(user_id='sajjan')
    return render(request,'index.html',{'videos': videos})

def get_videos(request,user_id):
    videos = Video.objects.filter(user_id='sajjan')
    return render(request,'index.html',{'videos': videos})

def save_video(request):
    user_id = request.POST['user_id']
    path = settings.STATIC_URL+"/"+user_id+str(time.time())+".webm"
    video = Video(user_id=user_id,pub_date=datetime.today().strftime('%Y-%m-%d'),video_path=path)
    video.save()
    print(request.FILES)
    uploaded_file = request.FILES['video_file']
    with open(path,'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)
    videos = Video.objects.filter(user_id=user_id)
    return render(request,'index.html',{'videos': videos})

def delete_video(request):
    videos = Video.objects.filter(user_id="sajjan")
    videos.delete()
    videos = Video.objects.filter(user_id='sajjan')
    return render(request,'index.html',{'videos': videos})