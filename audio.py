import pyaudio
import numpy as np
 
CHUNK = 2**10 #음성데이터를 불러올 때 한번에 몇개의 정수를 불러올 지 (현재 1024개)
RATE = 44100 #음성데이터의 샘플링 레이트, 일반적인 44100
 
#

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
#음성 데이터 스트림을 여는 코드 
#format : 비트의 깊이. paInt16이므로 16비트 
#channels : 
#rate : 샘플링 레이트 
#input : 입력스트림이니 True
#frame_per_buffer : 청크 
#input_device_index : 원하는 장치의 입력번호, 현재 장치에서 나의 입력 채널 번호, 입력안하면 알아서 해줌
#default : input_device_index=3 
while(True):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(int(np.average(np.abs(data))))
 
stream.stop_stream()
stream.close()
p.terminate()
