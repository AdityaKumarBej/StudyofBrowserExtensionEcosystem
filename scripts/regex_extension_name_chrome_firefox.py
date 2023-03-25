import csv
import re

def process_csv_column(input_csv, output_csv, column_name):
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + [f"{column_name}_processed"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Extract the data from the specified column
            data = row[column_name]

            # Remove special characters, spaces, and tabs, and lowercase all letters
            processed_data = re.sub(r'[^A-Za-z0-9]', '', data).lower()

            # Add the processed data as a new column and write it to the output CSV
            row[f"{column_name}_processed"] = processed_data
            writer.writerow(row)

if __name__ == "__main__":
    input_csv = '../datasets/firefox/post_presentation/firefox_extension.csv'
    output_csv = '../datasets/firefox/post_presentation/firefox_output_regex.csv'
    column_name = 'name'

    try:
        process_csv_column(input_csv, output_csv, column_name)
        print(f"Processed the input CSV file '{input_csv}' and created the output CSV file '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
