# Documentation

## Project Overview

This project is a web scraping tool designed to extract job posting information from dynamically loaded websites. It uses Selenium WebDriver to handle JavaScript-rendered content within iframes.

## Prerequisites

- Python 3.7 or higher
- Chrome browser installed on your system
- ChromeDriver (automatically managed by Selenium)

## Project Structure

```
project/
├── .gitignore
├── requirements.txt
└── scrap.py
```

## Setup Instructions

### 1. Create Virtual Environment

Create an isolated Python environment for the project:

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` prefix in your terminal after activation.

### 3. Install Dependencies

Install all required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

This will install:
- `requests` - HTTP library for making web requests
- `beautifulsoup4` - HTML parsing library
- `selenium` - Browser automation tool
- `lxml` - XML/HTML parser
- `schedule` - Job scheduling library
- `pyautogui` - GUI automation library

### 4. Verify Installation

Check if packages are installed correctly:

```bash
pip list
```

## Code Structure

### Commented Sections

The `scrap.py` file contains three approaches to web scraping, with the first two commented out:

#### Section 1: Basic Requests Method (Commented)

```python
# import requests as re
# from bs4 import BeautifulSoup
```

This approach uses simple HTTP requests and BeautifulSoup for parsing. It's commented out because it doesn't work for dynamically loaded content.

**Why it doesn't work:** The target website loads content via JavaScript after the initial page load, so a simple HTTP request only retrieves the basic HTML skeleton.

#### Section 2: Basic Selenium Method (Commented)

```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# ...
```

This is a working Selenium implementation but written as inline code rather than a reusable function. It's commented out in favor of the function-based approach.

#### Section 3: Function-Based Selenium Method (Active)

This is the current active implementation using a reusable function.

## Active Code Explanation

### Imports

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
```

- `webdriver` - Controls the browser
- `By` - Locates elements using various strategies (ID, CSS, XPath)
- `WebDriverWait` - Implements explicit waits
- `expected_conditions (EC)` - Predefined conditions for waiting
- `TimeoutException` - Handles timeout errors
- `time` - Adds delays when needed

### Main Function: scrape_iframe_content()

```python
def scrape_iframe_content(url):
```

This function takes a URL as input and extracts job information from an iframe.

#### Browser Setup

```python
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
```

- Creates Chrome browser options
- `--no-sandbox` - Disables Chrome's security sandbox (useful in certain environments)
- Initializes Chrome WebDriver

#### Content Extraction

```python
driver.get(url)
wait = WebDriverWait(driver, 20)
iframe = wait.until(EC.presence_of_element_located((By.ID, "icims_content_iframe")))
```

- Navigates to the target URL
- Creates a wait object with 20-second timeout
- Waits for the iframe to load before proceeding

```python
driver.switch_to.frame(iframe)
time.sleep(3)
```

- Switches context into the iframe
- Adds 3-second delay to ensure content is fully rendered

```python
job_title = driver.find_element(By.CSS_SELECTOR, "h1, .iCIMS_Header h2").text
description = driver.find_element(By.CSS_SELECTOR, ".iCIMS_InfoMsg, .iCIMS_Expandable_Text").text
body = driver.find_element(By.TAG_NAME, "body")
print(job_title, description, body.text)
```

- Extracts job title from h1 or specific h2 element
- Extracts description from specific CSS classes
- Gets entire body text
- Prints all extracted information

#### Cleanup

```python
finally:
    input("Press Enter to close...")
    driver.quit()
```

- Ensures browser closes even if errors occur
- Waits for user input before closing (for inspection)
- Properly terminates the WebDriver session

## Running the Script

### Basic Execution

```bash
python scrap.py
```

The script will:
1. Open a Chrome browser window
2. Navigate to the job posting URL
3. Wait for content to load
4. Extract and print job information
5. Wait for you to press Enter
6. Close the browser

### Modifying the Target URL

Change the URL in the last line of the script:

```python
url = "YOUR_TARGET_URL_HERE"
scrape_iframe_content(url)
```

## Uncommenting Sections

### To Test Basic Requests Method

1. Comment out the current active section (lines with function definition)
2. Uncomment Section 1 (lines 1-9)
3. Run the script

### To Test Basic Selenium Method

1. Comment out the current active section
2. Uncomment Section 2 (lines 11-30)
3. Run the script

### To Switch Back to Function Method

1. Comment out other sections
2. Uncomment the function-based section
3. Run the script

## Troubleshooting

### ChromeDriver Issues

If you get ChromeDriver errors:
```bash
pip install --upgrade selenium
```

Selenium 4.x automatically manages ChromeDriver.



### Browser Doesn't Close

If the browser hangs:
- Press Ctrl+C in terminal
- Manually close browser windows
- Check for zombie ChromeDriver processes



## Deactivating Virtual Environment

When finished working:

```bash
deactivate
```

