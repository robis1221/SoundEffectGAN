import sys
import wave

##READING THE DATA CHUNK AND COMPILING IT INTO A WAV

#opens the file containing the data chunk
f = open(sys.argv[1][:-4] + '.txt', 'rb')

##used for test purposes, swaps first half of the wav file with the second file
data=bytearray(f.read())
tmp_data=data[:int(len(data)/2)]
data[:int(len(data)/2)]=data[int(len(data)/2):]
data[int(len(data)/2):]=tmp_data

##compile a wav file
try:
    file = wave.open(sys.argv[1][:-4] + '2.wav', 'wb')
    file.setparams([2, 2, 44100, 10, 'NONE', 'not compressed'])
    file.writeframes(bytes(data))
    f.close()
    file.close()
except Exception as e:
    print(e)
    sys.exit(0)