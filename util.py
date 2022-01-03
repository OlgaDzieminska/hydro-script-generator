import json
import os
import shutil
from datetime import datetime

from Constants import TEMP_FOLDER_DIRECTORY, CHART_IMAGES_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY, \
    OUTPUT_FILE_NAME_BASE


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def removeTemporaryFiles():
    temp_directory = os.path.join(TEMP_FOLDER_DIRECTORY)
    for filename in os.listdir(temp_directory):
        file_path = os.path.join(temp_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def createRequiredDirectoriesIfDoesNotExists():
    for directory_to_create in [CHART_IMAGES_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY]:
        path_for_directory = os.path.join(TEMP_FOLDER_DIRECTORY, directory_to_create)
        if not os.path.exists(path_for_directory):
            os.makedirs(path_for_directory)


def provideOutputFileName():
    now = datetime.now()
    data_and_time_string = now.strftime("%d-%m-%Y %H.%M.%S")
    return "%s %s.docx" % (OUTPUT_FILE_NAME_BASE, data_and_time_string)


def createRegexForRiverNameInInputFile(search_river_name):
    return '^' + search_river_name + ' [(]'


def loadSettingsFromFile():
    file = open('project_settings.json')
    data = json.load(file)
    file.close()
    return data


def print_greetings():
    print('Generator operatów')
    print('Autor: Olga Dziemińska\n')


def fetch_request_data_from_UI():
    river_name_from_UI = input('Podaj nazwę rzeki, kanału lub jeziora. Format podanej nazwy jeziora powinien wyglądać następująco:"Jez. <nazwa jeziora>":')
    city_name_from_UI = input('Podaj przekrój rzeki (nazwa miasta):')
    year_from_from_UI = int(input('Podaj rok, od którego ma być generowany operat:'))
    year_to_from_UI = int(input('Podaj rok, do którego ma być generowany operat:'))
    year_of_krzywa_wahan_stanow_i_przeplywow_codziennych = int(
        input('Podaj rok, dla którego ma być wygenerowana krzywa wahań stanów i przepływów codziennych:'))
    first_year_of_multiannual_period = int(input(
        'Podaj początkowy rok czterolecia, dla którego mają byś wykonane histogramy częstości wystąpienia stanów/przepływów i krzywe sum czasów '
        'trwania stanów/przepływów wraz z wyższymi:'))
    return river_name_from_UI, city_name_from_UI, year_from_from_UI, year_to_from_UI, year_of_krzywa_wahan_stanow_i_przeplywow_codziennych, first_year_of_multiannual_period


def convertHydroMonthToNormal(hydro_month):
    if hydro_month > 2:
        return hydro_month - 2
    else:
        return hydro_month + 10
