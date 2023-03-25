import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def get_extension_ids(service, options , num_clicks):
    base_url = "https://microsoftedge.microsoft.com/addons/search/extensions"
    driver = webdriver.Edge(service=service, options=options)

    driver.get(base_url)
    extension_ids = set()

    for _ in range(num_clicks):
        time.sleep(2)  # Wait for extensions to load
        parent_div = driver.find_elements(By.CLASS_NAME, "c011")
        print("checking parent div", parent_div)
        child_divs = parent_div.find_elements(By.CLASS_NAME, "fui-FluentProvider fui-FluentProvider1 ___jdtuxv0 f19n0e5 fxugw4r f1o700av fk6fouc fkhj508 figsok6 f1i3iumi")

        print("checking the child div ", child_divs)


        # extensions = driver.find_elements_by_css_selector("a[class='card-image-link']")
        # for extension in extensions:
        #     print("checking this ", extension)
            # extension_id = extension.get_attribute("href").split('/')[-1]
            # extension_ids.add(extension_id)

        try:
            continue
            # show_more_button = driver.find_element_by_css_selector("button[class='c-show-more']")
            # show_more_button.click()
        except NoSuchElementException:
            print("No 'Show more' button found. Stopping.")
            break

    return extension_ids

def main():
    edge_webdriver_path = "../edge_webdriver/msedgedriver.exe"  # Replace with the path to your Edge WebDriver
    base_url = "https://microsoftedge.microsoft.com/addons/browse"
    num_clicks = 10  # Adjust the number of times to click the "Show more" button

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    service = Service(executable_path=edge_webdriver_path)

    extension_ids = get_extension_ids(service, options, num_clicks)

    # driver.quit()

    with open('extension_ids.txt', 'w') as output_file:
        for extension_id in extension_ids:
            output_file.write(f"{extension_id}\n")

    print(f"Successfully extracted {len(extension_ids)} extension IDs.")

if __name__ == '__main__':
    main()
