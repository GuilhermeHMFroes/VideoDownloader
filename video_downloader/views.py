from django.shortcuts import render
from .download import downloader

# Create your views here.
def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """

    if request.method == 'POST':
        # Se o formulário foi enviado, chame a função de download e retorne a saída para o template
        return downloader(request)

    return render(request, 'index.html')

def meus_downloads(request):

    context = {}

    return render(request, 'meus-downloads.html', context)
