import streamlit as st
import yt_dlp, os

st.title("🎵 YouTube Audio Downloader & Player (MP3)")

# Input URL
url = st.text_input("Enter YouTube URL:")

if url:
    st.info("⏳ Downloading audio... Please wait.")

    try:
        # Create downloads folder if it doesn't exist
        save_folder = "downloads"
        os.makedirs(save_folder, exist_ok=True)

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best",
            "outtmpl": f"{save_folder}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"

        st.success(f"✅ Audio Downloaded! Saved in {file_path}")
        st.audio(file_path)  # Play MP3 directly

    except Exception as e:
        st.error(f"❌ Download failed: {e}")
