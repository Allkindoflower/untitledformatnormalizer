from shutil import copy

    
def backup(file_to_backup):
    copy(file_to_backup, f"{file_to_backup}.bak")
      
if __name__ == "__main__":
    from sys import argv
    try:
        file_to_backup = argv[1]
        backup(file_to_backup)
        print("Backup completed.")
    except IndexError:
        print("Usage: backup(filename, backup-location e.g. content/backup.bak)")
        raise SystemExit(1)
    except PermissionError:
        print(f"Permission denied while backing up {file_to_backup}")
        raise SystemExit(2)
