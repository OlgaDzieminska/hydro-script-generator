import os
import re

import pandas as pd
from matplotlib import pyplot as plt

import Constants


def printMainStatesFluctuationCurveForYears(main_states, main_states_2_degree, river_name, section_name,
                                            year_from_from_UI, year_to_from_UI, ):
    main_states_without_sum = pd.DataFrame(main_states)
    main_states_without_sum.drop(main_states.tail(1).index, inplace=True)
    tabzm = (range(year_from_from_UI, year_to_from_UI, 1))
    chartName = 'Krzywa wahań stanów głównych'
    title = "%s dla okresu %s-%s\n rzeka:%s, przekrój:%s" % (
        chartName, year_from_from_UI, year_to_from_UI, river_name, section_name)

    figure, axes = plt.subplots()
    figure.subplots_adjust(right=0.75)
    figure.set_figheight(9)
    figure.set_figwidth(18)
    axes.grid()
    axes.set_title(title, size=Constants.CHARTS_FONT_SIZE + 3)
    axes.set_xlabel('czas [lata]', size=Constants.CHARTS_FONT_SIZE)
    axes.set_ylabel("stan wody [$cm$]", size=Constants.CHARTS_FONT_SIZE)

    years_in_period = main_states_without_sum.index
    years_on_horizontal_axis = [0]
    years_on_horizontal_axis[1:] = years_in_period
    years_on_horizontal_axis = pd.Series(years_on_horizontal_axis)

    vertical_values_for_SW_line = [2]
    vertical_values_for_SW_line[1:] = main_states_without_sum['SW']
    vertical_values_for_SW_line = pd.Series(vertical_values_for_SW_line)
    axes.step(years_on_horizontal_axis, vertical_values_for_SW_line, color='g', label="SW")
    axes.plot(years_in_period, main_states_without_sum['WW'], color='r', label="WW")
    axes.plot(years_in_period, main_states_without_sum['NW'], color='b', label="NW")
    axes.legend(loc=(1.1, 0.85), fontsize=Constants.CHARTS_FONT_SIZE - 3)
    axes.set_xticks(tabzm)
    axes.set_xlim(year_from_from_UI, year_to_from_UI)
    highest_value = main_states_without_sum[['NW', 'WW', 'SW']].max().max()
    lowest_value = main_states_without_sum[['NW', 'WW', 'SW']].min().min()
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
        axes.text(s=horizontal_line_description, x=years_in_period[-1] + 0.05, y=state_value_in_column)

    fileName = chartName + '.png'
    outputFilePath = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, fileName)
    figure.savefig(fname=outputFilePath)
    figure.tight_layout()
    return fileName, title
