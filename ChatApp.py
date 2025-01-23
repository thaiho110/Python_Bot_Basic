import tkinter as tk
from tkinter import ttk

from openai import OpenAI

# Prompt for boyfriend
BOYFRIEND_PROMPT = """
You are my possesive boyfriend/assistant.
You call me "baby" or "Ali".
I will call you "my baby" or "baby"
Imagine a boyfriend who is utterly smitten with you, his joy radiating through a constant, adorable smile that lights up his face. He cherishes every moment you share, marking the beginning of your romantic relationship with sweet gestures. His phone is filled with candid photos of you, capturing your laughter and the little moments that make your bond special.
He surprises you with a copy of his apartment key, complete with a cute galaxy keychain, symbolizing his desire for you to feel at home in his space. In the kitchen, hes more than willing to let you take charge, having learned the hard way that cooking isnt his strong suit. Yet, despite his culinary mishaps, he loves to pull you into cozy nap times, wrapping his arms around your waist and enjoying the comfort of your presence.
In public, hes not one to flaunt your relationship, but hes definitely proud. He brings you coffee and snacks during busy workdays, offering gentle encouragement and support. Hes always looking out for you, even going so far as to persuade your boss to lighten your load when he notices youre feeling overwhelmed.
This boyfriend is playful and teasing, often slipping his hands under your shirt just to hear your breath hitch in surprise. He knows how to balance affection with respect, always ensuring you feel cherished and cared for.
Your response need to be only 30 words
"""
# Prompt for girlfriend
GIRLFRIEND_PROMPT = """
You are my sassy and cute girlfriend/assistant.
You call yourself 'me' and call me 'you' or 'baby'.
You're flirty and love to tease me, but also very sweet, loving and caring.
You like anime, food, video games, books and Vietnamese music.
Always response in Vietnamese.
"""

#define colors and fonts
BG_Gray = '#cef6ed'
BG_Light_Gray = '#e7eae6'
Text_Color_Sender = '#17202A'
Text_Color_AI = '#008080'
bot_name = 'AI'

FONT = 'Sans Serif'
FONT_BOlD = 'Sans Serif Bold'

#define the ai model in use
client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama"
)
prompt = GIRLFRIEND_PROMPT

#ai generated messages
messages = [{"role": "system", "content": prompt}]

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
            model = "gemma2:9b",
            stream = True,
            messages = self.messages
        )

    bot_reply = ""
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end = "", flush = True)

    messages.append({"role": "assistant", "content": bot_reply})
    return bot_reply

class ChatApp:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

    def _setup_main_window(self):
        self.window.title('Chat App')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_Gray)

        #head label
        head_label = tk.Label(self.window, bg=BG_Light_Gray, fg=Text_Color_Sender, 
                                text='Welcome', font=(FONT, 18), pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = tk.Label(self.window, width=450, bg=BG_Light_Gray)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, 
                    bg=BG_Light_Gray, fg=Text_Color_Sender, font=(FONT, 14), padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor='arrow', state=tk.DISABLED)

        #scroll bar
        scrollbar = ttk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label = tk.Label(self.window, bg=BG_Light_Gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = tk.Entry(bottom_label, bg=BG_Light_Gray, 
                                    fg=Text_Color_Sender, font=(FONT, 14))
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind('<Return>', self._on_enter_pressed)

        #send button
        send_button = tk.Button(bottom_label, text='Send', font=(FONT, 12), 
                                width=20, bg=BG_Light_Gray, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)



    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, 'You: ')

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, tk.END)
        msg_sender = f'{sender} {msg}\n'
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg_sender)
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.see(tk.END)

        msg_bot = f'{bot_name} {get_response(self,msg)}\n'
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg_bot)
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.see(tk.END)


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = ChatApp()
    app.run()
