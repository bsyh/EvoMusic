class Note:
    def __init__(self):
        self.channel = 0
        self.note = [0]
        self.velocity = 0
        self.start_time = 0
        self.duration = 0


    def __init__(self, channel, note, velocity, start_time, duration):
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.start_time = start_time
        self.duration = duration


    def display(self):
        print("Note", self.channel, self.note, self.velocity, self.start_time, self.duration)


if __name__ == "__main__":


    pass