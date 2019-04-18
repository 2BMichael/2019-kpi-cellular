from os import path
from pydub import AudioSegment
from pydub.playback import play

                                                            
src = ("B:\\gitushka\\2019-kpi-cellular\\Treasure.mp3")
dst = "task2.wav"
                                                           
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

