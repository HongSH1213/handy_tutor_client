
# coding: utf-8

import os
import sys
import urllib.request

client_id = "ID"
client_secret = "SECRET"

url = "https://openapi.naver.com/v1/voice/tts.bin"

speakers = ['mijin', 'jinho', 'clara', 'matt'] 
# 한국어 여성, 한국어 남성, 영어 여성, 영어 남성
# speed는 -5~5 사용 -5는 0.5 빠르게 5는 0.5 느리게


mp3Path = './tmp.mp3'

class NaverTTS():
    def __init__(self, speaker=0, speed=0):
        self.speaker= speakers[speaker]
        self.speed = str(speed)    
    def play(self, txt):
        encText = urllib.parse.quote(txt)
        data = 'speaker=' + self.speaker + "&speed=" + self.speed + "&text=" + encText
        
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            with open(tmpPlayPath, 'wb') as f:
                f.write(response_body)
            
            #mp3 플레이어 설정
            
            #외부 프로그램 사용 vlc
            #os.system('cvlc ' + tmpPlayPath + ' --play-and-exit')
            #라즈베리파이
            #os.system('omxplayer ' + tmpPlayPath)
        else:
            print("Error Code:" + rescode)

def main():
    tts = NaverTTS()
    tts.play("안녕하십니까?")

if __name__ == '__main__':
    main()

