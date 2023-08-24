"""

Downloader
Parametros para Download: file_url e file_type ('mp4', 'mp3_128k')
>> Retorna link para download do arquivo.

"""

"""
# Importando a função 'render' do módulo 'django.shortcuts' para renderizar templates.
from django.shortcuts import render

# Importando a classe 'HttpResponse' do módulo 'django.http' para criar respostas HTTP personalizadas.
from django.http import HttpResponse

# Importando o módulo 'os' para lidar com operações do sistema de arquivos.
import os


# Definindo a função 'downloader' que será chamada quando a rota correspondente for acessada.
def downloader(request):
    # Construindo o caminho completo para o arquivo 'download.txt' usando o diretório do arquivo atual.
    document_path = os.path.join(os.path.dirname(__file__), 'download.txt')

    # Verificando se o arquivo 'download.txt' existe no caminho especificado.
    if not os.path.exists(document_path):
        # Se o arquivo não existe, retornando uma resposta de erro com status 404.
        return HttpResponse("Arquivo não encontrado.", status=404)

    # Abrindo o arquivo 'download.txt' em modo de leitura binária ('rb').
    with open(document_path, 'rb') as document_file:
        # Lendo o conteúdo do arquivo e criando uma resposta HTTP com o conteúdo.
        response = HttpResponse(document_file.read(), content_type='application/txt')

        # Definindo o cabeçalho 'Content-Disposition' para forçar o download do arquivo.
        response['Content-Disposition'] = 'attachment; filename="download.txt"'

        # Retornando a resposta HTTP com o conteúdo do arquivo para download.
        return response

    # Se o bloco 'with' não for executado (ocorreu um erro), a função retornará um template 'download.html'.
    #return render(request, 'download.html')
"""

from django.http import FileResponse
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