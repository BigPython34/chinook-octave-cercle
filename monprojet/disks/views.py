from django.shortcuts import render, get_object_or_404
from .models import Album



def album_list(request):
    query = request.GET.get('q', '')  
    if query:
        albums = Album.objects.filter(title__icontains=query)  
    else:
        albums = Album.objects.all()  
        
    return render(request, 'disks/album_list.html', {'albums': albums, 'query': query})
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)  
    tracks = album.tracks.all()  
    return render(request, 'disks/album_detail.html', {'album': album, 'tracks': tracks})


