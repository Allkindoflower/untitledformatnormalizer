def read(old_file):
    with open(old_file) as f: 
        full_str = f.read()
        return full_str
    
def remove(full_str):
    normalized = " ".join(full_str.split())                                                            
    return normalized
           
def write_new(normalized, new_file):
    with open(new_file, "w") as f:
        f.write(normalized)
        
def remove_double_spaces(old_file, new_file):
    full_str = read(old_file)
    normalized = remove(full_str)
    write_new(normalized, new_file)
    
    
if __name__ == "__main__":
    from sys import argv
    file_to_fix, fixed_file = argv[1], argv[2]
    try:
        remove_double_spaces(file_to_fix, fixed_file)
        print("Removed double spaces.")
    except FileNotFoundError:
        print(f"File not found, {argv[1]}. Spelling?")
        raise SystemExit(1)
    except IndexError:
        print("No arguments provided. Usage: remove_double_spaces(file-to-fix, fixed_file-name)")
        raise SystemExit(2)
    except PermissionError:
        print(f"Permission denied while removing spaces: {file_to_fix}. Try allowing access?")
        raise SystemExit(3)