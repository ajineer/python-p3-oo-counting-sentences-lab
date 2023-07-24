#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, _value):
    if(isinstance(_value, str)):
      self._value = _value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)

  def is_sentence(self):
    if(self.value[len(self.value)-1] == "."):
      return True
    else:
      return False

  def is_question(self):
    if(self.value[len(self.value)-1] == "?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if(self.value[len(self.value)-1] == "!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    self.count = 0
    self.value = self.value.replace('?','.')
    self.value = self.value.replace('!','.')
    sentArr = self.value.split('.')
    for sent in sentArr:
      if(len(sent) > 0):
        self.count +=1
    return self.count
  
# simple_string = MyString("one. two. three.")
# empty_string = MyString("")
# complex_string = MyString("This, well, is a sentence. This is Too!! And so is this, I think? Woo..")
# print(simple_string.count_sentences())
# print(empty_string.count_sentences())
# print(complex_string.count_sentences())