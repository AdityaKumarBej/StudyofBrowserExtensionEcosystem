import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import os
import pandas as pd

def fetch_request_status(extension_id, span_id_rating, span_id_usercount):
    try:
        modified_api_url = "https://chrome.google.com/webstore/detail/" + extension_id
        # print("the modified api url is", modified_api_url)
        response = requests.get(modified_api_url)
        if response.status_code == 200:
            status = "available"
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            title_tag = soup.find('title')
            title = title_tag.text if title_tag else None
            print("the title is ", title)
            return (extension_id, status)     #ADD .json to this extension_id
        else:
            return (extension_id, "expired", None)
    except Exception as e:
        return (extension_id, None, None)


def get_request_status(api_urls, span_id_rating,span_id_user_count, max_workers=20):
    count1 = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_request_status, url, span_id_rating, span_id_user_count) for url in api_urls]
        results = []
        for future in as_completed(futures):
            print("the count is", count1)
            count1 += 1
            result = future.result()
            results.append(result)
    return results


def write_to_csv(output_file, data, headers):
    print("the data is ", data)
    print("the headers is ", headers)
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)


def get_data_from_csv(csv_file_name, header_name, n_rows):
    result = []
    print("the csv file name is ", csv_file_name)
    with open(csv_file_name, "r", newline="", encoding="utf-8") as csvfile:        
        
        reader = csv.DictReader(csvfile)
        
        for index, row in enumerate(reader):
            if index >= n_rows:
                break

            result.append(row[header_name])
            
    return result

def main():
    # Specify the inout and output CSV file
    output_csv_file = "../datasets/chrome/post_presentation/expired_extensions.csv"
    input_csv_file =  "../datasets/chrome/post_presentation/100k_extension_set.csv"
    # span ID for rating and user count field
    span_id_rating = "bhAbjd"
    span_id_user_count = "e-f-ih"

    # Replace this with the actual list of API URLs
    api_urls = get_data_from_csv(input_csv_file, "extension_id", 797)

    print("the final api_urls are", api_urls)


    results = get_request_status(api_urls, span_id_rating, span_id_user_count, max_workers=20)

    headers = ["extension_id", "status"]
    write_to_csv(output_csv_file, results, headers)


main()