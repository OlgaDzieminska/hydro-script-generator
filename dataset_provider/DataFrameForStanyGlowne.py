import os

import pandas as pd

from dataset_provider.DatasetProvider import YEARLY_STATES_INPUT_FILE_HEADER
from dataset_repository.IMGWDatasetRepository import YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_Q, YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_H_WATER
from main import PROGRAM_ROOT_PATH, TEMP_FOLDER_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY, PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE

STANY_GLOWNE_1_STOPNIA_COLUMNS = ['NW', 'SW', 'WW']
STANY_GLOWNE_2_STOPNIA_COLUMNS = ['NNW', 'SNW', 'WNW', 'NSW', 'SSW', 'WSW', 'NWW', 'SWW', 'WWW']

EXTREMES_INDICATOR_FOR_NW = 1
EXTREMES_INDICATOR_FOR_SW = 2
EXTREMES_INDICATOR_FOR_WW = 3


def provideDataForYearlyFlowsAndStatesInYearsForFirstDegree(years_range, city_name, river_name, parameter_name):
    df_years = pd.DataFrame(columns=STANY_GLOWNE_1_STOPNIA_COLUMNS)
    for year in years_range:
        input_file_path = __provideFilePathForYearlyInputDataset(parameter_name, year)
        NW_value, SW_value, WW_value = __getValuesForYearlyValues(input_file_path, city_name, river_name)
        df_years.loc[year] = [NW_value, SW_value, WW_value]
    df_years = df_years.astype({"NW": int, "SW": int, "WW": int})
    addSumRow(df_years)
    return df_years


def addSumRow(df_years):
    NW_sum = sum(df_years['NW'])
    SW_sum = sum(df_years['SW'])
    WW_sum = sum(df_years['WW'])
    df_years.loc['sum'] = [NW_sum, SW_sum, WW_sum]


def __getValuesForYearlyValues(file_path, city_name, river_name):
    df = pd.read_csv(file_path, encoding='cp1250', header=None, names=YEARLY_STATES_INPUT_FILE_HEADER)
    newDF = df[df["City"] == city_name.upper()]
    newDF = newDF[newDF["River"] == river_name]
    NW_value = newDF[newDF['extremes_indicator'] == EXTREMES_INDICATOR_FOR_NW]['parameter_value'].min()
    SW_value = __getValueOfSW(newDF)
    WW_value = newDF[newDF['extremes_indicator'] == EXTREMES_INDICATOR_FOR_WW]['parameter_value'].max()
    return NW_value, SW_value, WW_value


def __getValueOfSW(dataFrame):
    SW_values = dataFrame[dataFrame['extremes_indicator'] == EXTREMES_INDICATOR_FOR_SW]['parameter_value']
    if len(SW_values) == 3:
        SWs = list(SW_values)
        SWs.sort()
        return SWs[1]
    else:
        return int(sum(SW_values) / len(SW_values))


def __provideFilePathForYearlyInputDataset(parameter_name, year):
    if parameter_name == 'h_water':
        file_name = YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_H_WATER % year
        return os.path.join(PROGRAM_ROOT_PATH, TEMP_FOLDER_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY, file_name)
    elif parameter_name == 'Q':
        file_name = YEARLY_DATA_CSV_FILE_NAME_TEMPLATE_Q % year
        return os.path.join(PROGRAM_ROOT_PATH, TEMP_FOLDER_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY, file_name)
    else:
        raise ValueError(PROVIDED_INVALID_WATER_PARAMETER_NAME_ERROR_MESSAGE)


# STANY_GLOWNE_2_STOPNIA_COLUMNS = ['NNW', 'SNW', 'WNW', 'NSW', 'SSW', 'WSW', 'NWW', 'SWW', 'WWW']

def provideDataForYearlyFlowsAndStatesInYearsForSecondDegree(yearly_data_for_first_degree):
    input_df_without_sum = yearly_data_for_first_degree.loc[yearly_data_for_first_degree.index[:-1]]
    df = pd.DataFrame(columns=STANY_GLOWNE_2_STOPNIA_COLUMNS)
    NNW = input_df_without_sum['NW'].min()
    SNW = yearly_data_for_first_degree.loc['sum']['NW'] / (len(input_df_without_sum))
    WNW = input_df_without_sum['NW'].max()

    NSW = input_df_without_sum['SW'].min()
    SSW = yearly_data_for_first_degree.loc['sum']['SW'] / len(input_df_without_sum)
    WSW = input_df_without_sum['SW'].max()

    NWW = input_df_without_sum['WW'].min()
    SWW = yearly_data_for_first_degree.loc['sum']['WW'] / len(input_df_without_sum)
    WWW = input_df_without_sum['WW'].max()

    df.loc[0] = [NNW, SNW, WNW, NSW, SSW, WSW, NWW, SWW, WWW]
    return df
