import os

def commit_for_one_day(repo_path, file_name="dummy.txt", commit_message="Commit for one day"):
    os.chdir(repo_path)
    
    with open(file_name, "a") as f:
        f.write("Commit made on this day.\n")
    
    os.system(f"git add {file_name}")
    
    os.system(f'git commit -m "{commit_message}" --date="2026-01-10 12:00:00"')
    
if __name__ == "__main__":
    repo_path = "./"
    commit_for_one_day(repo_path)