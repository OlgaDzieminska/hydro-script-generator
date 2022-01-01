import os

from docx import Document

from dataset_provider.DataFrameForCzestoscWystapieniaISumyCzasowTrwaniaProvider import createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaTable
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears
from operat_report_tests import ReportTestUtils
from operat_report_tests.ReportTestUtils import TEST_CITY_NAME, TEST_RIVER_NAME
from table_generator.CzestoscWystapieniaISumyCzasowTrwaniaTableGenerator import appendCzestoscWystapieniaISumyCzasowTrwaniaTableToDocument

years_range = range(1982, 1991 + 1)
parameter_name = 'Q'
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True
operat_document = Document()

########
os.chdir('../')
dataset_for_years = provideDataForDailyFlowsAndStatesInYears(years_range, TEST_CITY_NAME, TEST_RIVER_NAME)

dailyFlowsAndStatesInYears = createDataFrameForCzestoscWystapieniaISumyCzasowTrwaniaTable(dataset_for_years, years_range, parameter_name,
                                                                                          include_first_row_for_higher_in_frequency_table,
                                                                                          common_range_of_states_for_multiannual, False)

wet_year = dailyFlowsAndStatesInYears[1986]
appendCzestoscWystapieniaISumyCzasowTrwaniaTableToDocument(operat_document, wet_year, parameter_name)
ReportTestUtils.saveTestDocumentFileAndPrintFileName(operat_document)
