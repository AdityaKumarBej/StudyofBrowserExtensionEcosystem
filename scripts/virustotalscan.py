import requests
import time
import json

# Set your API key here
# API_KEY = '9bac36e9b2ec6231f6bf1fae6965636e05bccf437ce97d38573a964065c04027' # my ucd
# API_KEY = 'af0ce1f122ab3ae8e9372a2d9dee76401cbae058cf30be74e845c2afdc81263b' # my gmail
# API_KEY = 'ea2a18694c1c76283c80f8567e86b1d3cafa39c5882cb8d5480d1d3c4a1fbfe6' # akbej
# API_KEY = 'd834aa174bda963b364aa595ac6a95322a47e36599eeaa31f0616ef23051f288' # adi 1997 vt acc
# API_KEY = '1e9475b8d610ba6db9dcf99fe52314b725ec830f58dd2f779e15d024650f688c' # adi 1991 vt acc
# API_KEY = '52e169dde3f27b9f7ae02d36bc5c7f3107b12d362c58e29ad4bf16b34885ad10' # c p
API_KEY = '460d6f941d11d5a483a801026abcfd846b705b10d9a50f5e033ee46eea3a4549' # c p davis

# Set the URL of the VirusTotal Domain Report API
VT_DOMAIN_REPORT_API = 'https://www.virustotal.com/vtapi/v2/domain/report?'

# Set the name of the file containing the list of URLs
# URL_FILE = '../dataset 2.txt'
URL_FILE = '/Users/shivani/Downloads/adi_static_reports/adi_firefox_avast.txt'

# Read the list of URLs from the file
with open(URL_FILE) as f:
    urls = [line.strip() for line in f.readlines()]

# print(urls)
#https://www.virustotal.com/vtapi/v2/domain/report?apikey=9bac36e9b2ec6231f6bf1fae6965636e05bccf437ce97d38573a964065c04027&domain=hart-dev.com

# Opening JSON file
already_scanned_urls = open('/Users/shivani/Downloads/fiddler_domains_collected/mozilla/vt_report_firefox.json')

# returns JSON object as 
# a dictionary
scanned_data = json.load(already_scanned_urls)

present_count = 0
safe_count = 0
malicious_count = 0
unsure_count = 0

headers = {
    'x-apikey': API_KEY
}

params = {
    'limit': len(urls),
    'fields': 'last_analysis_stats,detected_urls'
}

# Iterate through each URL and call the VirusTotal Domain Report API
for url in urls:
    
    if url in scanned_data:
        print(f"{url}:{scanned_data[url]}")
        present_count += 1
    else:
        myapi = f'https://www.virustotal.com/api/v3/domains/{url}'
        response = requests.get(myapi, headers=headers, params=params)

        if response.status_code == 200 or response.status_code == 204:
            # print(response.json()['data']['attributes']["last_analysis_stats"]["malicious"])
            if response.json()['data']['attributes']["last_analysis_stats"]["malicious"]>0:
                print(f"{url}:malicious")
                malicious_count += 1
            elif response.json()['data']['attributes']["reputation"]<0:
                print(f"{url}:malicious")
                malicious_count += 1
            else:
                myapi = VT_DOMAIN_REPORT_API+'apikey='+API_KEY+'&domain='+url
                response = requests.get(myapi)
                if response.status_code == 200 or response.status_code == 204:
                    if("Webutation domain info" in response.json()):
                        if response.json()["Webutation domain info"]["Verdict"] == "malicious":
                            print(f"{url}:malicious")
                            malicious_count += 1
                        elif response.json()["Webutation domain info"]["Verdict"] == "safe":
                            print(f"{url}:safe")
                            safe_count += 1
                        else:
                            print(f"{url}:unsure")
                            unsure_count += 1
                    else:
                        print(f'{url}:safe')
                        safe_count += 1
                else:
                    print(f'{url}: {response.status_code} Error calling Webutation')
        else:
            print(f'{url}: {response.status_code} Error calling Domain Report')
        time.sleep(20)

# print(present_count)
print(f'safe_count:{safe_count}')
print(f'malicious_count:{malicious_count}')
print(f'unsure:{unsure_count}')
