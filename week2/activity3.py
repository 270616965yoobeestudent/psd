class StringManipulator:
  def __init__(self, text):
    self.text = text
  
  def find_character(self, character):
    return self.text.find(character)
  
  def count_character(self):
    return self.text.__len__()
  
  def uppercase(self):
    return self.text.upper()
  
if __name__ == "__main__":
  name = StringManipulator("Johnny")
  print("Find character 'o': ", name.find_character("o"))
  print("Count character:", name.count_character())
  print("Uppercase:", name.uppercase())