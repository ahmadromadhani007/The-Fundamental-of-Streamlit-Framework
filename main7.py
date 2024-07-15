import streamlit as st
import os

# Image
from PIL import Image
image = Image.open('dpmMe.jpg')
st.image(image, caption='Ahmad Romadhani, B.I.E')

# Audio|Vidio
# Define the base path
base_path = 'F:/datamining/app'

# Define the file paths
audio_file = os.path.join(base_path, 'firza.mp3')
video_file = os.path.join(base_path, 'firza.mp4')

# Check if the audio file exists and play it
if os.path.exists(audio_file):
    st.audio(audio_file)
else:
    st.error(f"Audio file not found: {audio_file}")

# Check if the video file exists and play it
if os.path.exists(video_file):
    st.video(video_file)
else:
    st.error(f"Video file not found: {video_file}")