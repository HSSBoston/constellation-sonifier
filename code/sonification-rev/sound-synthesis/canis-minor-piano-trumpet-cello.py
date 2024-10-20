from synthesizer import synthesize
from notes import *

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
midiData = [[1, initOnset,
             noteToNumber("A", 4), 100, hNote],
            [1, initOnset+hNote+tNote ,
             noteToNumber("C", 5), 100, hNote-tNote]]
midiData2 = [[1, initOnset,
             noteToNumber("A", 4), 100, hNote],
             [1, initOnset+hNote+tNote,
              noteToNumber("A",4), 0, hNote-tNote]]
midiData3 = [[1, initOnset,
             noteToNumber("C#", 3), 40, hNote],
             [1, initOnset+hNote+tNote,
              noteToNumber("E",3), 40, hNote-tNote]]
synthesize(midiData, "piano", "canis-minor-piano.wav")
synthesize(midiData2, "trumpet", "canis-minor-trumpet.wav")
synthesize(midiData3, "cello", "canis-minor-cello.wav")
