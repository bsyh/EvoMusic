def writeAndExport(listNotes):
  # multitrack midifile of 4 tracks
  # first track: guitar
  # second track: bass
  # third track: synth
  # fourth track: drums
  midiFile = MIDIFile(4)
  midiChannel = 0
  midiVolume = 127




  ### bass
  midiTrackBeatCounter = 0
  midiTrack = 2
  midiFile.addTrackName(midiTrack, 0, "Bass MIDI")

  for i in range(0, len(listNotes[1][0])):
    if (listNotes[1][0][i] != -1):
      #time: the time at which the note sounds. The value can be either
      #     quarter notes [Float], or ticks [Integer]. Ticks may be specified by
      #     passing eventtime_is_ticks=True to the MIDIFile constructor.
      #     The default is quarter notes.
      # :param duration: the duration of the note. Like the time argument, the
      #     value can be either quarter notes [Float], or ticks [Integer].
    
      midiFile.addNote(self, track, channel, pitch, time, duration, volume)
      midiFile.addNote(midiTrack, midiChannel, listNotes[1][0][i], midiTrackBeatCounter, listNotes[1][1][i] * 4,
                       midiVolume)
    midiTrackBeatCounter += listNotes[1][1][i] * 4


  with open(getFileName() + '.mid', 'wb') as outf:
    midiFile.writeFile(outf)
