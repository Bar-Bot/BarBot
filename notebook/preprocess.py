import os

def get_bars(path, artist):
    artist_path = f"{artist}_lyrics.txt"    
    path = os.path.join(path, artist_path)
    with open(path, mode='r', encoding="utf8") as f:
        text = f.read()
    bars = text.split("\n")
    while "" in bars:
        bars.remove("")
    return bars

def save_bars(bars, artist):
    path = "../data/bars/"
    path = os.path.join(path, artist)
    
    if not os.path.isdir(path):
        os.mkdir(path)
        
    bar_path = os.path.join(path, "bars.txt")
        
    with open(bar_path, mode='w', encoding="utf8") as f:
        for bar in bars:
            f.write(f"{bar} <eob>\n")
            
    return bar_path
    