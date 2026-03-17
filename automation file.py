import os
import shutil

base_path = os.getcwd()
projects_folder = os.path.join(base_path, "projects")

os.makedirs(projects_folder, exist_ok=True)

# EXACT filenames from your system
project_map = {
    "Calculator.py": "calculator",
    "Greeting program.py": "greeting-app",
    "guess the number.py": "guess-number-game",
    "Number Toolkit.py": "number-toolkit",
    "password checker.py": "password-checker",
    "tournament_nrr_calculator.py": "nrr-calculator",
    "university scholarship .py": "scholarship-tool",
    "p.py": "misc",
    "main.py": "misc"
}

for file_name, folder_name in project_map.items():
    old_path = os.path.join(base_path, file_name)

    if not os.path.exists(old_path):
        print(f"❌ Skipping {file_name} (not found)")
        continue

    new_folder_path = os.path.join(projects_folder, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Rename everything to main.py (clean structure)
    new_file_path = os.path.join(new_folder_path, "main.py")

    shutil.move(old_path, new_file_path)

    print(f"✅ Moved: {file_name} → {folder_name}/main.py")

print("\n🚀 All files organized successfully!")