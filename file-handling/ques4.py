def line_wise_reverse(inputfile, outputfile):

    input_file = open(inputfile,'r')
    output_file = open(outputfile,'w')

    for line in input_file:
        str1, str2 = map(str, line.strip().split())

        str1, str2 = str1[::-1], str2[::-1]

        

        output_file.write(f"{str2}\t{str1}\n")
    
    
    input_file.close()
    output_file.close()

    print("Processing done.")




line_wise_reverse("file-handling/input.txt","file-handling/output.txt")


