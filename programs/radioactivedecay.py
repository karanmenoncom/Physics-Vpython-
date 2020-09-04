from vpython import *
from vpython import graph
import random
from pydub import AudioSegment
from pydub.playback import play
wavfile='geiger.wav'
sound=AudioSegment.from_file(wavfile)

lambda1 = 0.005
max = 100; time_max = 500; seed = 68111
number = nloop = max 
graph1 = graph(title='Spontaneous Decay', xtitle= 'Time', ytitle = 'Number')
decayfunc = gcurve(color=color.green)
for time in arange(0,time_max + 1):
    
    for atom in arange (1 , number + 1):
        
        decay = random.random ( )
        if( decay < lambda1 ) :
            
            nloop = nloop - 1
            play(sound)

    number = nloop
    decayfunc.plot(pos= (time,number) )
    rate (30)
