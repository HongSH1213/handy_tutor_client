# handy tutor client  
## mic setting
http://jeongchul.tistory.com/542
## Set up
<pre>
pip install virtualenv
virtualenv env
source env/bin/activate
sudo apt install portaudio19-dev 
pip install pyaudio
pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
</pre>
## starting
<pre>
python transcribe_streaming_mic.py
</pre>
