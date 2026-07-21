input_file = open("file-handling/input.txt",'r')
output_file = open("file-handling/output.txt",'w')

total = 0

for line in input_file:

    num1, num2 = map(int, line.strip().split())

    product = num1 * num2

    total += product

    output_file.write(f"{num1}\t{num2}\t{product}\n")

output_file.write(f"Total\t{total}\n")

input_file.close()
output_file.close()

print("Processing completed. Check result.txt")