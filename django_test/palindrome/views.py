import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .palindrome import Palindrome
from .models import PalindromeModel

from rest_framework import viewsets

palindromeController = Palindrome()

def index(request):
  form = UploadFileForm()
  return render(request, 'palindrome/index.html', context={'form': form})

def bulk(request):
  file = None
  result = None
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    file = request.FILES['file']
    result = palindromeController.processFile(file)
  return render(request, 'palindrome/index.html', context={'form': form, "file":file, "result":result})


def checkString(request, **query_params):
  result = {}
  checkString = str(query_params['checkString'])
  result['string'] = checkString
  result['value'] = palindromeController.palindrome(checkString)
  instance = PalindromeModel(string=result['string'], isPalindrome=result['value'])
  instance.save()
  # print(instance)
  return render(request, 'palindrome/checkString.html', context={"result":result})

def palindromeHistory(request):
  # print(1)
  history = PalindromeModel.objects.all().order_by('added_on')
  print(history.values_list)
  return render(request, 'palindrome/history.html', context={"history":history.values})
