from django.db import models

# Create your models here.
class PalindromeModel(models.Model):
  string = models.CharField(max_length=100)
  isPalindrome = models.BooleanField(default=False)
  added_on = models.DateField(auto_now=True)
