import streamlit as st
import yt_dlp
import os

st.title("📥 Instagram Video Downloader")

url = st.text_input("Enter Instagram Video URL:")

if st.button("Download", type="primary"):
    if not url:
        st.warning("⚠️ Please enter an Instagram URL")
    else:
        try:
            st.info("⏳ Downloading Instagram video...")

            os.makedirs("insta_downloads", exist_ok=True)

            ydl_opts = {
                "format": "best",
                "outtmpl": "insta_downloads/%(title)s.%(ext)s",
                "quiet": True,
                "no_warnings": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            st.success("✅ Download successful!")
            st.video(filename)
            st.info(f"📁 Saved as: {filename}")

        except Exception as e:
            st.error(f"❌ Download failed: {e}")
