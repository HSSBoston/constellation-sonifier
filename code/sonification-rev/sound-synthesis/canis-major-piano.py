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
             noteToNumber("D", 4), 35, eNote+sNote],
            [1, initOnset+eNote+sNote,
             noteToNumber("G", 4), 110, eNote+sNote],
            [1, initOnset+eNote+sNote+eNote+sNote,
             noteToNumber("E", 4), 110, sNote],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote,
             noteToNumber("A", 4), 35, tNote*(3/4)],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote,
             noteToNumber("F", 5), 75, eNote],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote+eNote,
             noteToNumber("D", 5), 35, eNote*(3/4)],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote+eNote+qNote,
             noteToNumber("E", 5), 110, eNote]]
midiData2 = [[1, initOnset,
             noteToNumber("F", 5), 0, hNote],
             [1, initOnset+hNote,
             noteToNumber("F", 5), 100, eNote],
             [1, initOnset+hNote+eNote,
             noteToNumber("F", 5), 0, qNote+eNote]]
midiData3 = [[1, initOnset,
             noteToNumber("F", 2), 35, eNote+sNote],
            [1, initOnset+eNote+sNote,
             noteToNumber("B", 2), 35, eNote+sNote],
            [1, initOnset+eNote+sNote+eNote+sNote,
             noteToNumber("G", 2), 35, sNote],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote,
             noteToNumber("C", 3), 35, tNote*(3/4)],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote,
             noteToNumber("A", 3), 35, eNote],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote+eNote,
             noteToNumber("G", 3), 35, eNote*(3/4)],
            [1, initOnset+eNote+sNote+eNote+sNote+sNote+sNote+eNote+qNote,
             noteToNumber("A", 3), 35, eNote]]


synthesize(midiData, "piano", "canis-major-piano.wav")
synthesize(midiData2, "trumpet", "canis-major-trumpet.wav")
synthesize(midiData3, "cello", "canis-major-cello.wav")
