def get_final_line(filename):

    with open(filename,'r') as f:
        p = f.readlines()[-1]
        return p
    


get_final_line("notes.txt")