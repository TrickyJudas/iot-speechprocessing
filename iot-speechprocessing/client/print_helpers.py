def print_help():
    """Zeigt eine Übesicht über die möglichen Befehle an"""

    print()
    print("Befehle:")
    print("<enter>                  entsprichte 'rec'")
    print("rec                      um eine Aufnahme zu starten")
    print("play                     um die letzte Aufnahme wieder abzuspielen")
    print("play <filename.wav>      um filename.wav abzuspielen")
    print("save <filename.wav>      um die letzte Aufnahme abzuspeichern")
    print("print <key>              um den zum <key> zugehörigen <value> in der config anzuzeigen")
    print("print (config)           um die ganze config anzuzeigen")
    print("set <key> <value>        um den <value> zu <key> in der config zu setzen")
    print("exit                     um das Programm zu verlassen")
    print("help                     um diese Hilfe anzuzeigen")
    print()

def print_seperator(symbol = "-", symbols_per_line = 100, num_lines = 2):
    """Erzeugt einen Trennstrich in der Konsole.
    
    Keyword arguments:
    symbol -- das Symbol aus dem der Trennstrich gebildet wird (String)
    symbols_per_line -- wie viele solche Symbole pro Zeile erzeugt werden (int)
    num_lines -- Anzahl der Zeilen (int)
    """

    for _ in range(num_lines):
        for _ in range(symbols_per_line):
            print(symbol, end="")
        
        print()
