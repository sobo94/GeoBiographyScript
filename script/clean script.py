import pandas as pd
import re
import os

#-------------------------------------------------------------#
# Error 2: Replace symbols from "placeName" column. 
#-------------------------------------------------------------#
def symbols_placeName(placeaddress_values):
    symbols = {
        '®': '',
        'é': 'e',        
        '’' : '',
        }
    count_rows = 0
    
    for symbol, replacement in symbols.items():
        if symbol in placeaddress_values:
            count = placeaddress_values.count(symbol)
            count_rows += count  # Increment the count for each symbol found
            placeaddress_values = placeaddress_values.replace(symbol, replacement)
    return placeaddress_values, count_rows


#-------------------------------------------------------------#
# Error 3: Replace Urdu symbols from "placeAddress" column 
#  - Urdu is Left to Right so the comma's causes issues.
#  - the remaining 3 are just urdu to english transalation.
#-------------------------------------------------------------#
def symbols_placeAddress(placeaddress_values):
    symbols = {
        '،' : ',',
        'راشد منہاس روڈ' : 'Rashid Minhas Road',
        'کراچی'  : 'Karachi',
        'پاکستان' : 'Pakistan',
        'karachi': 'Karachi',
        }
    count_Rows = 0
    
    for symbol, replacement in symbols.items():
        if symbol in placeaddress_values:
            count = placeaddress_values.count(symbol)
            count_Rows += count  # Increment the count for each symbol found
            placeaddress_values = placeaddress_values.replace(symbol, replacement)
    return placeaddress_values, count_Rows





def main():
    
    # Relative home directory (one directory above script)
    parent_dir = os.path.join(os.path.dirname(os.getcwd()))
    home_dir = os.path.join(parent_dir, 'GeoBiographyScript')

    # Specifying source and destination directory.
    source_dir = os.path.join(home_dir, 'process', 'csv','merged')
    destination_dir = os.path.join(home_dir, 'process', 'csv','cleaned')

    # Specifying input and output file.
    input_file = os.path.join(source_dir, 'merged.csv')
    output_file = os.path.join(destination_dir, 'cleaned.csv')

    # Read and load input csv as a dataframe.
    df = pd.read_csv(input_file)

            #-------------------------------------------------------------#
            # Error 1: Empty values "placeName" to "Residential Address"
            #-------------------------------------------------------------#
    
    df["placeName"].fillna("Residential Address", inplace=True)
    empty_rows_changed_count = len(df[df['placeName'] == 'Residential Address'])
    print(f"1) Empty rows updated 'placeName' column: {empty_rows_changed_count}")

            #-------------------------------------------------------------#
            # Error 2: Replace  symbols from "placeName" column 
            #-------------------------------------------------------------#

    df['placeName'], symbols_name_removed_count = zip(*df['placeName'].apply(symbols_placeName))
    total_symbols_name_removed_count = sum(symbols_name_removed_count)
    print(f"2) Total number of rows changed in 'placeName' column: {total_symbols_name_removed_count}")

            #-------------------------------------------------------------#
            # Error 3: Replace  symbols from "placeAddress" column 
            #-------------------------------------------------------------#
   
    # Apply function to the "placeName" column
    df['placeAddress'], symbols_address_removed_count = zip(*df['placeAddress'].apply(symbols_placeAddress))
    total_symbols_address_removed_count = sum(symbols_address_removed_count)
    print(f"4) Total number of rows changed in 'placeAddress' column: {total_symbols_address_removed_count}")


    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"3) Clean file has been created.")

if __name__ == "__main__":
    main()
