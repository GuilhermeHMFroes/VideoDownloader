from django.shortcuts import render
from django.views.generic import TemplateView

from .download import downloader

# Create your views here.
class IndexView(TemplateView):
    def get(self, request):
        """ View Index.
            Exibe o arquivo localizado em `/config/templates/index.html`
        """

        context = {
            'download_options': ['mp3_128k', 'mp4'],
        }

        return render(request, 'index.html', context)
    
    def post(self, request):
        # Se o formulário foi enviado, chame a função de download e retorne a saída para o template
        video_url = request.POST.get('video_url')
        formato = request.POST.get('formato')
        
        content_type = ''
        if formato == 'mp4':
            content_type = 'video/mp4'
        elif formato == 'mp3':
            content_type == 'audio/mpeg'
        
        return downloader(video_url, formato, content_type)


class VideoView(TemplateView):
    def put(self, request):
        """
            TODO: Download video from YouTube
            ### Body: 
            - `file_url`: file url
            - `file_type`: file type. Choices supported are: `mp3_128k` and `mp4`
            
            ### Limitations: 
            - Only download video from YouTube.
        """

        # get file_type and file_url from Body

        # TODO: Register in database the info about the file that was downloaded

        return 'OK'

    def get(self, request):
        """
            TODO: Search for a video on youtube
            ### Parameters:
            - search_term: string
        """     

        # get search_term parameter from url

        # return the all results of the search.
        results = {
            1: {
                'thumbnail': '',
                'title': '',
                'description':'',
                'views':'',
                'duration':'',
                'url':'',
            },
            2:{},
            # ...
        }
        return results


class UserView(TemplateView):
    def get(self, request):
        """
            TODO: Get user info and downloads do usuário que está logado.
            
            ### Parameters:
            - user_id: int
        """

        context = {}

        return render(request, 'meus-downloads.html', context)