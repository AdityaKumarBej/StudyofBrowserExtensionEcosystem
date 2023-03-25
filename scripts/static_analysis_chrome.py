import os
import zipfile
import struct
from pathlib import Path
from io import BytesIO
import crx_unpack
import re
import core.core as core
import core.intel as intel
import core.virustotal as virustotal
import socket
import core.ip2country as ip2country
from bs4 import BeautifulSoup
import json
import csv
import time
import threading
import concurrent.futures


def extract_crx(ext_path, extract_dir):
    analyze_extracted_crx(ext_path, extract_dir)


def analyze_extracted_crx(ext_path, extract_dir):
    zip_contents = zipfile.ZipFile(ext_path, 'r')
    parts = str(ext_path).split('/')
    crx_file_name = parts[1:][0]
    print("the crx file extracted is", crx_file_name)
    zip_contents.extractall(extract_dir + "/" + crx_file_name)



    #get all files and store for further analysis

    html_files = []
    js_files = []
    json_files = []
    css_files = []
    static_files = []
    other_files = [] # File extensions that are not listed above

    for root, dirs, files in os.walk(extract_dir + "/" + crx_file_name):
        #print("checking files", files)
        for file in files:
            #print("subfiles", file)
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, extract_dir + "/" + crx_file_name)
            fname = file
            file = file.lower()
            if file.endswith(('.html', '.htm')):
                html_files.append(filepath)
                #core.report['files']['html'].append({fname : relpath})
            elif file.endswith('.js'):
                js_files.append(filepath)
                #core.report['files']['js'].append({fname : relpath})
            elif file.endswith('.json'):
                json_files.append(filepath)
                #core.report['files']['json'].append({fname : relpath})
            elif file.endswith('.css'):
                css_files.append(filepath)
                #core.report['files']['css'].append({fname : relpath})
            elif file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.svg', '.gif')):
                #core.report['files']['static'].append({fname : relpath})
                static_files.append(filepath)
            else:
                #core.report['files']['other'].append({fname : relpath})
                other_files.append(filepath)
    
    #print("checking js files", js_files)

    urls = []
    domains = []
    btc_addressess = []
    emails = []
    ipv4 = []
    ipv6 = []
    base64 = []
    comments = []

    for allfiles in (js_files, html_files, json_files, css_files):
        for file in allfiles:
            try:
                cnt = open(file, 'r', encoding="utf8")
                contents = cnt.read()
                relpath = os.path.relpath(file, extract_dir  + "/" + crx_file_name)
                #core.updatelog('Extracting intels from: ' + file)
                intels = intel.extract(contents, relpath)             

                ## Parse the intels and add them to result
                found_urls = intels['urls']
                found_mail = intels['mails']
                found_btcs = intels['btc']
                found_ipv4 = intels['ipv4']
                found_ipv6 = intels['ipv6']
                found_b64s = intels['base64']
                # found_cmnt = intels['comments']

                for u in found_urls:
                    urls.append(u)
                for b in found_btcs:
                    btc_addressess.append(b)
                for m in found_mail:
                    emails.append(m)
                for i in found_ipv4:
                    ipv4.append(i)
                for i in found_ipv6:
                    ipv6.append(i)
                for b in found_b64s:
                    base64.append(b)
                # for c in found_cmnt:
                #     comments.append(c)


            except Exception as e:
                print('Skipped reading file: {0} -- Error: {1}'.format(file, str(e)))

    #print("checking urls", urls)

    #let us perform a virustotal scan on the domains extracted



    for url in urls:
        domain = re.findall('^(?:https?:\/\/)?(?:[^@\/\\n]+@)?(?:www\.)?([^:\/?\\n]+)', url['url'])[0]
        url['domain'] = domain
        domains.append(domain)
    
    #print("the urls are", urls)
    #print("the domains are", domains)
    #print("the btc_addressess are", btc_addressess)
    #print("the email ids are", found_mail)
    #print("the ipv4 are ", ipv4)
    



    #get the count of external javascript files in manifest.json

    manifest_path = os.path.join(extract_dir + "/" + crx_file_name, "manifest.json")
    #print("the manifest path is", manifest_path)
   

    with open(manifest_path, "r") as manifest_file:
        manifest_data = json.load(manifest_file)
    
    external_js_count = 0
    name_of_extension = manifest_data["name"]


    if "content_scripts" in manifest_data:
        for content_script in manifest_data["content_scripts"]:
            if "js" in content_script:
                external_js_count += len(content_script["js"])

    #get the count of external js files in .html files
    #print("the count of external js files are - 1 ", external_js_count)

    
    extension_path = Path(extract_dir + "/" + crx_file_name)
    #print("checking extension path", extension_path)
    for html_file in extension_path.glob("**/*.html"):
        with open(html_file, "r") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
        external_js_count += len(soup.find_all("script", src=True))

    
    print("the name of the extension analysed is ---- ", name_of_extension)
    print("the total number of email ids are", len(found_mail)) #we can use scamalytics to see if email addresses has been flagged in their database
    print("the total number of domains are ", len(domains)) #we can use virustotal to identify if this is malicous
    print("the total number of ipv4 are ", len(ipv4))   #again, virustotal
    print("the total number of ipv6 are ", len(ipv6)) #again, virustotal
    #print("the total number of comments are ", len(comments)) #something like profanity filter analysis
    print("the total number of btc addresses are ", len(btc_addressess))
    print("the count of external js files are", external_js_count) #estlint

    new_csv_row = [name_of_extension, len(domains), len(found_mail), len(ipv4), len(ipv6), "na", len(btc_addressess), (external_js_count), crx_file_name]
    with open('result.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_csv_row)
    
    print("Data appended to the csv")
    
    # if virustotal.pub_vt == []:
 
    #     print('Starting virustotal analysis of domains. [SLOW MODE]')
    #     virustotal_scans = virustotal.domain_batch_scan(set(domains))

    # for domain in set(domains):
    #     #print('getting virustotal Scan results for domain: ' + domain)
    #     if virustotal.pub_vt != []:
    #         # the faster scan!
    #         virustotal_report = virustotal.scan_domain(domain)
    #         if not virustotal_report[0]:
    #             print('Error getting virustotal result... Error: ' + virustotal_report[1])
    #             domain_vt = {"error":"Either rate limited or something else went wrong while getting domain report from virustotal"}
    #         else:
    #             print('Virustotal result successfully acquired!')
    #             domain_vt = virustotal_report[1]
    #     else:
    #         domain_vt = virustotal_scans[domain][1]
    #         print('Virustotal result successfully acquired!')
            
    #     domainarr = {"name":domain,  "virustotal":domain_vt}
        #print("checking vt", domain_vt)
    
    #print("results of virustotal", virustotal_scans)
    #performing virus total scans



def extract_all_crx_files(crx_folder, output_base_dir):


    crx_folder_path = Path(crx_folder)
    count = 1
    for crx_file in crx_folder_path.glob("*.crx"):
        try:

            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = list(executor.map(extract_crx(crx_file, output_base_dir)))

            count += 1
            print("done with ", count , " file ")
            print(f"Successfully extracted {crx_file} to {output_base_dir}")
        except Exception as e:
            print(f"Failed to extract {crx_file}: {e}")


# Example usage
#crx_folder = './downloaded'
crx_folder = './downloaded_latest_chrome'
output_base_dir = './extracted_latest_chrome'


python_file = 'deleted_files.py'
os.system(f"python3 {python_file}")
extract_all_crx_files(crx_folder, output_base_dir)

# def my_f():
#     print("starting again ------------------------------------------- ")
#     os.system(f"python3 {python_file}")
#     extract_all_crx_files(crx_folder, output_base_dir)

# if __name__ == "__main__":
#     while True:
#         my_f()
#         time.sleep(120)  # Wait for 2 minutes (120 seconds) before running again