#import IPython.display as ipd
from pydub import AudioSegment
input_audiofile="audio.ogg"
output_audiofile="audio.mp3"
loadaudio = AudioSegment.from_ogg(input_audiofile)
loadaudio.export(output_audiofile, format="mp3")
#ipd.display(ipd.Audio("sampleMp3.mp3", autoplay=False))
