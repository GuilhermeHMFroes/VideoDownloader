from django.shortcuts import render

# Create your views here.
def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """
    # abre o arquivo `README.md` e le o conteudo do readme
    # with open(os.path.join(BASE_DIR, 'README.md'), 'r', encoding='UTF-8') as readme_file:
    #     readme_content = readme_file.read()

    # converte o conteudo em markdown para html
    # index_content = markdown(readme_content)

    # context = {
    #     'index_content': index_content,
    # }
    context = {}

    return render(request, 'index.html', context)

def meus_downloads(request):

    context = {}

    return render(request, 'meus-downloads.html', context)