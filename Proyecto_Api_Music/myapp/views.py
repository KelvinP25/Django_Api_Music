from django.shortcuts import render
from django.views import View
from .models import Vitrola, WaitList
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os
import random
import asyncio
# Create your views here.


class VictrolaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            music = list(Vitrola.objects.filter(pk=id).values())
            if len(music) > 0:
                musi = music[0]
                data = {'message': "Success", 'musi': musi}
            else:
                data = {'message': "Music not found.."}
            return JsonResponse(data)
        else:
            music = list(Vitrola.objects.values())
            if len(music) > 0:
                data = {'message': "Success", 'music': music}
            else:
                data = {'message': "Music not found.."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Vitrola.objects.create(
            artist=jd['artist'], titulo=jd['titulo'], track=jd['track'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        music = list(Vitrola.objects.filter(pk=id).values())
        if len(music) > 0:
            musi = Vitrola.objects.get(id=id)
            musi.artist = jd['artist']
            musi.titulo = jd['titulo']
            musi.track = jd['track']
            musi.save()
            data = {'message': "Success"}
        else:
            data = {'message': 'Music not found..'}
        return JsonResponse(data)

    def delete(self, request, id=0):
        music = list(Vitrola.objects.filter(pk=id).values())
        if len(music) > 0:
            music = Vitrola.objects.get(pk=id)
            music.delete()
            data = {'message': "Success"}
        else:
            data = {'message': 'Music not found..'}
        return JsonResponse(data)


class WaitListView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
            music = list(WaitList.objects.values())
            if len(music) > 0:
                data = {'message': "Success", 'music': music}
                return JsonResponse(data)
            else:
                data = {'message': "Music not found.."}
                return JsonResponse(data)

    def delete(self, request, id=0):
        music = list(WaitList.objects.filter(pk=id).values())
        if len(music) > 0:
            musi = WaitList.objects.get(pk=id)
            musi.delete()
            data = {'message': "Success"}
        else:
            data = {'message': 'Music not found..'}
        return JsonResponse(data)
    
    def post(self, request):
        jd = json.loads(request.body)
        WaitList.objects.create(
            artist=jd['artist'], titulo=jd['titulo'], track=jd['track'])
        data = {'message': "Success"}
        return JsonResponse(data)


'''
async def play_songs(self):
    song = list(WaitList.objects.values())
    songall = list(Vitrola.objects.values())
    if len(song) > 0:
        song_paths = [index['track'] for index in song]
        loop = asyncio.get_event_loop()
        for song in song_paths:
            await loop.run_in_executor(None, self.play_song, song.file_path.path)
            os.remove(song.file_path.path)
        return JsonResponse({'message': "All waiting lis music played"})
    else:
        song_paths = [index['track'] for index in songall]
        loop = asyncio.get_event_loop()
        song = random.choice(song_paths)
        await loop.run_in_executor(None, self.play_song, song.file_path.path)
'''


# import ipdb; ipdb.set_trace()
# song_paths = [index['track'] for index in music]
