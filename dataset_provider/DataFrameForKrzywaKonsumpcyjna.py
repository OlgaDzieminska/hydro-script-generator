import random

import numpy as np
import pandas as pd

import util

KRZYWA_KONSUMPCYJNA_COLUMNS = ['date', 'h_water', 'Q', 'X', 'Y', 'X_power', 'X_Y']
HYDRO_MONTHS_TO_RETRIEVE = [
    1,  # December
    3,  # January
    6,  # April
    8,  # July
    11  # November
]
NUMBERS_PRECISION = 8


def provide(dataset_for_years, years_range):
    krzywa_konsumpcyjna = pd.DataFrame(columns=KRZYWA_KONSUMPCYJNA_COLUMNS)

    i = 1
    for current_year in years_range:
        current_year_df = dataset_for_years[current_year]
        for current_hydro_month in HYDRO_MONTHS_TO_RETRIEVE:
            values_in_month = current_year_df[current_year_df['MonthHydro'] == current_hydro_month]
            days_in_month = values_in_month['day'].max()
            random_day = random.randint(1, days_in_month)

            date = '%02d-%02d-%d' % (random_day, util.convertHydroMonthToNormal(current_hydro_month), current_year)
            h_water_value = values_in_month[values_in_month['day'] == random_day]['h_water'].iloc[
                                0] / 100  # divide by 100 as h_water is in [cm], so we need to convert it to [m]
            Q_value = values_in_month[values_in_month['day'] == random_day]['Q'].iloc[0]
            X = round(np.log(h_water_value), NUMBERS_PRECISION)
            Y = round(np.log(Q_value), NUMBERS_PRECISION)
            X_power = round(X * X, NUMBERS_PRECISION)
            X_Y = round(X * Y, NUMBERS_PRECISION)
            new_row = [date, h_water_value, Q_value, X, Y, X_power, X_Y]
            krzywa_konsumpcyjna.loc[i] = new_row
            i += 1

    X_sum = round(np.sum(krzywa_konsumpcyjna['X']), NUMBERS_PRECISION)
    Y_sum = round(np.sum(krzywa_konsumpcyjna['Y']), NUMBERS_PRECISION)
    X_power_sum = round(np.sum(krzywa_konsumpcyjna['X_power']), NUMBERS_PRECISION)
    X_Y_sum = round(np.sum(krzywa_konsumpcyjna['X_Y']), NUMBERS_PRECISION)
    summary_row = [0, 0, 0, X_sum, Y_sum, X_power_sum, X_Y_sum]
    krzywa_konsumpcyjna.loc['sum'] = summary_row

    return krzywa_konsumpcyjna
