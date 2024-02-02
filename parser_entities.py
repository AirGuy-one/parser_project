import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class YouTubeParser:
    def __init__(self):
        self.cookies_handled = False
        self.options = Options()
        self.driver = self.initialize_browser()

    def initialize_browser(self):
        return webdriver.Remote("http://selenium:4444/wd/hub", options=self.options)

    def parse_channel(self, channel_url) -> list:
        self.driver.get(channel_url)

        if not self.cookies_handled:
            reject_button = self.driver.find_element(By.XPATH, "//button[span[text()='Reject all']]")
            reject_button.click()
            self.cookies_handled = True

        channel_username = self.driver.find_element(By.ID, 'text').text
        video_links = self.driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
        video_data = []
        for link in video_links:
            video_id = link.get_attribute('href').split('/watch?v=')[-1]
            video_href = link.get_attribute('href')
            video_data.append((video_id, channel_username, video_href))

        return video_data

    @staticmethod
    def insert_data_to_db(video_data, conn, cursor):
        print('insert data to db')
        # for data in video_data:
        #    query = f"INSERT INTO videos (video_id, channel_username, video_href) VALUES ('{data[0]}', '{data[1]}', '{data[2]}')"
        #    cursor.execute(query)
        # conn.commit()

    def cleanup(self):
        self.driver.quit()
