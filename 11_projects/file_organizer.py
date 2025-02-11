# File Organizer Application
import os
import shutil
from datetime import datetime
from pathlib import Path
import logging

class FileOrganizer:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.setup_logging()
        
        # File type mappings
        self.type_folders = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
            'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
            'Video': ['.mp4', '.avi', '.mkv', '.mov'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
        }
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename='file_organizer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def create_folders(self):
        """Create organization folders if they don't exist"""
        for folder in self.type_folders.keys():
            folder_path = self.source_dir / folder
            if not folder_path.exists():
                folder_path.mkdir()
                logging.info(f"Created folder: {folder}")
    
    def get_file_type(self, file_extension):
        """Determine the type of file based on its extension"""
        for folder, extensions in self.type_folders.items():
            if file_extension.lower() in extensions:
                return folder
        return 'Others'
    
    def organize_files(self):
        """Organize files into appropriate folders"""
        self.create_folders()
        
        # Counter for organized files
        organized_count = 0
        
        try:
            for item in self.source_dir.iterdir():
                if item.is_file():
                    # Skip the log file
                    if item.name == 'file_organizer.log':
                        continue
                    
                    # Get file type and destination folder
                    file_type = self.get_file_type(item.suffix)
                    dest_folder = self.source_dir / file_type
                    
                    # Create 'Others' folder if needed
                    if file_type == 'Others':
                        dest_folder = self.source_dir / 'Others'
                        if not dest_folder.exists():
                            dest_folder.mkdir()
                    
                    # Move file to appropriate folder
                    try:
                        if not dest_folder.exists():
                            dest_folder.mkdir()
                        
                        # Handle duplicate files
                        dest_path = dest_folder / item.name
                        if dest_path.exists():
                            # Add timestamp to filename
                            new_name = f"{item.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{item.suffix}"
                            dest_path = dest_folder / new_name
                        
                        # Move the file
                        shutil.move(str(item), str(dest_path))
                        organized_count += 1
                        logging.info(f"Moved {item.name} to {file_type} folder")
                        
                    except Exception as e:
                        logging.error(f"Error moving {item.name}: {str(e)}")
            
            return organized_count
            
        except Exception as e:
            logging.error(f"Error organizing files: {str(e)}")
            return 0
    
    def generate_report(self):
        """Generate a report of organized files"""
        report = "File Organization Report\n"
        report += "=" * 25 + "\n\n"
        
        total_files = 0
        for folder in self.type_folders.keys():
            folder_path = self.source_dir / folder
            if folder_path.exists():
                files = list(folder_path.glob('*'))
                report += f"{folder}: {len(files)} files\n"
                total_files += len(files)
        
        # Check Others folder
        others_path = self.source_dir / 'Others'
        if others_path.exists():
            files = list(others_path.glob('*'))
            report += f"Others: {len(files)} files\n"
            total_files += len(files)
        
        report += f"\nTotal organized files: {total_files}"
        return report

def main():
    print("=== File Organizer ===")
    
    # Get directory to organize
    while True:
        directory = input("\nEnter the directory path to organize: ")
        if os.path.exists(directory):
            break
        print("Directory does not exist. Please try again.")
    
    # Create and run organizer
    organizer = FileOrganizer(directory)
    
    print("\nOrganizing files...")
    organized_count = organizer.organize_files()
    
    if organized_count > 0:
        print(f"\nSuccessfully organized {organized_count} files!")
        print("\nOrganization Report:")
        print(organizer.generate_report())
    else:
        print("\nNo files were organized. Check the log file for details.")

if __name__ == "__main__":
    main() 