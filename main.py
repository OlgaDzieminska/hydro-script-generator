import json


def loadSettingsFromFile():
    file = open('project_settings.json')
    data = json.load(file)
    file.close()
    return data


def print_greetings(_author_name, _version):
    print('Generator operatów, wersja:', _version)
    print('Autor', _author_name)


def fetch_request_data_from_UI():
    river_name_from_UI = input('Podaj nazwę rzeki:')
    section_name_from_UI = input('Podaj przekrój rzeki')
    year_from_from_UI = input('Podaj rok, od którego operat ma być generowany')
    year_to_from_UI = input('Podaj rok, do którego operat ma być generowany')

    return {'Nazwa rzeki': river_name_from_UI, 'Nazwa przekroju': section_name_from_UI, 'Rok rozpoczęcia operatu': year_from_from_UI,
            'Rok zakończenia operatu': year_to_from_UI}