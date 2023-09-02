from django.shortcuts import render
from django.views.generic import TemplateView

from .models import DownloadedVideos
from .download import downloader
from .search import search_videos

from pytube import YouTube

import asyncio

# Create your views here.
class IndexView(TemplateView):
    async def get(self, request):
        """ View Index.
            Exibe o arquivo localizado em `/config/templates/index.html`

            TODO: Search for a video on youtube
            ### Parameters:
            - search_term: string
        """

        context = {
            'download_options': ['mp3_128k', 'mp4'],
        }

        if request.GET.get('search_term') is not None:
            context = {
                'results': search_videos(request.GET.get('search_term')),
            }

            return render(request, 'resultado-da-busca.html', context)

        return render(request, 'index.html', context)
    
    async def post(self, request):
        # Se o formulário foi enviado, chame a função de download e retorne a saída para o template
        video_url = request.POST.get('video_url')
        formato = request.POST.get('formato')

        # youtube_video = YouTube(video_url)
        # DownloadedVideos.objects.create(
        #     thumbnail = youtube_video.thumbnail_url,
        #     title = youtube_video.title,
        #     author = youtube_video.author,
        #     description = youtube_video.description,
        #     views = youtube_video.views,
        #     duration = youtube_video.length,
        #     url = video_url,
        #     formato = formato,
        # )
        
        response = await asyncio.to_thread(downloader, video_url, formato)
        return response
    
    async def put(self, request):
        search_query = request.PUT.get('search_query')
        results = search_videos(search_query)


class VideoView(TemplateView):
    def get(self, request):
        pass


class UserView(TemplateView):
    def get(self, request):
        """
            TODO: Get user info and downloads do usuário que está logado.
            
            ### Parameters:
            - user_id: int
        """
        downloaded_videos = DownloadedVideos.objects.all()

        context = {
            'downloaded_videos': downloaded_videos,
            'total_videos_downloaded': downloaded_videos.__len__,
        }

        return render(request, 'meus-downloads.html', context)