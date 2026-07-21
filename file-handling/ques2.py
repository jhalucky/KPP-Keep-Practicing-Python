vowel_count = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}

with open("notes.txt",'r') as file:
    for line in file:
        line = line.lower()
        for ch in line:
            if ch in vowel_count:
                vowel_count[ch] += 1


print("Vowel count: ")
print(vowel_count)