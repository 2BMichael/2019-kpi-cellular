import matplotlib.pyplot as plt
from pydub import AudioSegment
import numpy as np
import wave

sour = AudioSegment.from_file("sams1.wma")
sour1 = sour.export("task21.mp3", format="mp3", bitrate="64k")
sour11 = AudioSegment.from_mp3("task21.mp3")
sour2 = sour11.export("task3.wav", format="wav")

inp = AudioSegment.from_file("task3.wav")
inp1 = AudioSegment.from_file("sams1.wma")
plt.figure(figsize=(12, 5))

plt.plot(inp[1000:1005].get_array_of_samples(), label='before bitrate')
plt.plot(inp1[1000:1005].get_array_of_samples(), label='after bitrate')
plt.xlabel('vremia')
plt.ylabel('volume')
plt.grid()
plt.legend()
plt.show()
