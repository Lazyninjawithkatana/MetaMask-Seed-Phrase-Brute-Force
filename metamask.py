import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# GeckoDriver
gecko_path = "/home/noname/Desktop/selenium/geckodriver"

# MetaMask profile. 
firefox_profile = "/home/noname/.mozilla/firefox/6u9lrsfk.default-esr"  

# Firefox parameter configuration
options = Options()
options.set_preference('xpinstall.signatures.required', False)  
options.set_preference("extensions.autoDisableScopes", 0)  
options.add_argument(f"--profile={firefox_profile}")  

# WebDriver run
service = Service(gecko_path)
driver = webdriver.Firefox(service=service, options=options)

# MetaMask's URL, which you want to open. You should replace it with your own URL. 
metamask_url = "moz-extension://5b6c83673-6554-44fd-b9e7-71512331/home.html#onboarding/import-with-recovery-phrase"
driver.get(metamask_url)

sleep(3)

# Read file
with open("cleaned.txt", "r", encoding="utf-8") as file:
    words = file.read().replace("\n", "").split(",")  # world list

# 12 element
fields = [driver.find_element(By.ID, f'import-srp__srp-word-{i}') for i in range(12)]

# Clear all fields and write random words
while True:
    # We are preparing 12 random words.
    chosen_words = random.sample(words, 12)

    for field, word in zip(fields, chosen_words):
        field.clear()
        field.send_keys(word)

    # Checking the login button
    submit_button = driver.find_element(By.CSS_SELECTOR, ".import-srp__confirm-button")

    if submit_button.is_enabled():  # ✅ If the button is enabled, it means the combination is correct.
        print("✅ The correct option has been found!")
    
        # Let's remember the correct 12 words.
        with open("successful_attempts.txt", "a", encoding="utf-8") as file:
            file.write(" ".join(chosen_words) + "\n")
            file.flush()
            file.close()
    
        #break  
    else:
        print("❌ Wrong words, let's try again...")
