
import streamlit as st
import yt_dlp, os 

st.subheader("🎵 ▶️YouTube🔴 Audio Downloader & Player (MP3)")

url = st.text_input("Enter youtube url : ")

if url:
    st.info("⏳ Downloading audio... Please wait.")

    try:
        save_audio = "download"
        os.makedirs(save_audio,exist_ok=True)

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best",
            "outtmpl": f"{save_audio}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download = True)
            file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"

            st.success(f"✅ Audio Downloaded! Saved in {file_path}")

            st.audio(file_path)


    except Exception as e:
        st.error("Download Failed!")