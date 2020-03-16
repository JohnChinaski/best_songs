from rest_framework import views
import requests
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response


class Get_topTen(views.APIView):

    def get(self, request, *args, **kwargs):
        artist_id = self.kwargs.get("pk")

        if artist_id:
            url = "http://api.genius.com/artists/{}/songs".format(artist_id)
            header = {
                'Authorization': 'Bearer ' + '6quEo0Kb8tRsMnIP7slPhOPeW-a38A1ppw6GeHXn4os8HDyZZWCbipJlp4jojohl',
            }

            request = requests.get(url=url, headers=header)
            songs = json.loads(request.text).get("response").get("songs")
            artist = json.loads(request.text).get("response").get("songs")[0].get("primary_artist").get("name")
            song_list = []
            for song in songs:
                if song.get("title") not in song_list and len(song_list) < 10:
                    song_list.append(song.get("title"))

            top_ten = {artist: {}}

            count = 1
            for msc in song_list:
                top_ten.get(artist).update({
                    'song_{}'.format(count): msc
                })

                count += 1

            response = JsonResponse(
                top_ten
            )
            response.status_code = 200
            return response
