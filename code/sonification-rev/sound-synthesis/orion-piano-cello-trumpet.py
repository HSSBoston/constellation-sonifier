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
             noteToNumber("F", 5), 50, qNote],
            [1, initOnset+qNote,
             noteToNumber("C", 4), 35, qNote],
            [1, initOnset+qNote+qNote,
             noteToNumber("G", 4), 110, qNote],
            [1, initOnset+qNote+qNote+qNote,
             noteToNumber("A", 5), 35, eNote],
            [1, initOnset+qNote+qNote+qNote+eNote,
             noteToNumber("A", 4), 110, eNote+qNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote,
             noteToNumber("B", 4), 35, qNote+eNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote,
             noteToNumber("F", 5), 110, qNote+eNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote+qNote+eNote,
             noteToNumber("D", 4), 50, qNote+eNote]]
midiData2 = [[1, initOnset,
             noteToNumber("B", 3), 35, qNote],
            [1, initOnset+qNote,
             noteToNumber("E", 2), 35, qNote],
            [1, initOnset+qNote+qNote,
             noteToNumber("B", 2), 35, qNote],
            [1, initOnset+qNote+qNote+qNote,
             noteToNumber("C", 4), 35, eNote],
            [1, initOnset+qNote+qNote+qNote+eNote,
             noteToNumber("C", 3), 35, eNote+qNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote,
             noteToNumber("D", 3), 35, qNote+eNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote,
             noteToNumber("A", 3), 35, qNote+eNote],
            [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote+qNote+eNote,
             noteToNumber("F", 2), 35, qNote+eNote]]
midiData3 = [[1, initOnset,
             noteToNumber("F", 5), 45, qNote],
            [1, initOnset+qNote,
             noteToNumber("F", 5), 0, qNote+hNote*2+eNote],
            [1, initOnset+qNote+qNote+hNote*2+eNote,
             noteToNumber("D", 4), 45, qNote+eNote]]

synthesize(midiData, "piano", "orion-piano.wav")
synthesize(midiData2, "cello", "orion-cello.wav")
synthesize(midiData3, "trumpet", "orion-trumpet.wav")
