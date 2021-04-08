import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import pretty_midi
from Voice import Voice

class Composition:
    def __init__(self):
        self.voices = []
        return
    
    def get_length(self):
        length_of_each_voice = []
        for i in range(0, len(self.voices)):
            length_of_each_voice.append(self.voices[i].get_length())
        return max(length_of_each_voice)
    
    def get_voice_at_index(self, index):
        return self.voices[index]
    
    def add_voice(self, voice):
        self.voices.append(voice)
        return
    
    def write_midi_data(self, fileName='compoyse_composition'):
        pm = pretty_midi.PrettyMIDI()
        for i in range(0, len(self.voices)):
            pm.instruments.append(self.voices[i].get_midi_data())
        pm.write(fileName + '.mid')
        return