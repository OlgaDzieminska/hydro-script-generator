import os

import numpy as np
import pandas as pd

from HydrologyReportCreator import ORDERED_HYDRO_MONTHS, TEMP_FOLDER_DIRECTORY


def createDataFrameForObliczenieObjestosciOrazSumObjetosciTable(dataset_for_years, save_to_file):
    mean_flows_for_years = pd.DataFrame(columns=['year', 'month', 'days_in_month', 'mean_flow_monthly', 'mean_V', 'V_sum'])

    V_sum = 0
    row_index = 0
    years_range = list(dataset_for_years.keys())
    for current_year in years_range:
        current_year_values = dataset_for_years[current_year]

        for current_month in ORDERED_HYDRO_MONTHS:
            curr_month_df = current_year_values[current_year_values['MonthHydro'] == current_month]
            days_in_month = len(curr_month_df)
            mean_flow_monthly = np.sum(curr_month_df['Q']) / len(curr_month_df['Q'])
            mean_flow_monthly = round(mean_flow_monthly, 3)

            mean_V = mean_flow_monthly * days_in_month * 24 * 3600
            mean_V = round(mean_V, 2)
            mean_V *= 10 ** -6
            V_sum += mean_V

            row_index += 1
            mean_flows_for_years.loc[row_index] = [current_year, current_month, days_in_month, mean_flow_monthly, mean_V, V_sum]
    if save_to_file:
        out_file_name = 'Mean flow states ' + str(years_range[0]) + '-' + str(years_range[-1])
        out_file_path = os.path.join(TEMP_FOLDER_DIRECTORY, out_file_name)
        writer = pd.ExcelWriter(out_file_path + '.xlsx')
        mean_flows_for_years.to_excel(writer, index=False)
        writer.save()
    return mean_flows_for_years
