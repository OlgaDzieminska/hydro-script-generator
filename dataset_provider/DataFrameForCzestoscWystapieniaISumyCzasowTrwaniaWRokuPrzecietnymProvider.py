import os.path

import numpy as np
import pandas as pd

from dataset_provider.DatasetProvider import createTextualIndexesOfDataDividedByRanges, \
    findMinAndMaxValueOfWaterParameterInYearsRange, \
    createStatesForWaterParameter
from Constants import PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE, TEMP_FOLDER_DIRECTORY


def createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTable(dataset_for_years, years_range, parameter_name,
                                                                                 include_first_row_for_higher_in_frequency_table, save_to_file):
    output_dataframe = pd.DataFrame(columns=np.append(years_range, ['frequency', 'average year']))
    min_value, max_value = findMinAndMaxValueOfWaterParameterInYearsRange(dataset_for_years, years_range, parameter_name)
    states = createStatesForWaterParameter(min_value, max_value, parameter_name)
    states_as_index = createTextualIndexesOfDataDividedByRanges(states)

    for current_state in states:
        years_values_for_state = []
        for current_year in years_range:
            dataset_for_year = dataset_for_years[current_year][parameter_name]

            values_in_range_of_current_state = dataset_for_year[dataset_for_year >= current_state[0]]
            values_in_range_of_current_state = values_in_range_of_current_state[values_in_range_of_current_state <= current_state[1]]
            states_occurs = len(values_in_range_of_current_state)
            years_values_for_state = np.append(years_values_for_state, states_occurs)
        frequency_of_state = np.sum(years_values_for_state)
        mean_value_for_average_year = frequency_of_state / len(years_range)

        output_dataframe.loc[str(current_state)] = np.append(years_values_for_state, [frequency_of_state, mean_value_for_average_year])
    # LOWER
    lower = []
    for index, row in output_dataframe.iterrows():
        curr_lower = np.sum(output_dataframe['average year'][:index])
        lower = np.append(lower, curr_lower)
    output_dataframe['lower'] = lower

    # HIGHER
    higher = []
    average_year = output_dataframe['average year']
    days_count = sum(average_year)
    for i in range(0, len(average_year)):
        if not include_first_row_for_higher_in_frequency_table:
            curr_higher = days_count - sum(average_year[1:i + 1])
        else:
            curr_higher = sum(average_year[i:])

        higher = np.append(higher, curr_higher)

    output_dataframe = output_dataframe.T
    output_dataframe.loc['higher'] = higher
    output_dataframe = output_dataframe.T

    sum_of_years = []
    for current_year in years_range:
        sum_of_years = np.append(sum_of_years, np.sum(output_dataframe[str(current_year)]))

    sum_of_years = np.append(sum_of_years, 0)
    sum_of_years = np.append(sum_of_years, np.sum(output_dataframe['average year']))
    sum_of_years = np.append(sum_of_years, 0)
    sum_of_years = np.append(sum_of_years, 0)
    output_dataframe.loc['sum'] = sum_of_years

    states_as_index.append('sum')
    output_dataframe.index = states_as_index
    if save_to_file:
        if parameter_name == 'Q':
            file_name = 'Average flows for years ' + str(years_range[0]) + '-' + str(years_range[-1]) + '.xlsx'
        elif parameter_name == 'h_water':
            file_name = 'Average water states for years ' + str(years_range[0]) + '-' + str(years_range[-1]) + '.xlsx'
        else:
            raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)
        out_file_path = os.path.join(TEMP_FOLDER_DIRECTORY, file_name)
        writer = pd.ExcelWriter(out_file_path)
        output_dataframe.to_excel(writer, index=True)
        writer.save()
    return output_dataframe
