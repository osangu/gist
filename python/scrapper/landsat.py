import os
from typing import List
from datetime import datetime


# util.py
def make_bbox(location, margin=0.05):
    lat, lon = location
    return [lon - margin, lat - margin, lon + margin, lat + margin]


def make_first_and_last_day_of_year(year):
    first_day = datetime(year=year, month=1, day=1)
    end_day = datetime(year=year, month=12, day=31)

    return first_day, end_day


# search.py
from pystac_client import Client


class Searcher:

    def __init__(self, search_url: str = 'https://landsatlook.usgs.gov/stac-server'):
        self.client = Client.open(search_url)

    def search(
            self,
            bbox: List[tuple],
            start_at: datetime,
            end_at: datetime,
            collections: str = 'landsat-c2l1',
            query: dict = {"platform": {"in": ["LANDSAT_8", "LANDSAT_9"]}},
    ):
        s_dt = start_at.strftime('%Y-%m-%d')
        e_dt = end_at.strftime('%Y-%m-%d')

        searched_data = self.client.search(
            collections=[collections],
            bbox=bbox,
            query=query,
            datetime=f'{s_dt}/{e_dt}'
        )
        dataset = self._serialize_dataset(searched_data)

        return dataset

    @staticmethod
    def _serialize_dataset(plain_data):
        dataset = {}

        for ind, result in enumerate(plain_data):
            dataset[result.id] = {}

            for asset in result.assets:
                dataset[result.id][asset] = asset.href

        return dataset


# download.py
from selenium import webdriver
from selenium.webdriver.common.by import By


class Downloader:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome()

    def download(self, download_url: str):
        self.driver.get(download_url)

        current_url = self.driver.current_url

        if current_url.startswith('https://ers.cr.usgs.gov/login?'):
            self._handle_login_redirect()
            self.download(download_url)

    def _set_download_path(self):
        pass

    def _handle_login_redirect(self):
        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        sign_in_button = self.driver.find_element(By.ID, 'loginButton')
        sign_in_button.click()


# main.py
tiles = [
    ('Salzgitter', [52.1554604, 10.3953505]),
    ('Bremen', [53.1257501, 8.6898810]),
    ('Eisenhuttenstadt', [52.1644183, 14.6395639])
]
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]


def main(save_path: str, searcher: Searcher, downloader: Downloader):
    for t_name, t_locate in tiles:
        for year in years:
            bbox = make_bbox(t_locate)
            start_at, end_at = make_first_and_last_day_of_year(year)

            dataset = searcher.search(bbox, start_at, end_at)

            # TODO: save_path
            downloader.download(dataset)


if __name__ == '__main__':
    searcher = Searcher()
    downloader = Downloader(username='', password='')

    main('/Volumes/Work/Crawler/ncpl/', searcher, downloader)
