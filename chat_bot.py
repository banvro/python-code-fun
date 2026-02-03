import streamlit as st
import yt_dlp
import os
import json
import time

st.set_page_config(page_title="Video Chatbot", layout="wide")

st.title("🤖 Video Chatbot")
st.caption("Paste a video URL — I’ll show or play it 🎬🎵")

DOWNLOAD_DIR = "chat_downloads"
HISTORY_FILE = "chat_history.json"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ---------- Load chat history ----------
if "messages" not in st.session_state:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            st.session_state.messages = json.load(f)
    else:
        st.session_state.messages = []

# ---------- Save history ----------
def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(st.session_state.messages, f)

# ---------- Typing animation ----------
def typing_animation(text="Bot is thinking"):
    placeholder = st.empty()
    for i in range(3):
        placeholder.markdown(f"💬 **{text}{'.' * (i + 1)}**")
        time.sleep(0.5)
    placeholder.empty()

# ---------- Helpers ----------
def is_direct_video(url):
    return url.lower().endswith((".mp4", ".webm", ".mov"))

def detect_platform(url):
    if "youtube" in url or "youtu.be" in url:
        return "YouTube 🎥"
    if "instagram" in url:
        return "Instagram 📸"
    return "Direct Video 🎞"

def download_video(url, audio_only=False):
    if audio_only:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
        }
    else:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "quiet": True,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        if audio_only:
            file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
        else:
            file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp4"

    return file_path

# ---------- Sidebar ----------
st.sidebar.header("⚙️ Options")
mode = st.sidebar.radio("Download Mode", ["🎬 Video", "🎵 Audio only"])

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    save_history()
    st.rerun()

# ---------- Display chat ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        col1, col2, col3 = st.columns(3)
        with col1:
            if msg.get("video"):
                st.video(msg["video"])
            if msg.get("audio"):
                st.audio(msg["audio"])

# ---------- Chat input ----------
user_input = st.chat_input("Paste a video URL")

if user_input:
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    save_history()

    with st.chat_message("assistant"):
        typing_animation()

        try:
            platform = detect_platform(user_input)
            st.markdown(f"**Detected:** {platform}")

            audio_only = mode == "🎵 Audio only"

            if is_direct_video(user_input) and not audio_only:
                st.video(user_input)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Here’s your video 🎬",
                    "video": user_input
                })

            else:
                file_path = download_video(user_input, audio_only)

                if audio_only:
                    st.audio(file_path)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Here’s your audio 🎵",
                        "audio": file_path
                    })
                else:
                    st.video(file_path)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Here’s your video 🎬",
                        "video": file_path
                    })

            save_history()

        except Exception as e:
            st.error("❌ Failed to process URL")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error: {e}"
            })
            save_history()
