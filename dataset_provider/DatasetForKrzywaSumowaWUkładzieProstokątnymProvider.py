import numpy as np
import pandas as pd

from Constants import MONTHS


def provideDatasetForKrzywaSumowaWUkladzieProstokatnym(dataset_for_years):
    years = list(dataset_for_years.keys())
    flow_sum_for_years = pd.DataFrame(columns=MONTHS)

    for i, current_year in enumerate(dataset_for_years.keys()):
        df_for_current_year = dataset_for_years[current_year]
        flow_in_year = []

        if i == 0:
            flow_in_month = 0
        else:
            previous_year = years[i - 1]
            flow_in_month = flow_sum_for_years.loc[previous_year].values[-1]
        for current_month in MONTHS:
            curr_m_df = df_for_current_year[df_for_current_year["MonthHydro"] == float(current_month)]
            flow_in_month = round(flow_in_month + np.sum(curr_m_df['Q']), 1)
            flow_in_year = np.append(flow_in_year, flow_in_month)
        flow_sum_for_years.loc[current_year] = flow_in_year

    flow_line = pd.Series(dtype=float)
    flow_line.loc[0] = 0
    month_sum = 0
    for current_year in years:
        flow_sum_for_year = flow_sum_for_years.loc[current_year]

        for month in MONTHS:
            flow_line.loc[month_sum + month] = flow_sum_for_year[month]
        month_sum += 12

    mean_line = pd.Series(dtype=float)
    mean_line.loc[0] = 0
    mean_line.loc[12 * len(years)] = flow_line.iloc[-1]

    return flow_line, mean_line
