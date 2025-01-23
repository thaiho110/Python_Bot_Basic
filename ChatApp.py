import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from openai import OpenAI
import ai_bot as ai

#set default apperance
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

#define colors and fonts
BG_Gray = '#cef6ed'
BG_Light_Gray = '#e7eae6'
Text_Color_Sender = '#17202A'
Text_Color_AI = '#008080'

FONT = 'Sans Serif'
FONT_BOlD = 'Sans Serif Bold'

class ChatApp:
    
    
    def __init__(self):
        self.window = ctk.CTk()
        self._setup_main_window()

    def _setup_main_window(self):
        self.window.title('Chat App')
        self.window.resizable(width=True, height=True)
        self.window.configure(width=800, height=600, bg=BG_Gray)

        #head label
        head_label = tk.Label(self.window, bg=BG_Light_Gray, fg=Text_Color_Sender, 
                                text='Welcome', font=(FONT, 18), pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = tk.Label(self.window, width=450, bg=BG_Light_Gray)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, 
                    bg=BG_Light_Gray, fg=Text_Color_Sender, font=(FONT, 14), padx=5, pady=5, wrap=tk.WORD)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor='arrow', state=tk.DISABLED)


        #bottom label
        bottom_label = tk.Label(self.window, bg=BG_Light_Gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = tk.Entry(bottom_label, bg=BG_Light_Gray, 
                                    fg=Text_Color_Sender, font=(FONT, 14))
        self.msg_entry.grid(row=2, column=0)
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

        msg_bot = f'AI: {ai.get_response(msg)}\n'
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg_bot)
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.see(tk.END)


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = ChatApp()
    app.run()
