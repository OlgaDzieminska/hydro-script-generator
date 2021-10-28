from main import loadSettingsFromFile, print_greetings

# Task 1 - load settings from file
settingsDictionary = loadSettingsFromFile()
author_name = settingsDictionary['author']
print(author_name)
version = settingsDictionary['version']
print(version)


# Task 2 - Print greetings message with project version
print_greetings(author_name, version)


# Task 3 - Fetch request data from UI
# data_from_UI = fetch_request_data_from_UI()
data_from_UI = {'Nazwa rzeki': 'Wisła', 'Nazwa przekroju': 'Tczew', 'Rok rozpoczęcia operatu': 1980,
                'Rok zakończenia operatu': 1990}

river_name = data_from_UI['Nazwa rzeki']
print(river_name)
print(data_from_UI)
