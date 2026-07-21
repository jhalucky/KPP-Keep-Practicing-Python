import pickle
import re

with open('file-handling/input.txt','r') as file:
    text = file.read().lower()

words = re.findall(r"\b[a-z]+\b", text)

freq = {}

for word in words:

    freq[word] = freq.get(word, 0) + 1

with open("word_freq.pkl","wb") as file:
    pickle.dump(freq, file)

print("Dictionary serialized successfully")

word_list = ['alice','wonder','natural']

with open("word_freq.pkl","rb") as file:
    word_dict = pickle.load(file)

print("Word counts:")
for word in word_list:
    print(f"{word} : {word_dict.get(word, 0)}")