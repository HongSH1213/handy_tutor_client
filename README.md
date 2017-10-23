# handy tutor client  
## API KEY 발급
http://www.makewith.co/page/project/1088/story/2749/
## 셋업
apt 최신버전으로
<pre>
sudo apt-get update
sudo apt-get upgrade
</pre>
<pre>
sudo apt install portaudio19-dev 
</pre>
<pre>
sudo apt-get install python-dbus
</pre>
파이썬 가상환경 설치
<pre>
pip install virtualenv
</pre>
현재 디렉토리에 가상환경 생성
<pre>
virtualenv -p python3 --system-site-packages env
</pre>
가상환경 실행
<pre>
source env/bin/activate
</pre>
예제코드에 필요한 모듈 셋업
<pre>
pip install pyaudio
</pre>
<pre>
pip install omxplayer-wrapper
</pre>
<pre>
pip install -r requirements.txt
</pre>
<pre>
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
// 환경변수를 영구적으로 쓰려면 vi /env/bin/activate 마지막 줄에 위 문장 추가
</pre>
## 실시간 스트리밍 예제 실행
<pre>
python transcribe_streaming_mic.py
</pre>
## OMXPLAYER 제어
예제
<pre>
python omx.py
</pre>
http://python-omxplayer-wrapper.readthedocs.io/en/latest/
