# f = open("file-handling/ques1.py", 'w')
# f.write('Hello World!')

# f = open("file-handling/ques1.py", 'a')
# f.write('\nHello World')

# l = ['hi\n', 'I am Lucky\n', 'Everything is fine here\n']
# f = open("file-handling/ques1.txt", 'w')
# f.writelines(l)

# f = open("file-handling/ques1.txt",'r')
# s = f.read()
# print(s)

# its a mandatory line of code, cuz if a file has been opened, it has to be closed after all the operations are done.

# big_l = ["Hello world\n" for i in range(1000)]
# with open("file-handling/ques1.txt", 'w') as f:
#     f.writelines(big_l)
    

# with open("file-handling/ques1.txt", 'r') as f:
#     chunk_size = 100
    
#     while len(f.read(chunk_size)) > 0:
#         print(f.read(chunk_size),end="***")
#         f.read(chunk_size)

# to work with binary files we use binary mode:

# with open("file-handling/screenshot.png", 'rb') as f:
#     with open("file-handling/screenshot_copy.jpg",'wb') as wf:
#         wf.write(f.read())


# Serialization and deserialization


import json

# L = [1,2,3,4]
d = {
    "name" : "Lucky",
    "age" : 5,
    "height" : "5'6",
    "weight" : "65 kgs"
}

t = (1,2,3,4,5)

with open("file-handling/pp.json",'w') as f:
    d = json.dump(d,f)

with open("file-handling/pp.json", 'r') as rf:
    d = json.load(rf)
    print(type(d))