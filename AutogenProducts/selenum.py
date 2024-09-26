from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def selenum(ProductName):
    brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    
    # Path to the BraveDriver or chromedriver executable
    driver_path = r"C:\chromedriver-win64\chromedriver.exe"

    # Create an instance of ChromeOptions and specify the Brave binary location
    chrome_options = Options()
    chrome_options.binary_location = brave_path

    # Initialize the WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Maximize window
    driver.maximize_window()

    # Navigate to DuckDuckGo
    driver.get('https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1')

    # Wait for the first button to be clickable, instead of using time.sleep()
    wait = WebDriverWait(driver, 20)  # Timeout set to 20 seconds
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div[2]/main/div/div/div[2]/div/button")))
    element.click()

    # Wait for the second button to be clickable
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div[2]/main/div/div/div[3]/div/button")))
    element.click()

    # Wait for the third button to be clickable
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div[2]/main/div/div/div[4]/div/div[2]/button")))
    element.click()

    # Wait for the input field to be visible
    element = wait.until(EC.visibility_of_element_located((By.NAME, "user-prompt")))

    # Send the prompt to the input field
    element.send_keys("Write me a 900 word description of product that I'm gonna give you in Arabic. Be careful with the SEO and the Title: " 
                      + ProductName + 
                      ". Don't write something about alright or okay; this is your description, just write it straightforward. "
                      "Make the headline as H3, and add a link in the last part of the product for this website https://tossonlibrary.com/product-category/%d9%83%d8%b4%d8%a7%d9%83%d9%8a%d9%84-%d9%88%d9%83%d8%b1%d8%a7%d8%b3%d8%a7%d8%aa/ , and the source , note that the libarary in arabic its مكتبة طوسون.")
    element.send_keys(Keys.ENTER)

    # Wait for the description to be generated (adjust the wait time as necessary)
    time.sleep(35)  # This can be optimized with more precise waits based on content visibility
    
    # Scroll down the page to load the entire description
    driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    
    # Retrieve the generated description
    description = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div[2]/main/div/section[2]/div/div[2]/div/div[1]/div[2]/div[2]/div/div")
    print(description.get_attribute("innerHTML"))

    # Send a second prompt to get a short description
    element = wait.until(EC.visibility_of_element_located((By.NAME, "user-prompt")))
    element.send_keys("Write me a short description of this 300 words .")
    element.send_keys(Keys.ENTER)

    # Wait for the short description to appear
    time.sleep(10)  # Adjust this based on the responsiveness of the service
    short_description = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div[2]/main/div/section[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div")
    print(short_description.get_attribute("innerHTML"))

    return description.get_attribute("innerHTML"), short_description.get_attribute("innerHTML")

# Close the browser after processing
