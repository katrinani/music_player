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
    browser.get('https://muzsky.net/')

    # находим поиск и передаем туда песню
    elem = browser.find_element(By.ID, 'example-search-input')
    elem.send_keys(song + Keys.RETURN)
    # находим кнопку поиска и нажимаем
    share = browser.find_element(By.CSS_SELECTOR, ".btn.border-0.border.rounded-pill")
    share.click()

    # находим кноку скачивания первой песни
    try:
        info_music = browser.find_element(By.CSS_SELECTOR, '.icon.me-2.__adv_download')
        info_music.click()
    except NoSuchElementException:
        browser.quit()
        return "404"

    # -> переходим на страницу конкретной песни
    download_music = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'section.songdetail a.btn.btn-light.px-3.mx-2.w-75.mr-3.__adv_download'
        ))
    )
    download_music.click()

    # ожидание, чтобы успел скачаться
    time.sleep(15)
    browser.quit()

    return "OK"


if __name__ == "__main__":
    parsing_song("Linkin Park - Lost")
