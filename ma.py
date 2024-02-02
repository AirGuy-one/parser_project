import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", options=Options())
    cookies_handled = False
    print('driver has initialized')

    channels = ['https://www.youtube.com/@raily', 'https://www.youtube.com/@adorplayer']

    for index, channel in enumerate(channels):

        driver.get(channel)

        print(f'driver get {index}')

        try:
            if not cookies_handled:
                print(f'cookies handled {index}')
                reject_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[span[text()='Reject all']]")))
                print(reject_button.text, f'reject button created {index}')
                reject_button.click()
                print(f'reject button clicked {index}')
                time.sleep(5)
                cookies_handled = True

            channel_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "text"))).text

            video_links = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#video-title')))

            print(channel_username, f'channel_username {index}')
            print(video_links[0], f'first video link here {index}')

        finally:
            print(f'shit {index}')


if __name__ == '__main__':
    main()
