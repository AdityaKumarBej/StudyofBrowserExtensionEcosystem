import json

# Define the path to the input and output JSON files
input_file = './datasets/chrome/batched_extension_set/batch_103752_modified.json'
output_file = './datasets/chrome/batched_extension_set/batch_103752_modified.json'

# input_file = './test_set/test1.json'
# output_file = './test_set/test1.json'

# Define the key to count
count_key = 'permissions'

# Load the JSON data from the input file
with open(input_file) as f:
    data = json.load(f)

# Iterate through each JSON object in the array
for obj in data:
    # Count the number of values in the desired key
    count = len(obj[count_key])
    # Create a new entry in the JSON object with the count value
    obj['permission_count'] = count

# Write the modified list of JSON objects to a new JSON file
with open(output_file, 'w') as f:
    json.dump(data, f)
