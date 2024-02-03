import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, InvalidSessionIdException


class YouTubeParser:
    def __init__(self):
        self.cookies_handled = False
        self.driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", options=Options())
        self.conn = psycopg2.connect(dbname='youtube_parser_db', user='youtube_parser_user',
                                     password='youtube_parser_password', host='db', port='5432')
        self.cursor = self.conn.cursor()

    def parse_channel(self, channel_url: str) -> list:

        self.driver.get(channel_url)
        # Delay to allow the page to load
        time.sleep(5)

        if not self.cookies_handled:
            reject_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[span[text()='Reject all']]")))
            reject_button.click()
            time.sleep(5)
            self.cookies_handled = True

        try:
            channel_username = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "text"))).text

            video_links = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#video-title')))

            video_data = []
            for link in video_links:
                video_id = link.get_attribute('href').split('/watch?v=')[-1]
                video_href = link.get_attribute('href')
                video_data.append((video_id, channel_username, video_href))

            return video_data

        except InvalidSessionIdException as iside:
            print(f'InvalidSessionIdException occurred: {iside}')
        except TimeoutException as te:
            print(f'TimeoutException occurred while waiting for elements to load: {te}')
        except WebDriverException as wde:
            print(f'WebDriverException occurred: {wde}')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def creating_table(self):
        query = '''
                CREATE TABLE IF NOT EXISTS videos (
                    video_id VARCHAR(255),
                    channel_username VARCHAR(255),
                    video_href VARCHAR(255)
                );
                '''
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data_to_db(self, video_data: list):
        for data in video_data:
            query = f'''
                        INSERT INTO videos (
                            video_id,
                            channel_username,
                            video_href
                        ) VALUES (
                            '{data[0]}',
                            '{data[1]}',
                            '{data[2]}'
                        )
                    '''
            self.cursor.execute(query)
        self.conn.commit()

    def close_connections(self):
        self.cursor.close()
        self.conn.close()

    def cleanup(self):
        self.driver.quit()
