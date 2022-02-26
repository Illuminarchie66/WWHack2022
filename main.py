# This is a sample Python script.
import base64
import time

import pyaudio
import websockets
import json
import asyncio
import wave
import requests
import json
# import configure
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
# CHUNK = 1024
RATE = 16000
DURATION = 5

auth_key = "1fb21cd48fdd4de79c3e7f9e454afb0c"
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.s

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def getSnippet(stream, p):
    frames = []
    filename = 'snippet.wav'

    for i in range(0, int(RATE/FRAMES_PER_BUFFER * DURATION)):
        frames.append(stream.read(FRAMES_PER_BUFFER))
    stream.stop_stream()

    file = wave.open(filename, 'wb')
    file.setnchannels(CHANNELS)
    file.setsampwidth(p.get_sample_size(FORMAT))
    file.setframerate(FRAMES_PER_BUFFER)

    file.writeframes(b''.join(frames))
    return file

def transcribeFile(filename):
    # endpoint = "https://api.assemblyai.com/v2/transcript"
    #filename = 'Recording_3.mp4'
    file = open(filename, 'rb')
    data = file.read(10000000)

    headers = {'authorization': "1fb21cd48fdd4de79c3e7f9e454afb0c"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=data
                             )
    print(response.json())
    # info = json.loads(response)
    url = response.json()['upload_url']
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json1 = {
        "audio_url": url
    }
    headers = {
        "authorization": auth_key,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json1, headers=headers)

    json_object = json.dumps(response.json(), indent=4)
    with open("sample1.json", "w") as outfile:
        outfile.write(json_object)

    print(response.json())
    transcript = ''
    time.sleep(2)
    headers = {
        "authorization": auth_key,
    }
    c = 0
    endpoint = endpoint + "/" + response.json()['id']
    while True:
        time.sleep(1)
        response = requests.get(endpoint, headers=headers)
        #response = requests.post(endpoint, json=json1, headers=headers)
        json_object = json.dumps(response.json(), indent = 4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        print(response.json())
        if(response.json()['status'] == 'completed'):
            transcript = transcript+response.json()['text']
            break;
        else:
            c = c+1

    print(transcript)
    # json = {
    # "audio_url": "https://bit.ly/3yxKEIY"
    # }

def beginStream():
    p = pyaudio.PyAudio()

    # starts recording
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER,
    )

    return stream, p


    #stream,p = beginStream()
    # streamToAPI(stream)
#    transcribeFile()