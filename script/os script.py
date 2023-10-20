import os
import shutil

# Dictionary for month abbreviations
month_list = {
    "JANUARY"   : "01",
    "FEBRUARY"  : "02",
    "MARCH"     : "03",
    "APRIL"     : "04",
    "MAY"       : "05",
    "JUNE"      : "06",
    "JULY"      : "07",
    "AUGUST"    : "08",
    "SEPTEMBER" : "09",
    "OCTOBER"   : "10",
    "NOVEMBER"  : "11",
    "DECEMBER"  : "12"
}

def create_processed_directory(source_dir):
    processed_dir = os.path.join(source_dir, 'processed')
    json_dir      = os.path.join(processed_dir, 'json')
    csv_dir       = os.path.join(processed_dir, 'csv')
    
    clean_csv_dir  = os.path.join(csv_dir, 'cleaned')
    merged_csv_dir = os.path.join(csv_dir, 'merged')
    visual_csv_dir = os.path.join(csv_dir, 'visual')

    # Create the 'processed' directory and its subdirectories
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(clean_csv_dir, exist_ok=True)
    os.makedirs(merged_csv_dir, exist_ok=True)
    os.makedirs(visual_csv_dir, exist_ok=True)

    print('1) Create directory to store processed files.')



def main():
    
    # Relative source directory (one directory above)
    source_dir = os.path.join(os.path.dirname(os.getcwd()))
    
    # Create the 'processed' directory structure
    create_processed_directory(source_dir)

    # Update destination_dir to point to the 'Json' folder inside the 'processed' directory
    destination_dir = os.path.join(source_dir, 'processed', 'json')


    year_list = range(2014, 2024)
    file_count = 0

    try:
        for year in year_list:
            year_folder = os.path.join(source_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_folder):
                
                
                # Loop through months and rename JSON files
                for month_name, month_num in month_list.items():
                    
                    # variables to identify filenames and paths.
                    json_filename = f'{year}_{month_name}.json'
                    new_json_filename = f'{year}_{month_num}.json'
                    json_file_path = os.path.join(year_folder, json_filename)

                    # Check if the JSON file exists
                    if os.path.exists(json_file_path):
                        
                        try:
                            # Copy the file to the destination directory
                            destination_path = os.path.join(destination_dir, new_json_filename)
                            shutil.copy(json_file_path, destination_path)
                            file_count += 1

                        except Exception as e:
                            print(f'Error while processing {json_filename}: {str(e)}')

        print(f"2) Total number of Json files renamed: {file_count}")

    except Exception as e:
        print(f'Error in the main script: {str(e)}')

if __name__ == "__main__":
    main()
