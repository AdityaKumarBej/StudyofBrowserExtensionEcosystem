import json

# Define the paths to the input JSON files
file1 =  './datasets/firefox/only_name_and_permission_batches_firefox/batch6_mozilla.json'
file2 = './datasets/chrome/batched_extension_set/batch_103752_modified.json'

# Define the key to compare
compare_key = 'name'

# Load the JSON data from file1
with open(file1) as f:
    data1 = json.load(f)

# Load the JSON data from file2
with open(file2) as f:
    data2 = json.load(f)

# Create a new list to store the matching JSON objects
matches = []
common = []

# Iterate through each JSON object in data1
for obj1 in data1:
    # Get the value to compare
    value1 = obj1.get(compare_key)
    # Iterate through each JSON object in data2
    for obj2 in data2:
        # Get the value to compare
        value2 = obj2.get(compare_key)
        # If the values match, add the JSON object from data2 to the matches list

        if value1 == value2:
            #name matches, now see if their permissions count differ, if yes, make a note on the extension name only
            
            common.append(value1)
            #print("the values are ", value1 , " and " , value2)
            
            #print("the permission count in mozilla is " , obj1.get("permission_count") , " and in chrome is ", obj2.get("permission_count"))
            if obj1.get("permission_count") != obj2.get("permission_count"):
                temp = {}
                temp["name"] = value1
                temp["permissions_chrome"] = obj2.get("permissions")
                temp["permissions_firefox"] = obj1.get("permissions")
                matches.append(temp)

# Write the list of matching JSON objects to a new JSON file
# with open('result1.json', 'w') as f:
#     json.dump(matches, f)

# Load the existing JSON data from the input file
# with open('result1.json', 'r') as f:
#     existing_data = json.load(f)

# # Append the new data to the existing data
# existing_data.append(matches)

# # Write the updated data to the output file
# with open('result1.json', 'w') as f:
#     json.dump(existing_data, f)

# with open('common_extensions_chrome_firefox.json', 'w') as f:
#     json.dump(common, f)


# Load the existing JSON data from the input file
with open('common_extensions_chrome_firefox.json', 'r') as f:
    existing_data = json.load(f)

# # Append the new data to the existing data
existing_data.append(common)

# # Write the updated data to the output file
with open('common_extensions_chrome_firefox.json', 'w') as f:
    json.dump(existing_data, f)