import json
import csv
import os

def main():
    
    # Relative home directory (one directory above script)
    home_dir = os.path.join(os.path.dirname(os.getcwd()))

    # source_dir to point to 'Json' folder 
    source_dir = os.path.join(home_dir, 'processed', 'json')

    # destination_dir to point to 'all csv' folder
    destination_dir = os.path.join(home_dir, 'processed', 'csv','merged')

    output_file = os.path.join(destination_dir, 'merged.csv')

    year_list = range(2014, 2024)
    month_list = range(1, 13)
    file_count = 0


    # 2) Initialize extracted_data for all months
    all_extracted_data = []

    # 3) Loop through 10 year
    for year in year_list:
        # 4) Loop through 12 monthly files
        for month in month_list:
            
            # Generate the filename for each month
            input_filename = os.path.join(source_dir, f'{year:04d}_{month:02d}.json')
            
            try:
                with open(input_filename, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
            except FileNotFoundError:
                continue

            file_count+= 1
            
            # Extract relevant "placeVisit" data from the JSON
            extracted_data = []
            for entry in data.get('timelineObjects', []):
                if 'placeVisit' in entry:
                    place_visit     = entry['placeVisit']
                    latitude_str = place_visit['location'].get('latitudeE7', '')
                    if latitude_str:
                            latitude = float(latitude_str) / 1e7
                    longitude_str = place_visit['location'].get('longitudeE7', '')
                    if longitude_str:
                            longitude = float(longitude_str) / 1e7
                    place_address   = place_visit['location'].get('address', '')
                    place_name      = place_visit['location'].get('name', '')
                    place_confidence = place_visit.get('placeConfidence', '')
                    year_month      = f'{year:04d}-{month:02d}'


                    # Check if placeAddress is not empty before adding the row
                    if place_address:
                        extracted_row = {
                            'latitude'  : latitude,
                            'longitude' : longitude,
                            'yearMonth' : year_month, 
                            'startTimestamp': place_visit['duration']['startTimestamp'],
                            'endTimestamp': place_visit['duration']['endTimestamp'],
                            'placeAddress': place_address,
                            'placeName': place_name,
                            'placeConfidence': place_confidence,
                            # Add more keys as needed
                        }
                        extracted_data.append(extracted_row)
            
            # Append extracted data for this month to all_extracted_data
            all_extracted_data.extend(extracted_data)

        # Write all extracted "placeVisit" data to a single CSV file
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['latitude', 'longitude', 'yearMonth', 'startTimestamp',  'endTimestamp', 'placeAddress', 'placeName', 'placeConfidence']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()  # Write CSV header
            writer.writerows(all_extracted_data)  # Write all extracted data rows

        print(f"PlaceVisit data from year: '{year}' added")
    print(f"'{file_count}' Json files have been tabulated into merged.csv")
if __name__ == "__main__":
    main()
