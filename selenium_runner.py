import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def run_test(steps_json):
    driver = get_driver()
    results = []

    try:
        steps = json.loads(steps_json)
        for step in steps:
            action = step.get("action")

            if action == "open":
                driver.get(step["url"])
                results.append(f"Opened {step['url']} ✅")

            elif action == "fill":
                element = driver.find_element(By.NAME, step["field"])
                element.clear()
                element.send_keys(step["value"])
                results.append(f"Filled {step['field']} ✅")

            elif action == "click":
                element = driver.find_element(By.CSS_SELECTOR, step["selector"])
                element.click()
                results.append("Clicked element ✅")

            elif action == "check":
                if step["text"] in driver.page_source:
                    results.append(f"Found text '{step['text']}' ✅")
                else:
                    results.append(f"Text '{step['text']}' not found ❌")

    except Exception as e:
        results.append(f"Error: {str(e)}")
    finally:
        driver.quit()

    return results
