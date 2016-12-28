from services.sonos import Sonos
from aiohttp import web
import json


class Music:
    
    async def command(request):
        command = request.match_info.get('command')
        sonos = Sonos()

        if command == "play":
            sonos.play()
        elif command == "pause":
            sonos.pause()
        elif command == "next":
            sonos.next()
        
        current_track = sonos.getCurrentTrack()
        
        response= {
            "title": current_track['title'],
            "artist": current_track['artist'],
            "command": command
        }
        
        return web.Response(text=json.dumps(response))