import os
import shutil

#Path to the desktop folder
desktop_path = os.path.expanduser("~/Desktop")

#Dictionary containing the folder names and their corresponding file extensions
folders = {
    "Images": [".jpeg", ".jpg", ".png", "gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}

# Create the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
    # Placeholder: Add logic to move files based on their extension
    pass