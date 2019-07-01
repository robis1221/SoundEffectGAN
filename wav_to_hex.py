import sys, os
import wave
import binascii

##SAVING THE DATA CHUNK OF THE WAV FILE
try:
    dir =  os.listdir(sys.argv[1])
except:
    print("Incorrect folder path")
origin = os.getcwd()
os.mkdir(origin+"/"+sys.argv[1]+"_hex")
#opens a wav file using the wave library
for i, path in enumerate(dir,start=1):
    print("Converting file: "+path+", "+str(i)+"/"+str(len(dir)))
    os.chdir(origin + "/" + sys.argv[1])
    f = wave.open(path, 'rb')
    os.chdir(origin+"/"+sys.argv[1]+"_hex")
    try:

        ## WAS USED FOR TEST PURPOSES
        # print(f.getparams())
        # channels = f.getnchannels()
        # sample_width = f.getsampwidth()
        # frame_rate = f.getframerate()
        # n_frames = f.getnframes()
        # compression_type = f.getcomptype()
        # compression_name = f.getcompname()

        # opens the output file, writes the data chunk from the wav file
        file = open(path[:-4] + '.txt', 'wb')
        data = f.readframes(f.getnframes())
        file.write(binascii.hexlify(data))
        f.close()
        file.close()

    except Exception as e:
        print(e)
        sys.exit(0)



