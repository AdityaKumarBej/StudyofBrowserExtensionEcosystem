import json
import csv
from collections import OrderedDict

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)

    if isinstance(data, list):
        keys = set().union(*(d.keys() for d in data))
    else:
        keys = data.keys()
        data = [data]

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
if __name__ == "__main__":


    json_file = "../datasets/firefox/name_and_id_mapping.json"
    csv_file = "../datasets/firefox/name_and_id_mapping.csv"

    try:
        json_to_csv(json_file, csv_file)
        print(f"JSON file '{json_file}' has been successfully converted to CSV file '{csv_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
