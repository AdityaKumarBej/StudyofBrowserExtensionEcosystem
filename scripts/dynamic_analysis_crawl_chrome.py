import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the URL you want to open
url = ["https://www.youtube.com","https://www.nytimes.com","https://www.cnn.com"]

# Path to the ChromeDriver executable
chrome_driver_path = "/Users/shivani/Downloads/chromedriver_mac64/chromedriver"

# Path to the extension file
extension_path = "/Users/shivani/Downloads/extensions/chrome-malwarebytes.crx"

# Create a ChromeDriver service instance
service = Service(chrome_driver_path)

# Create a new Chrome webdriver instance with the extension
options = webdriver.ChromeOptions()
options.add_extension(extension_path)
driver = webdriver.Chrome(service=service, options=options)

# wait for the extension to get added successfully
time.sleep(20)
print("extension installed")

for each_url in url:
	# Navigate to URL
	driver.get(each_url)
	
	print(f"collecting domains from {each_url}...")

	# Wait till everything loads
	time.sleep(20) 

# Close browser
driver.quit()
