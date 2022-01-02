import os

import numpy as np
from matplotlib import pyplot as plt

import Constants


def createChart(dry_year_df, wet_year_df, average_year_df, parameter_name, dry_year, wet_year, city_name, river_name):
    plt.figure(figsize=(17, 8))
    plt.xlabel('czas [dni]', fontsize=Constants.CHARTS_FONT_SIZE)
    plt.grid()
    plt.xlim(-2, 370)
    x_axis = []

    for df_index in average_year_df.index[:-1]:
        end_range_as_string = df_index[1:-1].split('-')[-1]
        end_range_as_float = float(end_range_as_string)
        x_axis = np.append(x_axis, end_range_as_float)

    plt.plot(average_year_df['higher'][:-1], x_axis, color='black', lw=3, label='rok przeciętny', linestyle='--')
    plt.plot(dry_year_df['higher'][:-1], x_axis, lw=3, label='rok suchy - ' + str(dry_year), color='r', alpha=0.7)
    plt.plot(wet_year_df['higher'][:-1], x_axis, lw=3, label='rok mokry - ' + str(wet_year), color='tab:cyan', linestyle='--', alpha=0.7)

    if parameter_name == 'h_water':
        parameter_name_description = 'stanów'
        plt.ylabel('stan [$m$]', fontsize=Constants.CHARTS_FONT_SIZE)
    elif parameter_name == 'Q':
        parameter_name_description = 'przepływów'
        plt.ylabel('przepływ [$m^3 /s$]', fontsize=Constants.CHARTS_FONT_SIZE)
    else:
        raise ValueError(Constants.PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)

    chartName = 'Krzywe sum czasów trwania %s wraz z wyższymi' % parameter_name_description
    chart_title = "%s \n rzeka:%s przekrój:%s" % (chartName, river_name, city_name)
    plt.title(chart_title, fontsize=Constants.CHARTS_FONT_SIZE + 2)
    plt.legend()
    plt.tight_layout()

    fileName = chartName + '.png'
    outputFilePath = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, fileName)
    plt.savefig(fname=outputFilePath, dpi=600)

    return fileName, chart_title
