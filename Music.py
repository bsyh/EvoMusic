from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message,MetaMessage
from Note import Note
class Music:
    def __init__(self):
        self.track_list = []
        self.tick_length = 100



    def append_track(self,new_track):
        self.track_list.append(new_track)


    def display(self):
        for i in range(len(self.track_list)):
            print("Track", i)
            print("Note:",end="\t")
            for j in range(len(self.track_list[i].note_list)):
                print(self.track_list[i].note_list[j].note, end='\t\t')
            print("")
            print("Tick:", end="\t")
            for j in range(len(self.track_list[i].note_list)):
                print(self.track_list[i].note_list[j].tick, end='\t\t')
            print("")
            print("Type:", end="\t")
            for j in range(len(self.track_list[i].note_list)):
                print(self.track_list[i].note_list[j].type, end='\t')
            print("")

            print("")


    def save_midi(self,save_path = 'new_song.mid'):
        mid = MidiFile()
        for track_index in range(len(self.track_list)):
            track = MidiTrack()
            mid.tracks.append(track)
            track.append(Message('program_change', program=12, time=0))
            for note_index in range(self.track_list[track_index].size):
                # print("有track",track_index)
                note = self.track_list[track_index].note_list[note_index]
                velocity = note.velocity
                note_note = note.note
                tick = note.tick
                channel = note.channel
                if note.type:
                    track.append(Message('note_on', channel=channel, note=note_note, velocity=velocity, time=tick))
                else:
                    track.append(Message('note_off', channel=channel, note=note_note, velocity=velocity, time=tick))
        track.append(MetaMessage('end_of_track', time=0))
        mid.save(save_path)


if __name__ == "__main__":



    pass