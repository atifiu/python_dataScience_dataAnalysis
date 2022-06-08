languages = ["Java", "C++", "Python", "Javascript", "Julia", "Rust"]
for lang in languages[:]:
    languages.remove(lang)
    print(languages)


print(languages)

list1 = [['Apple', 'Orange', 'Mangoes']]
for index, value in enumerate(list1):
  print(index+1, value)

capitals = [[['india', 'uk', 'usa']], [['delhi', 'london', 'washington']]]
result = []
result = [val.upper()for sub1 in capitals for sub2 in sub1 for val in sub2]
print(result)

import os
print(os.environ["PYTHONSTARTUP"])