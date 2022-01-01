import os
import zipfile

import requests

from Constants import TEMP_FOLDER_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY, COULD_NOT_FIND_DATASET_FOR_REQUESTED_YEAR, \
    DAILY_VALUES_INPUT_FILES_DIRECTORY, PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE
from util import printProgressBar

BASE_URL = 'https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne'
DAILY_DATASET_ENDPOINT = "/dobowe/%d/"
HALF_YEARLY_DATASET_ENDPOINT = "/polroczne_i_roczne/%d/"
DAILY_DATA_ZIP_FILE_NAME_TEMPLATE = "codz_%d_%02d.zip"
DAILY_DATA_CSV_FILE_NAME_TEMPLATE = "codz_%d_%02d.csv"
YEARLY_DATA_ZIP_FILE_NAME_TEMPLATE_Q = "polr_Q_%d.zip"
YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_Q = "polr_Q_%d.csv"
YEARLY_DATA_ZIP_FILE_NAME_TEMPLATE_H_WATER = "polr_H_%d.zip"
YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_H_WATER = "polr_H_%d.csv"
YEARLY_VALUES_DOWNLOAD_PATH = os.path.join(TEMP_FOLDER_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY)


def __download_file(url: str, destination_directory: str):
    filename = url.split('/')[-1].replace(" ", "_")
    file_path = os.path.join(destination_directory, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        return file_path
    else:
        if r.status_code == 404:
            print(COULD_NOT_FIND_DATASET_FOR_REQUESTED_YEAR)
        r.raise_for_status()


def downloadDailyDataset(year):
    destination_directory = os.path.join(TEMP_FOLDER_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY)
    printProgressBar(0, 12, prefix='Postęp:', suffix='Ukończono', length=50)
    for current_month in range(1, 13):
        download_file_name = DAILY_DATA_ZIP_FILE_NAME_TEMPLATE % (year, current_month)
        current_url = BASE_URL + DAILY_DATASET_ENDPOINT % year + '/' + download_file_name
        __download_file(current_url, destination_directory=destination_directory)
        extractDatasetFromArchive(destination_directory, download_file_name)
        os.remove(os.path.join(destination_directory, download_file_name))
        printProgressBar(current_month, 12, prefix='Postęp:', suffix='Ukończono', length=50)
    print('Zakończono pobieranie zbioru danych dla dziennych z roku: %d.' % year)


def extractDatasetFromArchive(file_path, download_file_path):
    with zipfile.ZipFile(os.path.join(file_path, download_file_path), 'r') as zip_ref:
        zip_ref.extractall(file_path)


def downloadYearlyDatasets(years_range, parameter_name):
    number_of_years = len(years_range)
    printProgressBar(0, number_of_years, prefix='Postęp:', suffix='Ukończono', length=50)

    for i, current_year in enumerate(years_range):
        downloadYearlyDataset(current_year, parameter_name)
        printProgressBar(i + 1, number_of_years, prefix='Postęp:', suffix='Ukończono', length=50)

    print('Zakończono pobieranie zbioru danych dla rocznych i półrocznych.')


def downloadYearlyDataset(year, parameter_name):
    if parameter_name == 'h_water':
        download_file_name = YEARLY_DATA_ZIP_FILE_NAME_TEMPLATE_H_WATER % year
    elif parameter_name == 'Q':
        download_file_name = YEARLY_DATA_ZIP_FILE_NAME_TEMPLATE_Q % year
    else:
        raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)
    url = BASE_URL + HALF_YEARLY_DATASET_ENDPOINT % year + '/' + download_file_name
    __download_file(url, destination_directory=YEARLY_VALUES_DOWNLOAD_PATH)
    extractDatasetFromArchive(YEARLY_VALUES_DOWNLOAD_PATH, download_file_name)
    os.remove(os.path.join(YEARLY_VALUES_DOWNLOAD_PATH, download_file_name))
