import os
import shutil
def organize_files(directory):
    # Define file types and the corresponding folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Others": []
    }

    # Create folders for each category
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files into respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  # Only process files
            moved = False
            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder))
                    moved = True
                    break
            if not moved:  # If file doesn't match any category
                shutil.move(file_path, os.path.join(directory, "Others"))

    print("Files have been organized successfully!")

# Example usage: Organize files in the 'Downloads' folder
organize_files("C:/Users/HP/Downloads")