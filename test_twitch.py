import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import handle_modal, get_search_page, input_search, get_one_streamer, scroll_page

class TestTwitchStreaming:
    url = "https://m.twitch.tv/"
    search_term = "StarCraft II"

    def test_twitch_streaming(self, driver) -> None:
        """Test streamer is playing and get the screen shots

        :param driver: fixture
        """
        # Step 1: Go to Twitch and handle potential modal
        driver.get(self.url)
        handle_modal(driver)

        # Step 2: Click the search icon
        get_search_page(driver)

        # Step 3: Input "StarCraft II"
        input_search(driver, self.search_term)

        # Step 4: Scroll down 2 times
        scroll_page(driver)

        # Step 5: Select one streamer and handle potential modal
        get_one_streamer(driver)
        handle_modal(driver)

        # Step 6: Wait for stream to load and take a screenshot
        video_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
        )
        limit_time = 0
        while limit_time < 15:
            is_video_paused = driver.execute_script("arguments[0].paused;", video_element)
            if is_video_paused:
                limit_time += 1
            else:        
                break
        driver.save_screenshot("stream_screenshot.png")
        assert not is_video_paused, "Test Failed, video is not start playing"