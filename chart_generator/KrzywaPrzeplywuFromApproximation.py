import math
import os

import numpy as np
from matplotlib import pyplot as plt

import Constants


def computeFunctionParameters(df):
    n = len(df)
    W = n * np.sum(df['X_power']) - math.pow(np.sum(df['X']), 2)
    W_1 = np.sum(df['Y']) * np.sum(df['X_power']) - np.sum(df['X']) * np.sum(df['X_Y'])
    W_2 = n * np.sum(df['X_Y']) - np.sum(df['Y']) * np.sum(df['X'])
    a_1 = W_1 / W
    a_2 = W_2 / W
    a = math.exp(a_1)
    b = a_2
    return a, b


def Q_function(a, b, H):
    return a * math.pow(H, b)


def generateChart(df_for_krzywa_konsumpcyjna_table):
    df_for_krzywa_konsumpcyjna_table.drop(df_for_krzywa_konsumpcyjna_table.tail(1).index, inplace=True)  # drop row with summary

    a_param, b_param = computeFunctionParameters(df_for_krzywa_konsumpcyjna_table)

    H_values = np.arange(1, df_for_krzywa_konsumpcyjna_table['h_water'].max(), 0.001)
    Q_approx_values = []
    for H_current in H_values:
        Q_approx_values = np.append(Q_approx_values, Q_function(a_param, b_param, H_current))

    chart_name = 'Krzywa przepływu otrzymana w wyniku aproksymacji'
    approximated_curve_label = '$Q=%.1f*H^{%.1f}$' % (a_param, b_param)
    plt.figure(figsize=(10, 6))
    plt.scatter(Q_approx_values, H_values, linewidths=0.001, edgecolors='none', label=approximated_curve_label)
    plt.scatter(df_for_krzywa_konsumpcyjna_table['Q'], df_for_krzywa_konsumpcyjna_table['h_water'], marker='s', edgecolors='none', label='pomiary')
    plt.xlabel('$Q[m^3/s]$', fontsize=Constants.CHARTS_FONT_SIZE)
    plt.ylabel('$H[m]$', fontsize=Constants.CHARTS_FONT_SIZE)
    plt.title(chart_name, fontsize=Constants.CHARTS_FONT_SIZE + 3)
    plt.legend()
    plt.xticks(np.arange(0, max(Q_approx_values) + 50, 20))
    plt.grid()

    file_name = chart_name + '.png'
    file_path = os.path.join(Constants.TEMP_FOLDER_DIRECTORY, Constants.CHART_IMAGES_DIRECTORY, file_name)
    plt.savefig(file_path)

    return file_name, chart_name
