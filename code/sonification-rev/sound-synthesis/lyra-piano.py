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
             noteToNumber("F", 4), 50, eNote+sNote],
            [1, initOnset+eNote+sNote,
             noteToNumber("B", 4), 50, eNote+sNote],
            [1, initOnset+eNote+sNote+eNote+sNote,
             noteToNumber("G", 4), 50, qNote],
            [1, initOnset+eNote+sNote+eNote+sNote+qNote,
             noteToNumber("D", 5), 50, sNote],
            [1, initOnset+eNote+sNote+eNote+sNote+qNote+sNote,
             noteToNumber("B", 4), 50, tNote*(3/4)],
            [1, initOnset+eNote+sNote+eNote+sNote+qNote+sNote+sNote,
             noteToNumber("C#", 5), 50, qNote]]
midiData2 = [[1, initOnset+hNote+qNote,
             noteToNumber("C#", 5), 35, qNote]]


#synthesize(midiData, "piano", "lyra-piano.wav")
synthesize(midiData2, "trumpet", "lyra-trumpet.wav")

