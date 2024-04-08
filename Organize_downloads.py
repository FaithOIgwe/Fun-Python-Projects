import os
import shutil

# Function to organize files
def organize_downloads_folder(downloads_folder):
    # Dictionary mapping file extensions to folder names
    file_types = {
        "Documents": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
        "Music": [".mp3", ".wav", ".flac", ".mpg"],
        "Excel": [".xlsx"],
        "PowerBI": [".pbix"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executables": [".exe", ".msi"],
        "Word Documents": [".docx"],
        "Powerpoint": [".pptx"],
        "Python Files": [".py"],
        "Text Files": [".txt"],
        "Others": []  # Default folder for other file types
    }

    # creating folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(downloads_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files
    for filename in os.listdir(downloads_folder):
        if filename != "organize_downloads.py":  # Skip this script file
            src_path = os.path.join(downloads_folder, filename)
            if os.path.isfile(src_path):
                file_ext = os.path.splitext(filename)[1].lower()
                dest_folder = None

                for folder, ext_list in file_types.items():
                    if file_ext in ext_list:
                        dest_folder = folder
                        break

                if dest_folder is None:
                    dest_folder = "Others"

                dest_path = os.path.join(downloads_folder, dest_folder, filename)
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename} --> {dest_folder}")

    print("Organizing completed.")

if __name__ == "__main__":
    downloads_folder = r"C:\Users\faith.igwe-uzor\Downloads"
    organize_downloads_folder(downloads_folder)
