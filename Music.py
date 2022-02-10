from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message
from Note import Note
class Music:
    def __init__(self):
        self.track_list = []
        self.tick_length = 100



    def append_track(self,new_track):
        self.track_list.append(new_track)


    def save_midi(self,save_path = 'new_song.mid'):
        mid = MidiFile()
        for track_index in range(len(self.track_list)):
            track = MidiTrack()
            mid.tracks.append(track)
            track.append(Message('program_change', program=12, time=0))
            for note_index in range(self.track_list[track_index].size):
                print("有track",track_index)
                note = self.track_list[track_index].note_list[note_index]
                velocity = note.velocity
                note_note = note.note
                tick = note.tick
                channel = note.channel
                if note.velocity == 0:
                    track.append(Message('note_off', channel=channel, note=note_note, velocity=velocity, time=tick))
                else:
                    track.append(Message('note_on', channel=channel, note=note_note, velocity=velocity, time=tick))

        mid.save(save_path)


if __name__ == "__main__":



    pass