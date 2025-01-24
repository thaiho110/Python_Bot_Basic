# This is the main file for the Improved ChatApp project
from tkinter import *
import customtkinter as ctk
from pathlib import Path
from openai import OpenAI
import ai_bot as ai

# Assets Path and define colors and fonts
FONT = 'Sans Serif'
FONT_BOlD = 'Sans Serif Bold'
BG_Gray = '#cef6ed'
BG_Light_Gray = '#e7eae6'
Text_Color_Sender = '#17202A'
Text_Color_AI = '#008080'
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\Tkinter-Designer-1.0.7\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
class ChatApp:
    def run(self):
        self.window.mainloop()
        
    def _on_enter_pressed(self, event):
        msg = self.entry_1.get()
        self._insert_message(msg, 'You: ')
    
    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.entry_1.delete(0, END)
        msg_sender = f'{sender} {msg}\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg_sender)
        self.text_widget.configure(state=DISABLED,fg=Text_Color_Sender)
        self.text_widget.see(END)
    
        
        msg_bot = f'{ai.get_bot_name()}: {ai.get_response(msg)}\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg_bot)
        self.text_widget.configure(state=DISABLED,fg=Text_Color_AI)
        self.text_widget.see(END)
    
       
    def __init__(self):
        self.window = Tk()
        self.window.geometry("650x450")
        self.window.configure(bg = "#FFFFFF")
        self.canvas = Canvas(self.window,bg = "#FFFFFF",height = 450,width = 650,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0,0.0,650.0,450.0,fill="#D9D9D9",outline="")
        self.window.title('Chat App')
        self.window.resizable(width=False, height=False)    
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(280.0,408.0,image=self.entry_image_1)
    
    # Entry message box
        self.entry_1 = Entry(bd=0,bg="#CCC3C3",fg="#000716",highlightthickness=0)
        self.entry_1.place(x=25.0,y=383.0,width=510.0,height=48.0)
        self.entry_1.bind('<Return>', self._on_enter_pressed)
        self.canvas.create_rectangle(16.0,80.0,636.0,370.0,fill="#BAA8A8",outline="")
     
    # Send button
        self.button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.button_image_1,borderwidth=0,highlightthickness=0,command=lambda: self._on_enter_pressed(None),relief="flat")
        self.button_1.place(x=586.0,y=383.0,width=50.0,height=50.0)    
    
    # Bot name display
        head_label =Label(self.window, bg="#FFFFFF", fg="#000716", 
                                text=ai.get_bot_name(), font=(FONT, 18), pady=10)
        head_label.place(relwidth=1)
    
    #text widget
        self.text_widget = Text(self.canvas, width=20, height=2, 
                    bg="#D9D9D9", font=(FONT, 11), padx=5, pady=5, wrap=WORD,highlightthickness = 0,relief = "ridge")
        self.text_widget.place(x = 16.0, y = 80.0, width = 620.0, height = 290.0)
        self.text_widget.configure(cursor='arrow', state=DISABLED)
    
    # # message display bot   
    #     self.canvas.create_rectangle(69.0,99.0,539.0,144.0,fill="#D9D9D9",outline="")
    #     self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    #     self.image_1 = self.canvas.create_image(44.0,121.0,image=self.image_image_1)

    # # message display user
    #     self.canvas.create_rectangle(116.0,183.0,586.0,228.0,fill="#D9D9D9",outline="")
    #     self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    #     self.image_2 = self.canvas.create_image(611.0,205.0,image=self.image_image_2)
        
if __name__ == '__main__':
    app = ChatApp()
    app.run()