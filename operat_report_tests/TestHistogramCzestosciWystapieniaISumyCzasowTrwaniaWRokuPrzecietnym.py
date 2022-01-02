import os

from ReportTestUtils import MULTIANNUAL_YEARS_RANGE, TEST_CITY_NAME, TEST_RIVER_NAME
from chart_generator import HistogramCzestosciWystapieniaWRokuPrzecietnym
from dataset_provider import DatasetProvider
from dataset_provider.DataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymProvider import \
    createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTable
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears

# loaded settings from project_settings.json file
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True
save_dataFrame_to_file = False

# test settings
parameter_name = 'Q'

os.chdir('../')
# Fetch data from files and compose into dictionary of data frames for each year
dataset_for_years = provideDataForDailyFlowsAndStatesInYears(MULTIANNUAL_YEARS_RANGE, TEST_CITY_NAME, TEST_RIVER_NAME)

# Create DataFrame for CzestoscWystapieniaISumyCzasowTrwaniaTable (Q and h_water) and other tables and charts
states_in_average_years_dataFrame = createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTable(dataset_for_years, MULTIANNUAL_YEARS_RANGE,
                                                                                                                 parameter_name,
                                                                                                                 include_first_row_for_higher_in_frequency_table,
                                                                                                                 save_dataFrame_to_file)

# print charts
min_value, max_value = DatasetProvider.findMinAndMaxValueOfWaterParameterInYearsRange(dataset_for_years, MULTIANNUAL_YEARS_RANGE, parameter_name)
states = DatasetProvider.createStatesForWaterParameter(min_value, max_value, parameter_name)
HistogramCzestosciWystapieniaWRokuPrzecietnym.printHistogramCzestosciWystapieniaWRokuPrzecietnym(states_in_average_years_dataFrame, states, parameter_name,
                                                                                                 MULTIANNUAL_YEARS_RANGE[0], MULTIANNUAL_YEARS_RANGE[-1],
                                                                                                 TEST_CITY_NAME, TEST_RIVER_NAME)
