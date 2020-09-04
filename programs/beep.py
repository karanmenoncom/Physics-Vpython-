from pydub  import AudioSegment
from pydub.playback import play

wavfile='geiger.wav'
sound= AudioSegment.from_file(wavfile)
play(sound)
