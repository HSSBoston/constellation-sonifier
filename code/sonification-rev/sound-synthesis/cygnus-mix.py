from mixer import mix

trackFileNames = ["wav/cygnus-piano-reverb.wav",
                  "wav/cygnus-cello-reverb.wav",
                  "wav/cygnus-trumpet-reverb.wav"]
mix(trackFileNames, "wav/cygnus-mixed-reverb.wav")