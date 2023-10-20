import pandas as pd
import re
import os

#-------------------------------------------------------------#
# Error 2: Replace  symbols from "placeName" column 
#-------------------------------------------------------------#
def remove_symbols_placeName(placeNameText):
    symbols_name_to_replace = {
        '®': '',
        'é': 'e',        
        '’' : '',
        }
    symbols_name_removed_count = 0
    
    for symbol, replacement in symbols_name_to_replace.items():
        if symbol in placeNameText:
            count = placeNameText.count(symbol)
            symbols_name_removed_count += count  # Increment the count for each symbol found
            placeNameText = placeNameText.replace(symbol, replacement)
    return placeNameText, symbols_name_removed_count


#-------------------------------------------------------------#
# Error 3: Replace Urdu symbols from "placeAddress" column 
#-------------------------------------------------------------#








def main():
    
    # Relative home directory (one directory above script)
    home_dir = os.path.join(os.path.dirname(os.getcwd()))

    # Specifying source and destination directory.
    source_dir = os.path.join(home_dir, 'processed', 'csv','merged')
    destination_dir = os.path.join(home_dir, 'processed', 'csv','cleaned')

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

    # Apply the remove_symbols_placeName function to the "placeName" column
    df['placeName'], symbols_name_removed_count = zip(*df['placeName'].apply(remove_symbols_placeName))
    total_symbols_name_removed_count = sum(symbols_name_removed_count)
    print(f"2) Total number of rows changed in 'placeName' column: {total_symbols_name_removed_count}")


            #-------------------------------------------------------------#
            # Error 3: Todo.
            #-------------------------------------------------------------#



    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"3) Clean file has been created.")

if __name__ == "__main__":
    main()
