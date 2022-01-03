import os.path

import numpy as np
from matplotlib import pyplot as plt

import Constants
from table_generator import TableGenerator


def printKrzywaSumowaWUkladzieProstokatnym(datasetForKrzywaSumowaWUkladzieProstokatnym, years):
    flow_line = datasetForKrzywaSumowaWUkladzieProstokatnym[0]
    mean_line = datasetForKrzywaSumowaWUkladzieProstokatnym[1]

    fig, ax = plt.subplots(figsize=(20, 8))
    flow_line_label = 'Krzywa sumowa w okresie ' + str(years[0]) + ' - ' + str(years[-1])
    ax.plot(flow_line, 'b', label=flow_line_label, lw=3)

    mean_line_label = 'Średni przepływ w okresie ' + str(years[0]) + ' - ' + str(years[-1])
    ax.plot(mean_line, color='r', alpha=0.6, label=mean_line_label)

    ax.set_xticks(np.arange(0, 12 * len(years) + 1, 12))
    _yrs = [years[-1] + 1]
    ax.set_xticklabels(np.append(years, _yrs))
    plt.grid()
    plt.xlim(0, max(flow_line.index))
    plt.ylim(0, max(flow_line) + 1000)

    ax.legend()
    ax.set_ylabel('$\sum_ V [mln m^3]$', fontsize=13)

    chart_name = 'Krzywa sumowa w uładzie prostokątnym'
    ax.set_title(chart_name, fontsize=17)
    file_name = chart_name + '.png'
    file_path = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, file_name)
    fig.savefig(file_path)

    return file_name, chart_name
