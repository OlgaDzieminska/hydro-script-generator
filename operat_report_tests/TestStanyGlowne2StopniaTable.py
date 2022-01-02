import os

from docx import Document

from dataset_provider import DataFrameForStanyGlowne
from operat_report_tests import ReportTestUtils
from table_generator.StanyGlowne2StopniaTableGenerator import appendStanyGlowneIIStopniaTableToDocument

os.chdir('../')
city_name = "NOWY SĄCZ"
river_name = "Dunajec"
years_range = [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991]

# loaded settings from project_settings.json file
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True

# test settings
parameter_name = 'h_water'

operat_document = Document()
# dataset_for_years = DatasetProvider.provideDataForDailyFlowsAndStatesInYears(years_range, city_name, river_name)
main_states_first_degree = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForFirstDegree(years_range, city_name, river_name, parameter_name)
main_states_second_degree = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForSecondDegree(main_states_first_degree)

appendStanyGlowneIIStopniaTableToDocument(operat_document, main_states_second_degree)
ReportTestUtils.saveTestDocumentFileAndPrintFileName(operat_document)
