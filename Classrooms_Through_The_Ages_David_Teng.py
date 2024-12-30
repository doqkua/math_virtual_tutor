import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3
import tkinter as tk
import re

pairs = [
    (r'hi|hello|hey', ['Hello, I am your Virtual Math Tutor. How can I help you?']), 
    (r'(.*\btopics?\b.*math.*)', ['Here are the following topics in Math: \n - Addition\n - Subtraction\n - Multiplication\n - Division']),
    (r'(.*\baddition?\b)|(.*\badd?\b)', ['To add numbers, you must know how do you get an extra item. For example, if I have 1 apple, and I ask for 2 more apples, how many apples is that? It is 3 apples because I ask for two extra apples. This means 1 plus 2 = 3.']), 
    (r'(.*\bsubtraction?\b)|(.*\bsubtract?\b)', ['To subtract numbers, you must know how did your item got discarded. For example if I have 3 pencils, and I lost 1 pencil, how many pencils do I have now? It is two pencils because I lost 1 pencil. This means 3 minus 1 = 2.']),
    (r'(.*\bmultiplication?\b)|(.*\bmultiply?\b)', ['To multiply numbers, you must know that it is repeated addition. For example, if I have four lollipops each, and I want to separate the lollipops into five groups, how many lollipops did I separate? It is twenty lollipops because there is four lollipops in one group. This means 4 times 5 = 20.']),
    (r'(.*\bdivision?\b)|(.*\bdivide?\b)', ['To divide numbers, you must know that it is repeated subtraction. For example, if I have twenty boxes, and I give five boxes each per person, how many people did I give the boxes to? It is four people because I give them five boxes for one person. This means 20 divided by 5 = 4.']),
    (r'(.*\bthank?\b.*you.*)|(.*\bthanks?\b)', ["You're welcome!"]),
    (r'(.*\bgoodbye?\b)', ["Goodbye! Thank you for spending time with me. I hope I was helpful. Take care and see you soon!"])
]

chat = Chat(pairs, reflections)

engine = pyttsx3.init()
def speaker(text): 
    engine.say(text)
    engine.runAndWait()

def calculate_expression(expression): 
        try: 
            expression = re.sub(r'\s+', '', expression)
            res = eval(expression)
            return "The answer is: {:.2f}".format(res)
        except Exception: 
            return "Sorry, I can't understand the math expression. Please check and try again."

def response(): 
    user_input = user_entry.get()
    response = chat.respond(user_input)
    if re.match(r'^[\d+\-*/().\s]+$', user_input): 
         response = calculate_expression(user_input)
         if not response: 
            response = "I'm sorry, I didn't understand that. Could you rephrase?"
    speaker(response)
    chat_display.insert(tk.END, f"\nYou: {user_input}\n")
    chat_display.insert(tk.END, f"\nVirtual Math Tutor: {response}\n")
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Virtual Math Tutor')

chat_display = tk.Text(root, height=20, width=50, bg='white')
chat_display.pack()

user_entry = tk.Entry(root, width=40)
user_entry.pack()

send_button = tk.Button(root, text='Send', command=response)
send_button.pack()

root.mainloop()