import tkinter as tk
import pyjokes

def jok():
    t.config(text=pyjokes.get_joke())

zx = tk.Tk()
zx.geometry("500x500")
zx.title("😂 Joke Generator")
zx.configure(bg="#f2f2f2")

# Title
title = tk.Label(
    zx,
    text="😂 Joke Generator",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=20)

# Joke box
t = tk.Label(
    zx,
    text=pyjokes.get_joke(),
    font=("Arial", 16),
    wraplength=450,
    justify="center",
    bg="#ffffff",
    padx=20,
    pady=20
)
t.pack(padx=20, pady=30)

# Button
btn = tk.Button(
    zx,
    text="New Joke 😂",
    font=("Arial", 14, "bold"),
    command=jok,
    bg="#ffcc00",
    activebackground="#ffdb4d",
    relief="flat",
    padx=15,
    pady=8
)
btn.pack()

# Footer
footer = tk.Label(
    zx,
    text="😄 Made with Python",
    font=("Arial", 11),
    bg="#f2f2f2"
)
footer.pack(side="bottom", pady=10)

zx.mainloop()
