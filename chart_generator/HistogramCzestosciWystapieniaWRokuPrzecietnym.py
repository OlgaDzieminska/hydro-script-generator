import os

import numpy as np
from matplotlib import pyplot as plt

import Constants


def printHistogramCzestosciWystapieniaWRokuPrzecietnym(states_avg, states, parameter_name, year_from, year_to, city_name, river_name):
    y_ax = []
    chartName = 'Histogram częstości wystąpienia stanów w roku przeciętnym'
    chart_title = "%s dla okresu %s-%s\n rzeka:%s przekrój:%s" % (
        chartName, year_from, year_to, river_name, city_name)

    for state in states:
        a = sum(state) / 2
        y_ax = np.append(y_ax, a)

    if parameter_name == 'h_water':
        fig, ax = plt.subplots(figsize=(19, 8))
    elif parameter_name == 'Q':
        fig, ax = plt.subplots(figsize=(8, 15))
    else:
        raise ValueError(Constants.PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)

    for i in range(0, len(states)):
        state = states[i]
        y_pos = np.sum(state[0] + state[1]) / 2
        x_pos = states_avg['average year'][i]
        curr_height = state[1] - state[0]
        ax.barh(y_pos, x_pos, height=curr_height, align='center')

    ax.set_xlabel('Czas [dni]', size=Constants.CHARTS_FONT_SIZE)
    ax.set_title(chart_title, fontsize=Constants.CHARTS_FONT_SIZE + 2)

    if parameter_name == 'h_water':
        ax.set_ylabel('Stan [$cm$]', fontsize=Constants.CHARTS_FONT_SIZE)
        ax.set_yticks(y_ax)
        y_labels = [(str(state[0]) + '-' + str(state[1])) for state in states]
        ax.set_yticklabels(y_labels)
        ax.set_ylim(states[0][0] - 5, states[-1][1] + 5)
    elif parameter_name == 'Q':
        ax.set_ylabel('Przepływ [$m^3 /s$]', fontsize=Constants.CHARTS_FONT_SIZE)
        ax.set_ylim(states[0][0] - 20, states[-1][1] + 5)
    else:
        raise ValueError(Constants.PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)
    fig.tight_layout()
    ax.grid(axis='x')

    fileName = '%s - %s.png' % (chartName, parameter_name)
    outputFilePath = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, fileName)
    fig.savefig(fname=outputFilePath, dpi=600)
    return fileName, chart_title
