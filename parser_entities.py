import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YouTubeParser:
    def __init__(self):
        self.cookies_handled = False
        self.driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", options=Options())

    def parse_channel(self, channel_url) -> list:
        self.driver.get(channel_url)

        try:
            if not self.cookies_handled:
                print(f'cookies handled {channel_url}')
                reject_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[span[text()='Reject all']]")))
                print(reject_button.text, f'reject button created {channel_url}')
                reject_button.click()
                print(f'reject button clicked {channel_url}')
                time.sleep(5)
                self.cookies_handled = True

            channel_username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "text"))).text

            video_links = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#video-title')))

            print(channel_username, f'channel_username {channel_url}')
            print(video_links[0], f'first video link here {channel_url}')

            video_data = []
            for link in video_links:
                video_id = link.get_attribute('href').split('/watch?v=')[-1]
                video_href = link.get_attribute('href')
                video_data.append((video_id, channel_username, video_href))

            return video_data

        finally:
            print(f'shit {channel_url}')

    @staticmethod
    def insert_data_to_db(video_data, conn, cursor):
        print('insert data to db')
        # for data in video_data:
        #    query = f"INSERT INTO videos (video_id, channel_username, video_href) VALUES ('{data[0]}', '{data[1]}', '{data[2]}')"
        #    cursor.execute(query)
        # conn.commit()

    def cleanup(self):
        self.driver.quit()
