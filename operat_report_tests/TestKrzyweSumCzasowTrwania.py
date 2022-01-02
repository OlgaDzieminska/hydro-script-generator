import os

from ReportTestUtils import MULTIANNUAL_YEARS_RANGE, TEST_CITY_NAME, TEST_RIVER_NAME
from chart_generator import KrzyweSumCzasowTrwania
from dataset_provider.DataFrameForCzestoscWystapieniaISumyCzasowTrwaniaProvider import createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaTable
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

daily_flows_and_states_in_years = createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaTable(dataset_for_years, MULTIANNUAL_YEARS_RANGE, parameter_name,
                                                                                               include_first_row_for_higher_in_frequency_table,
                                                                                               common_range_of_states_for_multiannual, False)
dry_year = 1987
wet_year = 1986
wet_year_df = daily_flows_and_states_in_years[1986]
dry_year_df = daily_flows_and_states_in_years[1987]

KrzyweSumCzasowTrwania.createChart(dry_year_df, wet_year_df, states_in_average_years_dataFrame, parameter_name, dry_year, wet_year, TEST_CITY_NAME,
                                   TEST_RIVER_NAME)
