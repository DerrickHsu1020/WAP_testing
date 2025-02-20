# WAP_testing

# Twitch Streaming Test Automation

## Overview
This project automates the process of searching for a Twitch streamer on the mobile version of Twitch and verifying that the video stream plays correctly. The automation is implemented using Selenium with Pytest.

## Features
- **Mobile Browser Emulation**: Simulates an iPhone 12 Pro environment.
- **Automated UI Interactions**:
  - Navigates to Twitch
  - Searches for a specified game or keyword
  - Selects a streamer
  - Verifies video playback
- **Reusable Utility Functions**: Common functions are stored in `conftest.py` for better modularity.

## Project Structure
```
├── conftest.py          # Contains reusable fixtures and helper functions
├── test_twitch.py       # Main test script for Twitch streaming
├── README.md            # Project documentation
```

## Setup & Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- Chrome browser
- ChromeDriver (compatible with your Chrome version)


## Running the Tests
To execute the test, run:
```bash
pytest test_twitch.py
```

## Customization
### Modify Search Term
Update `search_term` inside `TestTwitchStreaming` class to search for a different game.

### Adjust Scroll Behavior
Modify `scroll_page(driver, direction, times, distance, delay)` in `conftest.py` to control scrolling behavior.

## Common Issues & Solutions
- **WebDriver Exception**: Ensure that your ChromeDriver version matches your installed Chrome browser version.
- **Element Not Found Errors**: Twitch's UI may have changed; update the selectors accordingly in `conftest.py`.
