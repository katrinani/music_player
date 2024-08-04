import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def parsing_song(song: str) -> str:
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    prefs = {"download.default_directory": "/home/katrina/PycharmProjects/music_player/song_processing/song"}
    option.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    browser.get('https://spotifydown.com/ru')

    # находим поиск и передаем туда песню
    elem = browser.find_element(By.CSS_SELECTOR, 'input.searchInput')
    time.sleep(3)
    elem.send_keys(song + Keys.RETURN)
    time.sleep(3)

    # находим кнопку скачивания первой песни
    try:
        wait = WebDriverWait(browser, 10)
        info_music = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[@class='flex items-center justify-end']//button[@class='w-24 sm:w-32 mt-2 p-2 cursor-pointer bg-button rounded-full text-gray-100 hover:bg-button-active']"
            )))
        info_music.click()
    except NoSuchElementException:
        browser.quit()
        return "404"
    time.sleep(3)

    # скачивание mp3
    button = browser.find_element(By.XPATH, "//a[@download]")
    button.click()
    # ожидание, чтобы успел скачаться
    time.sleep(5)
    browser.quit()

    return "OK"


if __name__ == "__main__":
    print(parsing_song("https://open.spotify.com/track/6f807x0ima9a1j3VPbc7VN"))
