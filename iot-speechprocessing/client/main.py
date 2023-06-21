from print_helpers import print_seperator, print_help
from Replay import replay_recording
from PreProcessing import filterAudioSignal
from record import start_recording
from convert import convert
from TCP_Client import speech_to_text
import os
import re
import json

CONFIG_FILE_NAME = "config.json"

def check_file_exists(file_name):
    return os.system(f"ls {file_name} > /dev/null 2>&1") == 0 #dann gibt es die Datei


if __name__ == "__main__":
    print()
    print("IOT Spracherkennung!")
    print()
    print_seperator()
    print_help()
    print_seperator()
    print()
    
    #Initializing a last_recording Variable
    last_recording = None

    # Dictionary für config-Parameter
    config = {}
    try:
        config = json.load(open(CONFIG_FILE_NAME, "r")) # liest die alte Konfiguration wieder ein 
    except OSError:
        print("Keine alte Konfiguration gefunden!")
        print("Benutze Standardkonfiguration")
        config = {
            "port": 2020,
            "max_rec_time": 10,
            "server_ip": "127.0.0.1"
        }
    
    while True:
        command = input("> ").strip()

        if command == "rec" or command == "":
            #10 Sekunden Aufnahme
            last_recording = start_recording()
            
            #"outputFile.wav" und "FilteredSignal.wav" sind temporär. 
            #Sie geben an, welche Datei gefiltert wird 
            # und als was sie gespeichert wird.
            #filterAudioSignal("outputFile.wav", "FilteredOutputFile.wav")
            #Umwandeln in Numpy-Array
            #last_recording = convert("outputFile.wav")

            text = speech_to_text(last_recording)

            print()
            print("Rückgabe:")
            print(text)
            print()
                
        elif command == "play":
            # 44100 und 'sysdefault' sind temporäre werte, damit die Funktion
            # auch ohne config schon funktionieren kann
            try:
                replay_recording(last_recording, 44100, 'sysdefault')
            except OSError:
                print("No existing recording could be found!")

        elif command[:4] == "play":
            file_name = command[5:]
            try:
                sound_file = convert(file_name)
                replay_recording(sound_file, 44100, 'sysdefault')
            except OSError:
                print("No existing recording could be found!")

        elif command == "exit":
            break
        
        elif command == "help":
            print_help()
            
        elif command[:4] == "save":
            # entfernt whitespace
            file_name = command[4:].replace(" ", "").replace("\n","").replace("\t","")
            try:
                os.system(f"cp outputFile.wav {file_name}")
            except OSError:
                print("No existing recording could be found!")

        elif command[:3] == "set":
            command = re.sub("\s+", " ", command)
            parts = command.split(" ")

            key, value = parts[1], parts[2]

            if key in config:
                config[key] = value
                json.dump(config, open(CONFIG_FILE_NAME, "w"))
            else:
                print("Diesen key gibt es nicht")

        elif command[:5] == "print":
            if command.strip() == "print" or re.findall("print\s+config(uration)?", command.strip()):
                for key, value in config.items():
                    print(f"{key}:              {value}")

            else:
                command = re.sub("\s+", " ", command)
                parts = command.split(" ")

                key = parts[1]

                if key in config:
                    print(f"{key}:              {config[key]}")
        else:
            print("No valid Command!")
    

