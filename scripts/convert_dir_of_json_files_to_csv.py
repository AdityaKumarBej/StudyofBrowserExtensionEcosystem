import json
import csv

# Specify the input JSON file and output CSV file paths
input_file = '../datasets/firefox/only_name_and_permission_batches_firefox/batch6_mozilla.json'
output_file = '../datasets/firefox/only_name_and_permission_batches_firefox/output6.csv'

# Read the JSON file
with open(input_file, 'r') as json_file:
    json_array = json.load(json_file)

# Extract the header fields (keys) from the first JSON object
header_fields = list(json_array[0].keys())

# Write the JSON data to the CSV file
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=header_fields)
    csv_writer.writeheader()
    for json_data in json_array:
        csv_writer.writerow(json_data)

print("The JSON array in the file has been successfully converted to a CSV file.")