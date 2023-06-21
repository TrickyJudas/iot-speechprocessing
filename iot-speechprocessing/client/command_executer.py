import vlc
import sys
import os

class Command_Executer:

    def __init__(self):
        self.media_player = vlc.MediaPlayer("http://stream.antenne.de/antenne/stream/mp3")

    def execute(self, obj):
        category, attributes = obj["category"], obj["attributes"]

        if category == "weather":
            self.__weather(attributes)
        elif category == "music":
            self.__music(attributes)
        else:
            print("Unbekannter Befehl!")



    def __weather(self, attr):
        position = attr["position"]

        print(f"Das Wetter in {position} ist entweder bewölkt oder nicht")

    def __music(self, attr):
        state = attr["state"]

        if state == "play":
            self.media_player.play()
        elif state == "pause":
            self.media_player.pause()
        else:
            self.media_player.stop()


if __name__ == "__main__":

    import time

    ce = Command_Executer()

    weather_tue = {
        "category": "weather",
        "attributes": {
            "position": "Tübingen"
        } 
    }
    music_start = {
        "category": "music",
        "attributes": {
            "state": "play"
        } 
    }
    music_pause = {
        "category": "music",
        "attributes": {
            "state": "pause"
        } 
    }
    music_stop = {
        "category": "music",
        "attributes": {
            "state": "stop"
        } 
    }

    ce.execute(weather_tue)
    print()

    print("Playing music")
    ce.execute(music_start)
    time.sleep(5)
    print("Music paused")
    ce.execute(music_pause)
    time.sleep(3)
    print("Music resumed")
    ce.execute(music_start)
    time.sleep(5)
    print("Music stopped")
    ce.execute(music_stop)