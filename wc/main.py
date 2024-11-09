import argparse
import os 


    
def count_lines(file_name,mode):
    with open(file_name, mode,encoding = "utf-8") as file:
        return len(file.readlines())
    

def count_words(file_name,mode):
    with open (file_name, mode, encoding='utf-8') as file:
        content = file.read()
        return len(content.split())
    
def count_chars(file_name,mode):
    with open (file_name, mode, encoding='utf-8') as file:
        content = file.read()
        line_breaks = content.count('\n')  # Count line breaks
        return len(content)+line_breaks

# The problem which i was encountering was that {wc -m test.txt} was returning more than
# my commands it was because wc was counting new lines twice as in windows newline are represneted by 2 character /r/n. 

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("filename", nargs='?', default="test.txt",help="give the filename")
    parser.add_argument("--c", action="store_true", help = "Gives the size of a file.")
    parser.add_argument("--l", action="store_true", help = "Gives the number of lines in a file.")
    parser.add_argument("--w", action="store_true", help = "Gives the number of words in a file.")
    parser.add_argument("--m", action="store_true", help = "Gives the number of characters in a file.")


    args = parser.parse_args()
    
    path = args.filename 
    
    if(args.c):
        file_size = os.stat(path).st_size
        print(f"{file_size} as {path}")

    elif(args.l):
        total_line = count_lines(path,"r")
        print(f"{total_line} {path}")
        
    elif(args.w):
        total_words = count_words(path,"r")
        print(f"{total_words} {path}")

    elif(args.m):
        total_chars = count_chars(path,"r")
        print(f"{total_chars} {path}")

    else:

        total_line = count_lines(path,"r")
        print(f"{total_line}  " ,end="")

        total_words = count_words(path,"r")
        print(f"{total_words}  ", end="")

        file_size = os.stat(path).st_size
        print(f"{file_size} {path}")
            
















