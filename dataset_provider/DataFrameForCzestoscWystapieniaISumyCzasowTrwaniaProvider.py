import os.path

import numpy as np
import pandas as pd

from dataset_provider.DatasetProvider import createTextualIndexesOfDataDividedByRanges, \
    DAILY_FLOWS_AND_STATES_IN_YEAR_HEADER, \
    findMinAndMaxValueOfWaterParameterInYearsRange, createStatesForWaterParameter, findMinAndMaxValueOfWaterParameter
from Constants import ORDERED_HYDRO_MONTHS, PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE, TEMP_FOLDER_DIRECTORY


def createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaTable(dataset_for_years, years_range, parameter_name,
                                                                 include_first_row_for_higher_in_frequency_table,
                                                                 common_range_of_states_for_multiannual, save_to_file):
    if common_range_of_states_for_multiannual:
        min_value, max_value = findMinAndMaxValueOfWaterParameterInYearsRange(dataset_for_years, years_range, parameter_name)
        states = createStatesForWaterParameter(min_value, max_value, parameter_name)
        states_as_index = createTextualIndexesOfDataDividedByRanges(states)

    states_in_years = {}
    for current_year in years_range:
        data_table_for_year = dataset_for_years[current_year][DAILY_FLOWS_AND_STATES_IN_YEAR_HEADER]

        if not common_range_of_states_for_multiannual:
            min_value, max_value = findMinAndMaxValueOfWaterParameter(data_table_for_year, parameter_name)
            states = createStatesForWaterParameter(min_value, max_value, parameter_name)
            states_as_index = createTextualIndexesOfDataDividedByRanges(states)

        states_in_year = pd.DataFrame(columns=states_as_index)
        for month in np.arange(1, 13, 1):
            states_for_month = []
            curr_m_df = data_table_for_year[data_table_for_year["MonthHydro"] == float(month)]
            for state in states:
                tmp = curr_m_df[curr_m_df[parameter_name] >= state[0]]
                tmp = tmp[tmp[parameter_name] <= state[1]]
                states_occurs = len(tmp)
                states_for_month = np.append(states_for_month, states_occurs)
            states_in_year.loc[month] = states_for_month

        # SUM PER MONTH
        sum_per_month = []
        states_in_year = states_in_year.T
        for index, row in states_in_year.T.iterrows():
            sum_per_month = np.append(sum_per_month, sum(row))
        states_in_year.loc['sum'] = sum_per_month

        # frequency
        frequency = []
        for index, row in states_in_year.iterrows():
            freq = sum(row)
            frequency = np.append(frequency, freq)
        states_in_year = states_in_year.T
        states_in_year.loc['frequency'] = frequency

        # LOWER
        lower = []
        frequency[-1] = 0
        for i in range(0, len(frequency)):
            lower = np.append(lower, sum(frequency[:i + 1]))
        lower[-1] = 0
        states_in_year.loc['lower'] = lower

        # HIGHER
        higher = []
        days_count = sum(frequency)
        for i in range(0, len(frequency)):
            if not include_first_row_for_higher_in_frequency_table:
                curr_higher = days_count - sum(frequency[1:i + 1])  # omits first row
            else:
                curr_higher = sum(frequency[i:])  # starts from first row
            higher = np.append(higher, curr_higher)
        states_in_year.loc['higher'] = higher
        states_in_year = states_in_year.T

        new_columns = [str(hydro_month) for hydro_month in ORDERED_HYDRO_MONTHS]
        new_columns.extend(['frequency', 'lower', 'higher'])
        states_in_year.columns = new_columns

        states_in_year = states_in_year.astype(
            {"11": int, "12": int, "1": int, "2": int, "3": int, "4": int, "5": int, "6": int, "7": int, "8": int, "9": int, "10": int, "frequency": int,
             "lower": int, "higher": int})

        states_in_years[current_year] = states_in_year
        if save_to_file:
            if parameter_name == 'h_water':
                out_file_name = 'daily states-' + str(current_year) + '.xlsx'
            elif parameter_name == 'Q':
                out_file_name = 'daily flows-' + str(current_year) + '.xlsx'
            else:
                raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)
            out_file_path = os.path.join(TEMP_FOLDER_DIRECTORY, out_file_name)
            writer = pd.ExcelWriter(out_file_path)
            states_in_year.to_excel(writer, index=True)
            writer.save()
    return states_in_years
