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

def find_command(text):
    text_upper_list= text.upper().split()
    for x in text_upper_list:
        #command == music
        print(x)
        if x == "MUSIC":
            for y in text_upper_list:
                if (y== "ON" or y== "PLAY"):
                    return music_start
                elif y== "pause".upper():
                    return music_pause
                elif y=="stop".upper():
                    return music_stop
        #command == wheater
        if x == "Weather".upper():
            for y in text_upper_list:
                if y== "in".upper() and y<len(text_upper_list)-1:
                    position = text_upper_list[y+1]
                    weather_position= {
                        "category": "weather",
                        "attributes": {
                            "position": str(position)
                        } 
                    }
                    return weather_position
                else:
                    return weather_tue