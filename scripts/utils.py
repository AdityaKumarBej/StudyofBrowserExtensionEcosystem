import json
import os
import csv

# Define the path to the input JSON file
input_file = './datasets/firefox/myjsonfile_1_100.json';
output_dir = '/Users/adityabej/Desktop/Classes/Winter 23/Security/Project/ExtAnalysis-v.1.0.5/downloaded_firefox/set1'

# Load the JSON data from the file
with open(input_file, 'r') as f:
    data = json.load(f)

# Count the number of JSON objects in the array
count = len(data)

# Print the count


# for inner_array in data:
#     for item in inner_array:
#         if "current_version" in item:
#             for inside in item["current_version"]:
#                 if "files" in inside:
#                     print(inside.files)
                
               

for inner_array in data:
    # Iterate over the inner array
    for item in inner_array:
        # Access the nested keys to get the URL value
        url = item['current_version']['files'][0]['url']
        # Print the URL value
        #print(url)
                    
           



#print(count)
#current_verison -> files[0]['url']


# # Specify the directory path
# dir_path = './datasets/chrome/100k_extension_set'

# # List all files in the directory
# file_names = [
#     os.path.splitext(f)[0] for f in os.listdir(dir_path)
#     if os.path.isfile(os.path.join(dir_path, f))
# ]

# # Write the file names to a JSON file
# with open('file_names.json', 'w') as json_file:
#     json.dump({"file_names": file_names}, json_file)

# print("File names written to JSON file.")


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


folder_path = "datasets/chrome/100k_extension_set"
output_csv_file = "datasets/chrome/post_presentation/100k_extension_set.csv"

json_data = read_json_files(folder_path)
headers = extract_headers(json_data)
# write_csv_file(output_csv_file, json_data, headers)


import multiprocessing

max_workers = multiprocessing.cpu_count()
print(f"Max workers: {max_workers}")
