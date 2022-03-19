import os
import re
from django.test import TestCase
from .palindrome import Palindrome

palindrome = Palindrome()

cases = {
  "Anna": True,
  "Annie": False,
  "Civic": True,
  "Kayak": True,
  "Levels": False,
  "Madam": True,
  "Mom": True,
  "Noon": True,
  "Racecar": True,
  "Radar": True,
  "Redder": True,
  "Refer": True,
  "Rotator": True,
  "Rotor": True,
  "Sagas": True,
  "Solos": True,
  "Stats": True,
  "Tenet": True,
  "Wow": True,
  "Was it a cat I saw?": True,
  "Eva, can I see bees in a cave?": True,
  "A man, a plan, a canal. Panama!": True,
}

class PalindromeTestCase(TestCase):
  def test_format_string(self):
    for string in cases.keys():
      f_string = palindrome.formatString(string)
      punctuationCount = len(re.findall('[^a-zA-z]', f_string))
      self.assertEqual(punctuationCount, 0)
      
  def test_palindrome(self):
    for string, expected in cases.items():
      f_string = palindrome.formatString(string)
      check = palindrome.palindrome(f_string)
      self.assertEqual(check, expected)