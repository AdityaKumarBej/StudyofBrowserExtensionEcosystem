import csv
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def make_api_call(row):
    # Extract the necessary information from the row
    # (e.g., an ID or data point needed for the API call)
    #print("checking row", row[0])
    extension_id = row[0]
    #print("the extension id is ", extension_id)
    # Make the API call
    modified_api_url = "https://chrome.google.com/webstore/detail/" + extension_id
    response = requests.get(modified_api_url)

    # Extract the data you want from the response
    # result = response.json()['desired_data']
    if response.status_code == 200:
        return row + ["active"]
    else:
        return row + ["expired"]
    # Return the original row with the API result appended
    # return row + [result]

def process_csv(input_file, output_file, max_workers=10):
    # Read the input CSV file
    count1 = 1
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Get the header row
        rows = list(reader)  # Get the rest of the rows
    
    #print("cehcking rows", rows)
    # Add a column to the header for the API results
    header.append('api_result')

    # Create a ThreadPoolExecutor to parallelize the API calls
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit the API calls for each row and store the resulting Future objects
        futures = [executor.submit(make_api_call, row) for row in rows]

        # Collect the results as they become available
        processed_rows = []
        for future in as_completed(futures):
            print("the count is ", count1)
            count1 += 1
            processed_rows.append(future.result())

    # Write the results to a new CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(processed_rows)

input_file =  "../datasets/chrome/post_presentation/100k_extension_set.csv"
output_file = "../datasets/chrome/post_presentation/output.csv"
process_csv(input_file, output_file)