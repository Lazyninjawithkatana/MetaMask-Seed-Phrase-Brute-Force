# MetaMask-Seed-Phrase-Brute-Force
This project is a Selenium-based automation script designed to test MetaMask seed phrase inputs. The script randomly selects words from a predefined list and attempts to find a valid combination. If a valid phrase is detected (i.e., the "Continue" button becomes active), the phrase is logged into a file.

⚠️ DISCLAIMER: This project is for educational purposes only. It should not be used for illegal activities, unauthorized access, or any form of unethical behavior. The author is not responsible for any misuse of this code.

Features

Uses Selenium WebDriver to automate interactions with the MetaMask extension.

Reads a list of possible words from a file and selects random combinations.

Detects when a valid seed phrase is found and logs it.

Compatible with Linux, macOS, and Windows.

Requirements

Linux & macOS

Python 3.x

Mozilla Firefox

GeckoDriver (WebDriver for Firefox)

Selenium (pip install selenium)

Windows

Python 3.x (Add to PATH during installation)

Mozilla Firefox

GeckoDriver (Ensure it's in the system PATH)

Selenium (pip install selenium)

