from google.colab import drive
drive.mount('/content/drive')

pip install pydub

from pydub import AudioSegment
import librosa
import pandas as pd

Stats:
*   bellypain = 80
*   burping = 40
*   discomfort = 135
*   hungry = 80
*   tired = 80

To bring uniformity, we will make all folders to have 80 audio files.
All audios are longer than 5 seconds and maximum lie between 5-7 seconds
Now, what to do is:
*   For all folders except burping: We will extract starting 2.5 seconds of audio files and store them in the new location 
*   For burping: As its number is only 40, so to make them 80, we will extract starting 2.5 seconds as well as next 2.5 seconds of audio and store these two created files in the new location. This will result in 80 files of burping.

We will also keep a check if files have not exceeded the count of 80 because discomfort has 135 files and we want only 80.

The following function performs the above mentioned tasks:
