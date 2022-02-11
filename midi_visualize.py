from roll import MidiFile
def midi_visualize(path):
    mid = MidiFile(path)
    mid.draw_roll()