import json
import os
import csv

def read_json_files(folder_path):
    json_data = []
    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            with open(os.path.join(folder_path, file), "r") as f:
                data = json.load(f)
                file_without_extn, _= os.path.splitext(file)
                data["file_name"] = file_without_extn
                json_data.append(data)
    return json_data

def extract_headers(json_data):
    headers = set()
    for data in json_data:
        for key in data.keys():
            headers.add(key)
    return list(headers)


def write_csv_file(output_file, json_data, headers):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for data in json_data:
            csv_writer.writerow(data)


folder_path = "../datasets/firefox/post_presentation"
output_csv_file = "../datasets/firefox/post_presentation/firefox_extension.csv"

json_data = read_json_files(folder_path)
headers = extract_headers(json_data)
# write_csv_file(output_csv_file, json_data, headers)