import os
import re

import pandas as pd
from matplotlib import pyplot as plt

from Constants import TEMP_FOLDER_DIRECTORY


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
