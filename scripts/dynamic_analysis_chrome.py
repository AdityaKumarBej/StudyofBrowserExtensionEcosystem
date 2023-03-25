import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def analyze_extension(extension_path, output_json, chrome_driver_path=None):
    chrome_options = Options()
    # chrome_options.add_argument(f'--load-extension={extension_path}')
    chrome_options.add_extension(extension_path)
    # chrome_options.add_argument('--disable-web-security')
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--incognito')

    caps = DesiredCapabilities.CHROME.copy()
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options, desired_capabilities=caps)

    domains = set()

    try:
        # Replace 'https://example.com' with the URL you want to analyze
        driver.get('https://google.com')

        # Wait for the extension to perform its tasks
        time.sleep(10)

        logs = driver.get_log('performance')
        for log in logs:
            if 'Network.requestWillBeSent' in log['message']:
                message = json.loads(log['message'])
                url = message['message']['params']['request']['url']
                print("the url is ", url)
                domains.add(url)
                # domain = url.split("://")[-1].split("/")[0].strip()
                # print("the domain is ", domain)
                # domains.add(domain)

    finally:
        driver.quit()

    with open(output_json, 'w') as outfile:
        json.dump(list(domains), outfile)

if __name__ == "__main__":
    extension_path = '../chrome_extensions_packed/hola_chrome_extension.crx'
    output_json = '../dynamic_analysis_chrome.json'
    chrome_driver_path = '../chrome_driver_executable/chromedriver_mac64/chromedriver'

    try:
        analyze_extension(extension_path, output_json, chrome_driver_path or None)
        print(f"Domains contacted by the extension have been saved to '{output_json}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
