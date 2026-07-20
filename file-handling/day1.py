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
    

with open("file-handling/ques1.txt", 'r') as f:
    chunk_size = 100
    
    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size),end="***")
