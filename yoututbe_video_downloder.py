
import streamlit as st 
import yt_dlp
import os 

st.title("📥 YouTube Video Downloader")

url = st.text_input("Enter youtube url : ")

quality = st.selectbox("Select quality : ", 
        ["Best", "720p", "480p", "360p"]
)

if st.button("Download", type="primary"):
    st.info("⏳ Downloading... Please wait")

    try:
        os.makedirs("my_videos",exist_ok=True)


        quality_map = {
                "Best": "bestvideo+bestaudio/best",
                "720p": "bestvideo[height<=720]+bestaudio/best",
                "480p": "bestvideo[height<=480]+bestaudio/best",
                "360p": "bestvideo[height<=360]+bestaudio/best",
            }
        
        ydl_opts = {
                "format": quality_map[quality],
                "merge_output_format": "mp4",
                "outtmpl": "downloads/%(title)s.%(ext)s",
                "quiet": True,
                "no_warnings": True,
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download = True)
            filename = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp4"

            st.success("✅ Download complete!")

            st.video(filename)

    except Exception as e:
        st.error("Something Went Wrong...")