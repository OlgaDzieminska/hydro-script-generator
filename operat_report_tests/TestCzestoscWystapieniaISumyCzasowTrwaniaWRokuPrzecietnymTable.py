import os

from docx import Document

from ReportTestUtils import MULTIANNUAL_YEARS_RANGE, TEST_CITY_NAME, TEST_RIVER_NAME
from dataset_provider.DataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymProvider import \
    createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTable
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears
from operat_report_tests import ReportTestUtils
from table_generator.CzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymGenerator import \
    appendCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTableToDocument

# loaded settings from project_settings.json file
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True
save_dataFrame_to_file = False

# test settings
parameter_name = 'h_water'

os.chdir('../')
# Fetch data from files and compose into dictionary of data frames for each year
dataset_for_years = provideDataForDailyFlowsAndStatesInYears(MULTIANNUAL_YEARS_RANGE, TEST_CITY_NAME, TEST_RIVER_NAME)

# Create DataFrame for CzestoscWystapieniaISumyCzasowTrwaniaTable (Q and h_water) and other tables and charts
states_in_average_years_dataFrame = createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTable(dataset_for_years, MULTIANNUAL_YEARS_RANGE,
                                                                                                                 parameter_name,
                                                                                                                 include_first_row_for_higher_in_frequency_table,
                                                                                                                 save_dataFrame_to_file)

# Create document
operat_document = Document()

# Append tables and charts to document
appendCzestoscWystapieniaISumyCzasowTrwaniaWRokuPrzecietnymTableToDocument(operat_document, states_in_average_years_dataFrame, MULTIANNUAL_YEARS_RANGE,
                                                                           parameter_name)

# Save document
ReportTestUtils.saveTestDocumentFileAndPrintFileName(operat_document)
