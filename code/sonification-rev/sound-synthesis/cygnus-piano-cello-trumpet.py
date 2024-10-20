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
             noteToNumber("C", 4), 75, hNote-tNote],
            [1, initOnset+hNote,
             noteToNumber("E", 4), 75, eNote],
            [1, initOnset+hNote+eNote,
             noteToNumber("E", 5), 75, qNote],
            [1, initOnset+hNote+eNote+qNote,
             noteToNumber("B", 4), 75, eNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote,
             noteToNumber("E", 5), 75, eNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote+eNote,
             noteToNumber("B", 5), 75, qNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote+eNote+qNote,
             noteToNumber("B", 3), 75, qNote]]
midiData2 = [[1, initOnset,
             noteToNumber("E", 2), 35, hNote-tNote],
            [1, initOnset+hNote,
             noteToNumber("G", 2), 35, eNote],
            [1, initOnset+hNote+eNote,
             noteToNumber("G", 3), 35, qNote],
            [1, initOnset+hNote+eNote+qNote,
             noteToNumber("D", 3), 35, eNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote,
             noteToNumber("G", 3), 35, eNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote+eNote,
             noteToNumber("D", 4), 35, qNote],
            [1, initOnset+hNote+eNote+qNote+eNote+qNote+eNote+eNote+qNote,
             noteToNumber("D", 2), 35, qNote]]
midiData3 = [[1, initOnset+hNote+eNote,
             noteToNumber("E", 5), 40, qNote],
            [1, initOnset+hNote+eNote+qNote,
             noteToNumber("E", 5), 0, eNote+hNote*2]]

#synthesize(midiData, "piano", "cygnus-piano.wav")
#synthesize(midiData2, "cello", "cygnus-cello.wav")
synthesize(midiData3, "trumpet", "cygnus-trumpet.wav")
