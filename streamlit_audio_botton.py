#pip install gtts
#pip install  iPython
import streamlit as st
import pandas as pd
import numpy as np


#------------------ import audio 
from gtts import gTTS
from IPython.display import Audio
# --- App Title and Description ---
st.title("Audio Application in Streamlit") 
st.write("This is a simple app to demonstrate the audio play")
#-------------------
text_to_speech=gTTS('hello world this is Dsata science class',lang='hi')

text_to_speech.save('text_to_speech_gTTs.wav')
#sound_file='text_to_speech_gTTs.wav'

#Audio(sound_file,autoplay=False)

audio_file = open('text_to_speech_gTTs.wav', "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/wav')

st.header('enter the text to convert to speech')
