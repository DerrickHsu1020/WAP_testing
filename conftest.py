import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver(mobile_type: str = "iPhone 12 Pro"):
    """Setup chromedriver for mobile testing.

    :param mobile_type: mobile model for emulation, default value: iPhone 12 Pro
    """
    mobile_emulation = {"deviceName": mobile_type}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def handle_modal(driver, wait_time: int = 5):
    """Handles Twitch modal pop-ups.
    
    :param driver: Selenium WebDriver instance
    :param wait_time: Time(secs) for waiting the element
    """
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-a-target='modal-close-button']"))
        )
        close_button.click()
    except Exception:
        pass  # No modal present

def get_search_page(driver, wait_time: int = 10):
    """Navigates to the Twitch search page.
    
    :param driver: Selenium WebDriver instance
    :param wait_time: Time(secs) for waiting the element
    """
    try:
        search_button = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/directory']"))
        )
        search_button.click()
    except Exception as e:
        assert False, f"Failed to click search input: {e}"

def input_search(driver, search_term: str, wait_time: int = 10):
    """Inputs search term in the Twitch search box.
    
    :param driver: Selenium WebDriver instance
    :param wait_time: Time(secs) for waiting the element
    """
    search_input = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    search_input.send_keys(search_term)
    search_input.send_keys(Keys.RETURN)

def get_one_streamer(driver, wait_time: int = 10):
    """Selects the first available streamer.
    
    :param driver: Selenium WebDriver instance
    :param wait_time: Time(secs) for waiting the element
    """
    stream_buttons = WebDriverWait(driver, wait_time).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//button[contains(@class, 'ScCoreLink-sc')]")
        )
    )
    if stream_buttons:
        button = stream_buttons[0]
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(button))
        driver.execute_script("arguments[0].click();", button)
    else:
        assert False, "No streamers found"

def scroll_page(driver, direction: str="down", times: int=2, distance: int=800, delay: int=2):
    """Scrolls the page in the specified direction.

    :param driver: Selenium WebDriver instance
    :param direction: "down" (default) or "up"
    :param times: Number of times to scroll (default: 2)
    :param distance: Pixels to scroll per step (default: 800)
    :param delay: Delay between scrolls in seconds (default: 2)
    """
    scroll_distance = distance if direction == "down" else -distance

    for _ in range(times):
        driver.execute_script(f"window.scrollBy(0, {scroll_distance})")
        time.sleep(delay)
