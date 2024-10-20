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
             noteToNumber("F", 3), 80, hNote],
            [1, initOnset+hNote,
             noteToNumber("A", 3), 80, qNote],
            [1, initOnset+hNote+qNote,
             noteToNumber("G", 3), 80, qNote],
            [1, initOnset+hNote+qNote+qNote,
             noteToNumber("G", 3), 80, eNote],
            [1, initOnset+hNote+qNote+qNote+eNote,
             noteToNumber("E", 3), 80, eNote],
            [1, initOnset+hNote+qNote+qNote+eNote+eNote+qNote+eNote,
             noteToNumber("F", 3), 80, sNote],
            [1, initOnset+hNote+qNote+qNote+eNote+eNote+qNote+eNote+sNote,
             noteToNumber("B", 3), 80, tNote*(3/4)],
            [1, initOnset+hNote+qNote+qNote+eNote+eNote+qNote+eNote+sNote+sNote,
             noteToNumber("F", 6), 80, eNote*(3/4)]]

synthesize(midiData, "piano", "big-dipper-piano.wav")

