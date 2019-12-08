import time
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Action:
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity"
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        size = self.driver.get_window_size()
        self.start_x = size['width'] - 20
        self.start_y = size['height'] - 20
        self.distance = size['height'] // 2
        self.wait = WebDriverWait(self.driver, 10)

    def comments(self):
        time.sleep(2)
        self.driver.tap([(self.start_x, self.start_y)], 500)

    def scroll(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.ss.android.ugc.aweme:id/aqt"]')))
            while True:
                self.driver.swipe(self.start_x, self.start_y, self.start_x, self.start_y - self.distance)
                print('向上滑动')
                time.sleep(2)
        except TimeoutException as e:
            print('app已失去响应， 请重试')

    def main(self):
        # self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()