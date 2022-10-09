from django.shortcuts import render

from django.http import HttpResponse
from .forms import CaesarCipherForm
import string


def index(request):
    return HttpResponse("Hello, world. You're at the cryptography index.")

#def caesar_cipher(request):

#    form = CaesarCipherForm()
#    key = 158
#    key_mod = 158%26
#    text = 'salut'
#    new_text= ""
#    print("hello")
#    print(key, text)
    
    # position dans l'alphabet
#    for i in range(len(text)):
#        letter = text[i]
#        new_letter = string.ascii_lowercase[string.ascii_lowercase.index(letter)+key_mod]
#        new_text = new_text + new_letter

#    return render(request, 'caesar.html', {'key': key, 'text': text, 'new_text': new_text, 'form': form})

def cipher_form(request):

    new_text = ""

    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key_field']
            text = form.cleaned_data['text_field']

            key_mod = key % 26
            print(key, text, key_mod)
            for i in range(len(text)):

                letter = text[i]
                new_letter = string.ascii_lowercase[(string.ascii_lowercase.index(letter)+key_mod)%26]
                new_text = new_text + new_letter
                print(new_letter)
                print(new_text)

    form = CaesarCipherForm()
    return render(request, 'caesar.html', {'new_text': new_text, 'form': form})