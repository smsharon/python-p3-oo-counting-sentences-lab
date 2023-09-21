#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value = ""):
    self._value = ""
    self.value = value
  def get_value(self):
    return self._value
  def set_value(self, value):
    if type(value) == str:
      self._value = value 
    else:
      print("The value must be a string.")  
  value = property(get_value, set_value)       

    
    
  def is_sentence(self):
        return True if  self._value.endswith('.') else False  
  def is_question(self):
            return True if  self._value.endswith('?') else False 
  def is_exclamation(self):
              return True if  self._value.endswith('!') else False
  def count_sentences(self):
    sentences = re.split(r'[.!?]', self._value)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)            
  
work = MyString()
#print(work.value)
print(work.count_sentences())
#work.value = "please work"
#print(work.value)
#work.value = 89
#print (work.value)
#work.value = "This is a string! It has three sentences. Right?"
#print(work.count_sentences())