from services.sonos import Sonos

class Music:
	
	async def handle(request):
	    name = request.match_info.get('name', "Anonymous")
	    text = "Hello, " + name
	    return web.Response(text=text)
		
