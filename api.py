import pickle
from util import Track,Music,one_pt_crossover,reverse_mutation,evaluation,feedmax
from midi_visualize import midi_visualize
import shutil
import os
from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message

# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
# roll = mid.get_roll()

# draw piano roll by pyplot
# mid.draw_roll()
from rule_weight import set_weight, read_weight
import pickle

# provide choice

from feature_extraction import read_to_notes,containsPattern,compose
from util import Feature,Feature_pool,original


def initialize(some_para_settings):
    pass

def evolve(decision):
    pass

