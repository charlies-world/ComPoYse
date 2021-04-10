class Meter:
    def __init__(self):
        return
    
    def set_length_of_quarter_in_seconds(self, bpm_length_of_quarter):
        NUMBER_OF_SECONDS_IN_A_MINUTE = 60
        self.length_of_quarter_in_seconds = (bpm_length_of_quarter / NUMBER_OF_SECONDS_IN_A_MINUTE)
        return
    
    def compute_rhythmic_value_length_in_seconds(self, rhythmic_value):
        if(rhythmic_value == 'two_hundred_fifty_sixth'):
            return self.length_of_quarter_in_seconds / 64
        elif(rhythmic_value == 'one_hundred_twenty_eighth'):
            return self.length_of_quarter_in_seconds / 32
        elif(rhythmic_value == 'sixty_fourth'):
            return self.length_of_quarter_in_seconds / 16
        elif(rhythmic_value == 'thirty_secondth'):
            return self.length_of_quarter_in_seconds / 8
        elif(rhythmic_value == 'sixteenth'):
            return self.length_of_quarter_in_seconds / 4
        elif(rhythmic_value == 'eighth'):
            return self.length_of_quarter_in_seconds / 2
        elif(rhythmic_value == 'quarter'):
            return self.length_of_quarter_in_seconds * 1
        elif(rhythmic_value == 'half'):
            return self.length_of_quarter_in_seconds * 2
        elif(rhythmic_value == 'whole'):
            return self.length_of_quarter_in_seconds * 4
        return