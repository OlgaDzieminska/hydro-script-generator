import os

import numpy as np
from matplotlib import pyplot as plt

import Constants
from Constants import CHARTS_FONT_SIZE


def printDailyFlowsAndStatesFluctuationCurveChart(przeplyw, stanWody, river_name, city_name,
                                                  year_of_chart):
    days = len(przeplyw)
    chart_name = "Krzywa wahań stanów i przepływów codziennych w roku %d" % year_of_chart
    chart_title = "Krzywa wahań stanów i przepływów codziennych w roku %s\n rzeka:%s przekrój:%s" % (
        year_of_chart, river_name, city_name)

    fig, axes_for_states = plt.subplots()
    fig.subplots_adjust(right=0.75)
    fig.set_figheight(9)  # wysokosc w
    fig.set_figwidth(22)
    axes_for_states.grid()  # siatka
    axes_for_flows = axes_for_states.twinx()  # druga para osi. Oś X jest wspolna

    axes_for_states.set_title(chart_title, size=CHARTS_FONT_SIZE + 2)
    axes_for_states.set_xlabel('czas [dni]', size=CHARTS_FONT_SIZE)
    axes_for_states.set_ylabel("Przepływ wody [$m^{3}/s$]", size=CHARTS_FONT_SIZE)
    axes_for_flows.set_ylabel("Stan wody [cm]", size=CHARTS_FONT_SIZE)

    axes_for_states.plot(przeplyw, "b-", lw=2, label="Stan wody")
    axes_for_flows.plot(stanWody, "r-", lw=2, label="Przepływ")

    axes_for_states.set_xlim(0, days)
    axes_for_states.set_ylim(0.2, max(przeplyw) + 50)
    axes_for_states.set_xticks(np.arange(0, days, 10))

    axes_for_states.legend(loc=(0.9, 0.9))  # legenda do wykresu
    axes_for_flows.legend(loc=(0.9, 0.86))

    fig.tight_layout()
    file_name = chart_name + '.png'
    output_file_path = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, file_name)
    fig.savefig(bbox_inches='tight', fname=output_file_path)

    return file_name, chart_name
