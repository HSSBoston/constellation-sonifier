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
             noteToNumber("F", 4), 50, qNote+eNote],
            [1, initOnset+qNote+eNote,
             noteToNumber("C", 5), 50, sNote*(3/4)],
            [1, initOnset+qNote+eNote+eNote,
             noteToNumber("E", 5), 50, qNote],
            [1, initOnset+qNote+eNote+eNote+qNote,
             noteToNumber("F", 5), 50, eNote*(3/4)],
            [1, initOnset+qNote+eNote+eNote+qNote+qNote+qNote,
             noteToNumber("A", 4), 50, qNote],
            [1, initOnset+qNote+eNote+eNote+qNote+qNote+qNote+qNote,
             noteToNumber("C", 4), 50, hNote],
            [1, initOnset+qNote+eNote+eNote+qNote+qNote+qNote+qNote,
             noteToNumber("A", 5), 50, hNote]]
midiData2 = [[1, initOnset+qNote+eNote+eNote,
             noteToNumber("E", 5), 50, qNote],
             [1, initOnset+qNote+eNote+eNote+qNote,
             noteToNumber("E", 5), 0, qNote+hNote*2]]


#synthesize(midiData, "piano", "aquila-piano.wav")
synthesize(midiData2, "trumpet", "aquila-trumpet.wav")

