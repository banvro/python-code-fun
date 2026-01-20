# joke_baba_yellow_theme.py
# pip install pyjokes

import tkinter as tk
from tkinter import ttk
import pyjokes
import random

# Family friendly Hindi jokes (single paragraph)
hindi_jokes = [
    "पति: आज खाना बहुत स्वादिष्ट बना है! पत्नी: वाह! पहली बार तारीफ़! पति: अरे नहीं… मैं तो बस कल के खाने से compare कर रहा था 😂",
    "पप्पू: डॉक्टर साहब, मुझे लगता है मैं कुत्ता बन गया हूँ। डॉक्टर: कब से? पप्पू: पिल्ला था तब से ही! 🐶",
    "बीवी: तुम मुझसे कितना प्यार करते हो? पति: 4G जितना। बीवी: मतलब? पति: कभी full speed, कभी network नहीं मिलता 😭",
    "लड़की: मुझे लड़के में सबसे जरूरी चीज़ चाहिए। लड़का: क्या? लड़की: धैर्य… क्योंकि मैं बहुत लेट रिप्लाई देती हूँ 😌",
    "दोस्त: तेरी GF बहुत सुंदर है यार! दूसरा: हाँ, पर उसका भाई मुझसे 3 गुना सुंदर है 😱",
    "टीचर: होमवर्क किसने किया? छोटू: सर पापा ने। टीचर: अगली बार खुद करना। छोटू: लेकिन सर आपने कहा था elders की help लेनी चाहिए 😅",
    "पति: बॉस ने कहा मैं बहुत lucky हूँ। बीवी: क्यों? पति: क्योंकि घर में भी boss तुम ही हो 😄",
]

def get_joke(lang):
    if lang == "Hindi":
        return random.choice(hindi_jokes)
    else:
        try:
            return pyjokes.get_joke(category="neutral")
        except:
            return "Why do programmers love yellow themes? Because bugs look cute 🐛😂"

# ─── WINDOW ──────────────────────────────────────────────
root = tk.Tk()
root.title("😂 Joke बाबा")
root.geometry("500x620")
root.configure(bg="#707001")   # light yellow
root.resizable(False, False)

# ─── MAIN FRAME ──────────────────────────────────────────
main = tk.Frame(root, bg="#e8cc13")
main.pack(fill="both", expand=True, padx=25, pady=25)

# ─── HEADER ──────────────────────────────────────────────
header = tk.Label(
    main,
    text="😂 Joke बाबा 😂",
    font=("Segoe UI Emoji", 34, "bold"),
    fg="#8B5A00",
    bg="#e8cc13"
)
header.pack(pady=(0, 20))

# ─── JOKE CARD ───────────────────────────────────────────
card = tk.Frame(main, bg="#FFFDE7", bd=0)
card.pack(fill="both", expand=True)

joke_text = tk.Text(
    card,
    wrap="word",
    font=("Segoe UI Emoji", 16),
    bg="#fce64e",
    fg="#5D4037",
    bd=0,
    padx=35,
    pady=35,
    height=8
)
joke_text.pack(fill="both", expand=True)

joke_text.tag_configure("center", justify="center")
joke_text.config(state="disabled")

# ─── CONTROLS ────────────────────────────────────────────
controls = tk.Frame(main, bg="#e8cc13")
controls.pack(fill="x", pady=20)

lang_var = tk.StringVar(value="English")

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Pretty.TRadiobutton",
    background="#e8cc13",
    foreground="#8B5A00",
    font=("Segoe UI", 13)
)

ttk.Radiobutton(
    controls, text="English 🇬🇧",
    variable=lang_var, value="English",
    style="Pretty.TRadiobutton"
).pack(side="left", padx=20)

ttk.Radiobutton(
    controls, text="हिंदी 🇮🇳",
    variable=lang_var, value="Hindi",
    style="Pretty.TRadiobutton"
).pack(side="left", padx=20)

# ─── BUTTON ──────────────────────────────────────────────
style.configure(
    "Fancy.TButton",
    font=("Segoe UI", 14, "bold"),
    padding=14,
    background="#FFD54F"
)

style.map(
    "Fancy.TButton",
    background=[("active", "#FFCA28")]
)

def show_new_joke():
    joke = get_joke(lang_var.get()).strip()

    joke_text.config(state="normal")
    joke_text.delete("1.0", tk.END)
    joke_text.insert(tk.END, f"✨ {joke} ✨", "center")
    joke_text.config(state="disabled")

btn = ttk.Button(
    main,
    text="🤣 अगला जोक",
    command=show_new_joke,
    style="Fancy.TButton"
)
btn.pack(pady=10)

# ─── FIRST JOKE ──────────────────────────────────────────
show_new_joke()

root.mainloop()
