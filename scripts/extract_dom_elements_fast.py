import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import os
import pandas as pd

def make_api_call(row):
    # Extract the necessary information from the row
    # (e.g., an ID or data point needed for the API call)
    extension_id = row[0]
    #print("the name is",row[1])
    # span ID for rating and user count field
    span_id_rating = "bhAbjd"
    span_id_usercount = "e-f-ih"

    #print("the extension id is ", extension_id)
    # Make the API call
    modified_api_url = "https://chrome.google.com/webstore/detail/" + extension_id
    response = requests.get(modified_api_url)

    # Extract the data you want from the response
    # result = response.json()['desired_data']
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
     
        span_tag_rating = soup.find('span', {'class': span_id_rating})
        span_tag_usercount = soup.find('span', {'class': span_id_usercount})
        span_value_rating = span_tag_rating.text.replace("(","").replace(")", "") if span_tag_rating else None  
        span_tag_usercount =  span_tag_usercount.text.split("+")[0] if span_tag_usercount else None  

        return row + [span_tag_usercount, span_value_rating]
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
    header.append('user_count')
    header.append('rating_count')
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

input_file =  "../datasets/chrome/post_presentation/final_chrome_extensions.csv"
output_file = "../datasets/chrome/post_presentation/final_chrome_extensions_result.csv"
process_csv(input_file, output_file)