import json
import os

import re

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

TEMP_FOLDER_DIRECTORY = "temp"
chartsFontSize = 14


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
    year_of_chart_from_UI = input('Podaj rok, dla którego ma być wygenerowana krzywa wahań stanów i przepływów codziennych')
    return {'Nazwa rzeki': river_name_from_UI, 'Nazwa przekroju': section_name_from_UI, 'Rok rozpoczęcia operatu': year_from_from_UI,
            'Rok zakończenia operatu': year_to_from_UI,
            'Rok dla którego ma być wygenerowana krzywa wahań stanów i przepływów codziennych': year_of_chart_from_UI}


def printDailyFlowsAndStatesFluctuationCurveChart(przeplyw, stanWody, river_name, section_name,
                                                  year_of_chart, dni):
    chartFileName = "Krzywa wahań stanów i przepływów codziennych w roku %d" % year_of_chart
    title1 = "Krzywa wahań stanów i przepływów codziennych w roku %s\n rzeka:%s przekrój:%s" % (
        year_of_chart, river_name, section_name)

    fig, axes_for_states = plt.subplots()
    fig.subplots_adjust(right=0.75)
    fig.set_figheight(9)  # wysokosc w
    fig.set_figwidth(22)
    axes_for_states.grid()  # siatka
    axes_for_flows = axes_for_states.twinx()  # druga para osi. Oś X jest wspolna

    axes_for_states.set_title(title1, size=chartsFontSize + 2)
    axes_for_states.set_xlabel('czas [dni]', size=chartsFontSize)
    axes_for_states.set_ylabel("Przepływ wody [$m^{3}/s$]", size=chartsFontSize)
    axes_for_flows.set_ylabel("Stan wody [cm]", size=chartsFontSize)

    axes_for_states.plot(przeplyw, "b-", lw=2, label="Stan wody")
    axes_for_flows.plot(stanWody, "r-", lw=2, label="Przepływ")

    axes_for_states.set_xlim(0, len(dni))
    axes_for_states.set_ylim(0.2, max(przeplyw) + 50)
    axes_for_states.set_xticks(np.arange(0, len(dni), 10))

    axes_for_states.legend(loc=(0.9, 0.9))  # legenda do wykresu
    axes_for_flows.legend(loc=(0.9, 0.86))

    fig.tight_layout()
    outputFilePath = '{tempDirectory}/{fileName}.png'.format(tempDirectory=TEMP_FOLDER_DIRECTORY,
                                                             fileName=chartFileName)
    fig.savefig(bbox_inches='tight', fname=outputFilePath)

    return outputFilePath


def printMainStatesFluctuationCurveForYears(main_states, main_states_2_degree, river_name, section_name,
                                            year_from_from_UI, year_to_from_UI, ):
    tabzm = (range(year_from_from_UI, year_to_from_UI, 1))
    chartName = 'Krzywa wahań stanów głównych'
    title = "%s dla okresu %s-%s\n rzeka:%s przekrój:%s" % (
        chartName, year_from_from_UI, year_to_from_UI, river_name, section_name)

    figure, axes = plt.subplots()
    figure.subplots_adjust(right=0.75)
    figure.set_figheight(9)
    figure.set_figwidth(18)
    axes.grid()
    myFontSize = 14
    axes.set_title(title, size=myFontSize + 3)
    axes.set_xlabel('czas [lata]', size=myFontSize)
    axes.set_ylabel("stan wody [$cm$]", size=myFontSize)

    d = main_states['Rok']
    c = [0]
    c[1:] = d
    c = pd.Series(c)

    years = (range(year_from_from_UI, year_to_from_UI + 1, 1))
    a = main_states['SW']
    b = [2]
    b[1:] = a
    b = pd.Series(b)
    axes.step(c, b, color='g', label="SW")
    axes.plot(years, main_states['WW'], color='r', label="WW")
    axes.plot(years, main_states['NW'], color='b', label="NW")
    axes.legend(loc=(1.1, 0.85), fontsize=myFontSize - 3)
    axes.set_xticks(tabzm)
    axes.set_xlim(year_from_from_UI, year_to_from_UI)
    highest_value = main_states[['NW', 'WW', 'SW']].max().max()
    lowest_value = main_states[['NW', 'WW', 'SW']].min().min()
    axes.set_ylim(lowest_value - 10, highest_value + 30)

    patternsWithColors = [('.WW', 'red'), ('.SW', 'green'), ('.GS', 'violet'), ('.NW', 'blue')]
    for columnName in main_states_2_degree:
        state_value_in_column = main_states_2_degree[columnName][0]
        matchingColor = 'black'
        for pattern, color in patternsWithColors:
            patternMatches = re.match(pattern, columnName)
            if patternMatches:
                matchingColor = color
                break
        if matchingColor == 'black':
            print(columnName)
        axes.axhline(y=state_value_in_column, linestyle="--", color=matchingColor)
        horizontal_line_description = '%s (%d)' % (columnName, state_value_in_column)
        axes.text(s=horizontal_line_description, x=years[-1] + 0.05, y=state_value_in_column)

    fileName = chartName + '.png'
    outputFilePath = os.path.join(TEMP_FOLDER_DIRECTORY, fileName)
    figure.savefig(fname=outputFilePath)
    figure.tight_layout()
    return outputFilePath
