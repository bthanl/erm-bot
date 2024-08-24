import requests
from cogs.libs.asyncRun import asyncRun
from cogs.libs.YTDL import YTDLSource
import discord

cobalt_url = 'https://api.cobalt.tools/api/json'

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
}

async def getYT(url):

	json = {
		'url': url,
		'isAudioOnly': True,
	}

	#first request
	response = requests.post(cobalt_url, headers = headers, json = json)

	response.raise_for_status() # raises exception when not a 2xx response

	if response.status_code == 204: # if not successful
		print("failed: " + response.status_code)
		return

	response = response.json()
	new_url = response.get('url') # get stream url
	mp3 = requests.get(new_url, headers = headers) # get mp3

	_id = url[-11:]
	ext = "mp3"
	path = 'temp/' + _id + "." + ext

	# create and write to temp file
	with open(path, 'wb') as file:
		file.write(mp3.content)

	# create "fake" data for YTDLSource object
	data = dict()
	data["title"] = await getData(path, 2)
	data["artist"] = await getData(path, 1)
	data["description"] = None
	data["duration"] = await getDuration(path)
	data["id"] = _id
	data["ext"] = ext

	#turn into YTDLSource obj with data
	return YTDLSource(discord.FFmpegPCMAudio(path), data = data)

async def getData(path, sel):
	output = await asyncRun("ffmpeg -v error -i " + path + " -f ffmetadata -")

	#;FFMETADATA1
	#artist=Ado
	#title=[Ado]Value
	#encoder=Lavf60.3.100
	
	x = output.split("\n")
	x = x[sel].split("=")
	return x[1]

async def getDuration(path):
	output = await asyncRun("ffmpeg -v error -stats -i " + path + " -f null -")
	#size=N/A time=00:03:12.19 bitrate=N/A speed= 808x    A

	x = output.split("\r")
	x = x[1].split("=")
	x = x[2].split(" ")
	x = x[0].split(":")
	      #h               m                s
	res = int(x[0]) * 60 + int(x[1]) * 60 + int(round(float(x[2])))
	return res