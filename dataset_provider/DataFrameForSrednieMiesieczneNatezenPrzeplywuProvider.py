import os.path

import numpy as np
import pandas as pd

from HydrologyReportCreator import ORDERED_HYDRO_MONTHS, TEMP_FOLDER_DIRECTORY


def createDataFrameForSrednieMiesieczneNatezeniaPrzeplywuTable(dataset_for_years, save_to_file):
    months_columns = [str(hydro_month) for hydro_month in ORDERED_HYDRO_MONTHS]
    mean_flows_for_years = pd.DataFrame(columns=months_columns)

    years_range = list(dataset_for_years.keys())
    for current_year in years_range:
        current_year_values = dataset_for_years[current_year]
        newRow = []
        for current_month in ORDERED_HYDRO_MONTHS:
            curr_month_df = current_year_values[current_year_values['MonthHydro'] == current_month]
            mean_flow_monthly = np.sum(curr_month_df['Q']) / len(curr_month_df['Q'])
            mean_flow_monthly = round(mean_flow_monthly, 3)
            newRow = np.append(newRow, mean_flow_monthly)
        mean_flows_for_years.loc[current_year] = newRow

    overall_mean_flow = []
    for current_month in ORDERED_HYDRO_MONTHS:
        sum_of_flow = np.sum(mean_flows_for_years[str(current_month)])
        sum_of_mean_flow = round(sum_of_flow / len(dataset_for_years), 2)
        overall_mean_flow = np.append(overall_mean_flow, sum_of_mean_flow)
    mean_flows_for_years.loc['mean'] = overall_mean_flow

    if save_to_file:
        out_file_name = 'Mean flow states ' + str(years_range[0]) + '-' + str(years_range[-1])
        out_file_path = os.path.join(TEMP_FOLDER_DIRECTORY, out_file_name)
        writer = pd.ExcelWriter(out_file_path + '.xlsx')
        mean_flows_for_years.to_excel(writer, index=False)
        writer.save()
    return mean_flows_for_years
