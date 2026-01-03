def read_file(old_file):
    '''
    Docstring for read_file
    
    :param old_file: Read file to be fixed
    '''
    with open(old_file, "r") as f:
        full_str = f.read()
        return full_str

def make_upper(full_str): # uses a flag based system to capitalize letters after punctuation
    '''
    Docstring for make_upper
    
    :param full_str: String returned from read_file, to be fixed
    '''
    capitalize_next = True # starts as true to capitalize first letter in the file, handled in the elif statement
    fixed = [] # build the file content in array
    for value in full_str:
        if value in ("?", ".", "!"): 
            capitalize_next = True
        elif capitalize_next and value.isalpha():
            value = value.capitalize()
            capitalize_next = False      
        fixed.append(value)
    fixed_content = "".join(fixed)
    return fixed_content
 

def write_to_file(fixed_content, newfile):
    '''
    Docstring for write_to_file
    
    :param fixed_content: Fixed content assigned to this variable
    :param newfile: Newly created file
    '''
    with open(newfile, "w") as f:
        f.write(fixed_content)
        
def capitalize(old_file, newfile): 
    '''
    Docstring for capitalize
    
    :param old_file: File to be fixed
    :param newfile: Newly created file
    
    The script's orchestrator
    '''
    full_str = read_file(old_file)
    joined = make_upper(full_str)
    write_to_file(joined, newfile)
    
if __name__ == "__main__":
    from sys import argv
    try:
        old_file, newfile = argv[1], argv[2]
        capitalize(old_file, newfile)
        print("Correctly capitalized.")
    except IndexError:
        print("Usage: python capitalize.py (old file name, new file name(without extension))")
        raise SystemExit(1)        
    except FileNotFoundError:
        print(f"File not found: {argv[1]}. Spelling?")
        raise SystemExit(2)
    except PermissionError:
        print(f"Permission error while operating on {argv[1]}. Try allowing access.")
        raise SystemExit(3)
        
    
            
            