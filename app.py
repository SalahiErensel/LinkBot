import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Set the path to the GeckoDriver executable
geckodriver_path = "YOUR_INSTALLED_GECKODRIVER_PATH"

# Read IPs from a text file
with open('YOUR_TXT_FILE_OPERATION_HERE', 'r') as file:
    ips = file.read().splitlines()
    link = input("Please enter a Link :  ") 

# Loop through each IP and perform the actions
for ip in ips:
    # Set up proxy options for Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument(f'--proxy-server=http://{ip}:80') 

    # Create a new instance of the Firefox driver with the proxy settings
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    # Navigate to the webpage
    driver.get(link)
    
    print("Entered to Link")

    # Wait for 2 seconds
    time.sleep(2)

    # Close the entire Firefox browser
    driver.quit()