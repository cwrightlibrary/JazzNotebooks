from music21 import *

def create_score(info, notes):
    s = stream.Score()
    part = stream.Part()
    if info[0] == "Treble":
        part.append(clef.TrebleClef())
    elif info[0] == "Bass":
        part.append(clef.BassClef)
    part.append(key.KeySignature(info[1]))
    part.append(meter.TimeSignature(info[2]))
    
    ns = notes.split(" ")
    for n in ns:
        if n[0] == "!":
            part.append(harmony.ChordSymbol(n[1:]))
        else:
            nnl = n.split("/")
            part.append(note.Note(nnl[0], quarterLength=float(nnl[1])))
    
    s.append(part)
    s.show("musicxml.png")

info = ["Treble", 0, "4/4"]
notes = "!Dm7 C#4/0.5 D4/0.5 F4/1 !G7 G4/1 B4/1 !Cmaj7 C5/4"
create_score(info, notes)
