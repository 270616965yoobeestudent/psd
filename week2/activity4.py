class StringManipulator:
  def find_character(self, text, character):
    return text.find(character)
  
  def count_character(self, text):
    return text.__len__()
  
  def uppercase(self, text):
    return text.upper()
  
if __name__ == "__main__":
  name = StringManipulator()
  print("Find character 'o': ", name.find_character("Johnny", "o"))
  print("Count character:", name.count_character("Johnny"))
  print("Uppercase:", name.uppercase("Johnny"))

  # __init__ method help assign value to class variables, it can reduce dupplicate work
  # such as keep sending `text` to every methods.