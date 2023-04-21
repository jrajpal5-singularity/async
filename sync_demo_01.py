"""demo for downloading free photos from pexels.com"""

import time
import os
from pathlib import Path
from typing import List, Optional
import requests


def download_file(photo_id: str, dirname: str) -> None:
    """download file from Pexels

    Args:
        photo_id (str): id of the photo to download
        dirname (str): directory where photos to be downloaded
    """
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        print(f"Downloading: {photo_id}.jpeg")

        filepath = Path(f"{dirname}/{photo_id}.jpeg")

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            with open(filepath, "wb") as img_file:
                img_file.write(response.content)
            print(f"Downloaded: {photo_id}.jpeg")

    except Exception as exe:
        print(exe)

def download_all(list_photo_ids: List[str], dirname: Optional[str]="images_01") -> None:
    """download all photos from the given list

    Args:
        list_photo_ids (List[str]): list of photo ids to download
        dirname (str, optional): directory where photos to be downloaded. Defaults to "images_01".
    """
    os.makedirs(dirname, exist_ok=True)
    for photo_id in list_photo_ids:
        download_file(photo_id=photo_id, dirname=dirname)
        print(f"----\n\n")


if __name__ == '__main__':
    # get the list of photos ids
    with open("list_photo_ids.txt", "r") as f:
        list_photo_ids = [line.rstrip() for line in f.readlines()]
    print(list_photo_ids)
    # call download all function
    start_time = time.time()
    download_all(list_photo_ids=list_photo_ids)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")