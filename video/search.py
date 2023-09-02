from pytube import Search

def search_videos(query, max_results=10):
    s = Search(query)
    results = s.results[:max_results]
    videos = []

    for result in results:
        video_data = {
            "title": result.title,
            "author": result.author,
            "thumbnail_url": result.thumbnail_url,
            "description": result.description if result.description else "N/A",
            "video_url": result.watch_url 
        }
        videos.append(video_data)

    return videos

# if __name__ == "__main__":
#     search_query = input("Digite a palavra-chave para pesquisa: ")
#     search_results = search_videos(search_query)
    
#     for index, video in enumerate(search_results, start=1):
#         print(f"Resultado {index}:")
#         print(f"Título: {video['title']}")
#         print(f"Autor: {video['author']}")
#         print(f"URL da Thumbnail: {video['thumbnail_url']}")
#         print(f"Descrição: {video['description']}")
#         print(f"URL do Vídeo: {video['video_url']}")
#         print()