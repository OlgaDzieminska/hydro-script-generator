import math
import os

import numpy as np
import pandas as pd

import util
from dataset_repository.IMGWDatasetRepository import DAILY_DATA_CSV_FILE_NAME_TEMPLATE
from main import DAILY_VALUES_INPUT_FILES_DIRECTORY, PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE, TEMP_FOLDER_DIRECTORY

DAILY_FLOWS_AND_STATES_INPUT_FILE_HEADER = ["ID", "City", "River", "YearHydro", "MonthHydro", "day", "h_water", "Q", "temp", "Month"]
YEARLY_STATES_INPUT_FILE_HEADER = ['ID', 'City', 'River', 'YearHydro', 'half_year_indicator', 'parameter_name', 'extremes_indicator',
                                   'parameter_value', 'fom_year', 'fom_month', 'fom_day', 'fom_hour', 'from_minute', 'to_year', 'to_month', 'to_day',
                                   'to_hour', 'to_minute']

DATASET_LACK_OF_DATA = 99999.999
DAILY_FLOWS_AND_STATES_IN_YEAR_HEADER = ['day', "MonthHydro", "h_water", 'Q']


def provideDataForDailyFlowsAndStatesInYears(years_range, city_name, river_name):
    df_years = {}
    for year in years_range:
        df_months = pd.DataFrame()
        for month in np.arange(1, 13, 1):
            file_name = DAILY_DATA_CSV_FILE_NAME_TEMPLATE % (year, month)
            file_path = os.path.join(TEMP_FOLDER_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY, file_name)
            curr_df = __getDataFrameForDailyValues(file_path, city_name, river_name)[DAILY_FLOWS_AND_STATES_IN_YEAR_HEADER]
            max_index = curr_df.index.max() + 1
            curr_df.index = np.arange(max_index, max_index + len(curr_df), 1)
            df_months = df_months.append(curr_df)
        df_months.index = np.arange(0, len(df_months))
        df_years[year] = df_months
    return df_years


def findMinAndMaxValueOfWaterParameterInYearsRange(data_table, years_range, parameter_name):
    if parameter_name == 'h_water':
        return findMinAndMaxValueOfWaterHeightForYearsRange(data_table, years_range)
    if parameter_name == 'Q':
        return findMinAndMaxValueOfFlowForYearsRange(data_table, years_range)
    raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)


def findMinAndMaxValueOfWaterHeightForYearsRange(data_table, years_range):
    min_value = 9999999
    max_value = 0
    for current_year in years_range:
        current_year_values = data_table[current_year]
        curr_min, curr_max = findMinAndMaxValueOfWaterHeight(current_year_values)
        if curr_min < min_value:
            min_value = curr_min
        if curr_max > max_value:
            max_value = curr_max
    return min_value, max_value


def findMinAndMaxValueOfFlowForYearsRange(data_table, years_range):
    min_value = 9999999
    max_value = 0
    for year in years_range:
        current_year = data_table[year]
        curr_min, curr_max = findMinAndMaxValueOfFlow(current_year)
        if curr_min < min_value:
            min_value = curr_min
        if curr_max > max_value:
            max_value = curr_max
    return min_value, max_value


def findMinAndMaxValueOfWaterParameter(data_table_for_year, parameter_name):
    if parameter_name == 'h_water':
        return findMinAndMaxValueOfWaterHeight(data_table_for_year)
    if parameter_name == 'Q':
        return findMinAndMaxValueOfFlow(data_table_for_year)
    raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)


def findMinAndMaxValueOfFlow(data_table_for_year):
    min_value = data_table_for_year['Q'].min()
    max_value = data_table_for_year['Q'].max()
    return min_value, max_value


def findMinAndMaxValueOfWaterHeight(data_table_for_year):
    min_value = data_table_for_year['h_water'].min()
    min_value = 10 * int(min_value / 10)  # take minimum range like 20,50,70...
    max_value = data_table_for_year['h_water'].max()
    return min_value, max_value


def createStatesForWaterParameter(min_value, max_value, parameter_name):
    if parameter_name == 'h_water':
        return createWaterHeightStates(min_value, max_value)
    if parameter_name == 'Q':
        return createFlowStates(min_value, max_value)
    raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)


def createWaterHeightStates(h_min, h_max):
    fromS = np.arange(h_min, h_max + (10 - h_max % 10), 10)
    toS = fromS + 9
    states = np.vstack((fromS, toS)).T
    return states


def createFlowStates(Q_min, Q_max):
    k = 5
    delta = np.log(Q_max) - np.log(Q_min)
    delta_q = []
    delta_Q = [Q_min]
    Q = [Q_min]
    for i in range(1, k):
        Q_prev = Q[i - 1]
        Q_curr = round(Q_min * math.exp((i / (k - 1)) * delta), 1)
        _delta_Q = Q_curr - Q_prev
        _delta_q = round(_delta_Q / k, 1)
        delta_q = np.append(delta_q, _delta_q)
        delta_Q = np.append(delta_Q, _delta_Q)
        Q = np.append(Q, Q_curr)
    intervals = []
    for i in range(0, k - 1):
        curr_Q = Q[i]
        next_Q = Q[i + 1]
        curr_delta_q = delta_q[i]

        start_interval = curr_Q
        end_interval = start_interval + curr_delta_q
        _interval = [start_interval, end_interval]
        intervals = np.append(intervals, _interval)
        for j in range(1, k):
            start_interval = end_interval
            end_interval = start_interval + curr_delta_q
            if j == 1:
                start_interval -= 0.1
            if j == k - 1:
                end_interval = next_Q - 0.2
            _interval = [round(start_interval + 0.2, 1), round(end_interval + 0.1, 1)]
            intervals = np.append(intervals, _interval)
    intervals = intervals.reshape((k - 1) * len(Q), 2)
    intervals[k * (k - 1) - 1, 1] = Q[k - 1]
    return intervals


def createTextualIndexesOfDataDividedByRanges(ranges):
    return [str(state[0]) + '-' + str(state[1]) for (state) in ranges]


def filterRiverNameAndCityNameInInputDataFrame(input_file_df, city_name, river_name):
    river_name_pattern = util.createRegexForRiverNameInInputFile(river_name)
    input_file_df = input_file_df[input_file_df["City"] == city_name.upper()]

    return input_file_df[input_file_df['River'].str.contains(river_name_pattern)]


def __getDataFrameForDailyValues(file_path, city_name, river_name):
    input_file_df = pd.read_csv(file_path, encoding='cp1250', header=None, names=DAILY_FLOWS_AND_STATES_INPUT_FILE_HEADER)
    return filterRiverNameAndCityNameInInputDataFrame(input_file_df, city_name, river_name)
