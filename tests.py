import pandas as pd

from main import loadSettingsFromFile, print_greetings, printMainStatesFluctuationCurveForYears, printDailyFlowsAndStatesFluctuationCurveChart

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

# TEST printDailyFlowsAndStatesFluctuationCurveChart
df = pd.read_csv("./testStatesAndFlows.csv", encoding='cp1250', sep='\t')
dni = df["dzien"]
stanWody = df["stan wody"]
przeplyw = df["przeplyw"]
printDailyFlowsAndStatesFluctuationCurveChart(przeplyw, stanWody, "Ganges", "Hong-Kong", 2049, dni)

# TEST printMainStatesFluctuationCurveForYears
main_states_dictionary = {'Rok': [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991],
                          'NW': [106, 101, 91, 97, 98, 87, 100, 90, 104, 102],
                          'SW': [169, 142, 132, 149, 143, 127, 130, 140, 131, 136],
                          'WW': [378, 378, 243, 377, 321, 443, 220, 376, 248, 330]}
main_states = pd.DataFrame(main_states_dictionary)

main_states_2_degree_dictionary = {'NNW': [87], 'SNW': [97.6], 'WNW': [106], 'NSW': [127], 'SSW': [139.9], 'WSW': [169],
                                   'NWW': [220],
                                   'SWW': [331.4], 'WWW': [443]}
main_states_2_degree = pd.DataFrame(main_states_2_degree_dictionary)

printMainStatesFluctuationCurveForYears(main_states, main_states_2_degree, 'river_name', 'section_name', 1982, 1991)
