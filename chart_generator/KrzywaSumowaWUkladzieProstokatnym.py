import os.path

import numpy as np
from matplotlib import pyplot as plt

from HydrologyReportCreator import TEMP_FOLDER_DIRECTORY, CHART_IMAGES_DIRECTORY


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
    ax.set_ylabel('$\sum V [mln m^3]$', fontsize=13)
    ax.set_title('Krzywa sumowa w uładzie prostokątnym', fontsize=17)
    file_name = 'Krzywa sumowa w układzie prostokątnym.png'
    file_path = os.path.join(TEMP_FOLDER_DIRECTORY, CHART_IMAGES_DIRECTORY, file_name)
    fig.savefig(file_path)
