import numpy as np
from matplotlib import pyplot as plt

from Constants import TEMP_FOLDER_DIRECTORY, CHARTS_FONT_SIZE


def printDailyFlowsAndStatesFluctuationCurveChart(przeplyw, stanWody, river_name, city_name,
                                                  year_of_chart, dni):
    chartFileName = "Krzywa wahań stanów i przepływów codziennych w roku %d" % year_of_chart
    title1 = "Krzywa wahań stanów i przepływów codziennych w roku %s\n rzeka:%s przekrój:%s" % (
        year_of_chart, river_name, city_name)

    fig, axes_for_states = plt.subplots()
    fig.subplots_adjust(right=0.75)
    fig.set_figheight(9)  # wysokosc w
    fig.set_figwidth(22)
    axes_for_states.grid()  # siatka
    axes_for_flows = axes_for_states.twinx()  # druga para osi. Oś X jest wspolna

    axes_for_states.set_title(title1, size=CHARTS_FONT_SIZE + 2)
    axes_for_states.set_xlabel('czas [dni]', size=CHARTS_FONT_SIZE)
    axes_for_states.set_ylabel("Przepływ wody [$m^{3}/s$]", size=CHARTS_FONT_SIZE)
    axes_for_flows.set_ylabel("Stan wody [cm]", size=CHARTS_FONT_SIZE)

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
