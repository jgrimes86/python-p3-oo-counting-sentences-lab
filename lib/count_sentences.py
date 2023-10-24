#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value
    
    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
    
    def count_sentences(self):
        if len(self.value) == 0:
            return 0
        else:
            no_questions = self.value.replace("!", ".")
            no_exclamations = no_questions.replace("?", ".")
            sentence_list = no_exclamations.split(". ")
            return len(sentence_list)


