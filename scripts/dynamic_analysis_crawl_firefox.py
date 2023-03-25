import time
from selenium import webdriver

# Set the URL you want to open
url = ["https://www.youtube.com","https://www.nytimes.com","https://www.cnn.com"]

# Path to the extension file
extension_path = "/Users/shivani/Downloads/extensions/mozilla-malwarebytes.xpi"

driver = webdriver.Firefox()
driver.install_addon(extension_path, temporary=True)

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