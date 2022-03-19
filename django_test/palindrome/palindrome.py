import re

class Palindrome:
  def palindrome(self, string:str):
    return ''.join(reversed(string)) == string

  def formatString(self, string:str):
    if string == '':
      return ''
    string = re.sub(r'[^\w\s]', '', string)
    string = string.replace(' ', '').lower()
    return string

  def processFile(self, file):
    result = {}
    chunks = file.chunks()
    for chunk in chunks:
      strings = chunk.decode('utf-8').split('\n')
      for string in strings:
        f_string = self.formatString(string)
        result[string] = self.palindrome(f_string)
    return result