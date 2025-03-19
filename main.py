import os
import eel
import sys
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():
    try:
        eel.init("frontend") 
        
        play_assistant_sound()
        @eel.expose
        def init():
            try:
                eel.hideLoader()
                speak("Welcome to Jarvis")
                speak("Ready for Face Authentication")
                flag = recoganize.AuthenticateFace()
                if flag == 1:
                    speak("Face recognized successfully")
                    eel.hideFaceAuth()
                    eel.hideFaceAuthSuccess()
                    speak("Welcome to Your Assistant")
                    eel.hideStart()
                    play_assistant_sound()
                else:
                    speak("Face not recognized. Please try again")
            except Exception as e:
                print(f"Error in init: {str(e)}")
                
        # Use a more compatible browser option
        browser_path = None
        if os.path.exists("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"):
            browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        elif os.path.exists("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"):
            browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        
        if browser_path:
            os.system(f'start "" "{browser_path}" --app="http://localhost:8000/index.html"')
        else:
            os.system('start msedge.exe --app="http://localhost:8000/index.html"')
        
        # Add error handling for eel.start
        try:
            eel.start("index.html", mode=None, host="localhost", block=True)
        except Exception as e:
            print(f"Eel error: {str(e)}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

