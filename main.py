import json


def loadSettingsFromFile():
    file = open('project_settings.json')
    data = json.load(file)
    file.close()
    return data


settingsDictionary = loadSettingsFromFile()
author_name = settingsDictionary['author']
print(author_name)
version = settingsDictionary['version']
print(version)
