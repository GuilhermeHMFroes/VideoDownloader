from django.http import HttpResponse
from pytube import YouTube
from io import BytesIO

def downloader(video_url, formato):
    try:
        youtube_video = YouTube(video_url)
        buffer = BytesIO()

        if formato == "mp4":
            video_stream = youtube_video.streams.get_highest_resolution()
            content_type = 'video/mp4'
            stream = video_stream

        elif formato == "mp3":
            audio_stream = youtube_video.streams.filter(only_audio=True).first()
            content_type = 'audio/mpeg'
            stream = audio_stream

        else:
            return HttpResponse("Formato não suportado")

        response = HttpResponse(content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{youtube_video.title}.{formato}"'

        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        response.write(buffer.read())

        return response
    except Exception as e:
        return HttpResponse("Erro ao baixar o vídeo: " + str(e))