import pandas as pd
import re
import os

# Function to extract city from placeAddress
def extract_city(address):

    common_cities = ['Karachi', 'North York', 'Mississauga', 'Toronto', 
                      'Elora', 'Cambridge', 'Kitchener', 'Waterloo', 
                      'Scarborough']


    # Define a list of common cities in Ontario and Karachi
    all_cities = ['Buffalo', 'Karachi', 'Montreal', 'North York',
                  'Mississauga', 'Toronto', 'Brampton', 'Fergus', 'Elora',
                  'Hamilton', 'Ottawa', 'Markham', 'Etobicoke', 'Thornhill',
                  'London', 'Milton', 'Cambridge', 'Kitchener', 'Waterloo', 
                  'Niagara Falls', 'Scarborough', 'Vaughan', 'Windsor',
                  'Richmond Hill', 'Oakville', 'Burlington', 'Greater Sudbury',
                  'Oshawa', 'Barrie', 'St. Catharines', 'Kingston', 'West Montrose',
                  'Guelph', 'Thunder Bay', 'Brantford', 'Pickering']
    
    # Iterate through the list and return the city if found in the address
    for city in common_cities:
        if city in address:
            return city
    return 'Others'  # Return 'Unknown' if no matching city found


def main():
   
     # Relative home directory (one directory above script)
    parent_dir = os.path.join(os.path.dirname(os.getcwd()))
    home_dir = os.path.join(parent_dir, 'GeoBiographyScript')

    # Specifying source and destination directory.
    source_dir = os.path.join(home_dir, 'process', 'csv','cleaned')
    destination_dir = os.path.join(home_dir, 'process', 'csv','visual')

    # Specifying input and output file.
    input_file = os.path.join(source_dir, 'cleaned.csv')
    output_file = os.path.join(destination_dir, 'visual.csv')
   
    data = pd.read_csv(input_file)

    # Extract relevant columns
    selected_columns = ['latitude', 'longitude', 'placeName', 'placeAddress']

    # Create a new DataFrame with the selected columns
    new_df = data[selected_columns].copy()  

    # Extract and format the StartDate from startTimestamp
    new_df['StartDate'] = pd.to_datetime(data['startTimestamp'], format='ISO8601', errors='coerce').dt.strftime('%d-%m-%Y')

    # Extract and map the 'City' from 'placeAddress'
    new_df['City'] = new_df['placeAddress'].apply(extract_city)
        
    # Save the cleaned DataFrame to a new CSV file
    new_df.to_csv(output_file, index=False)
    print(f"1) File ready for flourish.")

if __name__ == "__main__":
    main()
