import os
import shutil
from datetime import datetime
def organize_files(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        if file_name.endswith(".jpg") and file_name.startswith("IMG_"):
            try:
                file_path = os.path.join(folder_path, file_name)
                date_str = file_name.split("_")[1]  # Extract YYYYMMDD
                date = datetime.strptime(date_str, "%Y%m%d")
                month_folder = date.strftime("%Y_%B")  # Include year in folder name
                month_folder_path = os.path.join(folder_path, month_folder)
                if not os.path.exists(month_folder_path):
                    os.makedirs(month_folder_path)
                shutil.move(file_path, os.path.join(month_folder_path, file_name))
            except Exception as e:
                print(f"Failed to move file {file_name}: {e}")

# Replace 'folder_path' with the path to the folder containing the files
folder_path = "C:\\Users\\anujm\\OneDrive\\Desktop\\organizer\\photo"
organize_files(folder_path)
