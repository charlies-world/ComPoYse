import unittest
import pretty_midi
from compoyse.midi.Note import Note
from compoyse.midi.Meter import Meter
from compoyse.midi.MIDIExceptions import ValueNotValidMIDIValue

class TestNote(unittest.TestCase):
    def test___init___no_parameters__defaults_are_set(self):
        test_note = Note()
        self.assertEquals(test_note.get_note_data(), [0,'C', 0, ''], "Notes values are the default parameters.")
        return
    
    def test_set_velocity__velocity_is_set(self):
        test_note = Note()
        test_note.set_velocity(100)
        self.assertEquals(test_note.get_velocity(), 100, "Velocity is 100.")
        return
    
    def test_set_letter__letter_is_set(self):
        test_note = Note()
        test_note.set_letter('C')
        self.assertEquals(test_note.get_letter(), 'C', "Note is D.")
        return
    
    def test_set_octave__octave_is_set(self):
        test_note = Note()
        test_note.set_octave(5)
        self.assertEquals(test_note.get_octave(), 5, "Octave is 5.")
        return
    
    def test_set_midi_value__midi_value_is_set(self):
        test_note = Note()
        test_note.set_midi_value(100)
        self.assertEquals(test_note.get_midi_value(), 100, "Midi value is 100.")
        return
    
    def test_set_rhythmic_value__rhythmic_value_is_set(self):
        test_note = Note()
        test_note.set_rhythmic_value(['quarter'])
        self.assertEquals(test_note.get_rhythmic_value(), ['quarter'], "Note is a quarter note.")
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        test_note = Note()
        test_note.set_velocity(100)
        test_note.set_letter('C')
        test_note.set_octave(5)
        test_note.set_rhythmic_value(['whole'])
        test_note.set_start_and_end(0, test_meter)
        
        test_note_midi_data = test_note.get_midi_data()
        
        self.assertEquals(test_note_midi_data.get_duration(), 4, "MIDI note calls pretty_midi function and is 4 seconds long.")
        return
    
    def test_is_note__returns_true(self):
        test_note = Note()
        self.assertEquals(test_note.is_note(), True, "This is a note.")
        return
    