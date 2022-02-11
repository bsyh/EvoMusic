class Note:
    def __init__(self):
        self.channel = 0
        self.note = 0
        self.velocity = 0
        self.tick = 0


    def __init__(self, channel, note, velocity, tick):
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.tick = tick

    def set_channel(self,channel):
        self.channel = channel

    def set_note(self,note):
        self.note = note

    def set_velocity(self,velocity):
        self.velocity = velocity

    def set_tick(self,tick):
        self.tick = tick


    def display(self):
        print("Note", self.channel, self.note, self.velocity, self.tick)


if __name__ == "__main__":
    note1 = Note(13,40,80,100)
    note1.display()