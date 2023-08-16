from django.shortcuts import render

# Create your views here.
def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """

    context = {
        'download_options': ['mp3_128k', 'mp4'],
    }

    return render(request, 'index.html', context)


def videoDownloader(request):
    """
        ### Body: 
        - `file_url`: file url
        - `file_type`: file type. Choices supported are: `mp3_128k` and `mp4`
        
        ### Limitations: 
        - Only download video from YouTube.
    """
    if request.method == 'POST':
        # get file_type and file_url from Body

        # TODO: Register in database the info about the file that was downloaded

        pass

def videoSearcher(request):
    """
        ### Parameters:
        - search_term: string
    """

    # TODO: Search for a video on youtube

    if request.method == 'GET':
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
