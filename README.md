# handy tutor client  
## 마이크 셋팅
http://jeongc팅hul.tistory.com/542
## 셋업
apt 최신버전으로
<pre>
sudo apt-get update
sudo apt-get upgrade
</pre>
파이썬 가상환경 설치
<pre>
pip install virtualenv
</pre>
현재 디렉토리에 가상환경 생성
<pre>
virtualenv env
</pre>
가상환경 실행
<pre>
source env/bin/activate
</pre>
예제코드에 필요한 모듈 셋업
<pre>
sudo apt install portaudio19-dev 
</pre>
<pre>
pip install pyaudio
</pre>
<pre>
pip install -r requirements.txt
</pre>
<pre>
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
</pre>
## 실시간 스트리밍 예제 실행
<pre>
python transcribe_streaming_mic.py
</pre>
