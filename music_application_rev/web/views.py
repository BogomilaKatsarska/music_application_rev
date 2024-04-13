from django.shortcuts import render, redirect
from music_application_rev.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from music_application_rev.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'albums/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumEditForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/edit-album.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }
    return render(request, 'core/home-no-profile.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumDeleteForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/delete-album.html', context)


def details_profile(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)
