Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

  # [assignment] Add your code here
def find_anagram(word='',anagram=''):
    return sorted(word) ==sorted(anagram)

word= "hello"
anagram= "check"
print(find_anagram(word,anagram))
    

word="below"
anagram="elbow"
print(find_anagram(word,anagram))
