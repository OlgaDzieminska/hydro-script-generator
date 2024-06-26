import os

from docx import Document

from dataset_provider import DatasetProvider, DataFrameForStanyGlowne
from dataset_repository import IMGWDatasetRepository
from operat_report_tests import ReportTestUtils
from table_generator import StanyGlowne1StopniaTableGenerator

os.chdir("../")
# User input
city_name = "Nowy Sącz"
river_name = "Dunajec"
years_range = range(1982, 1991 + 1)

# loaded settings from project_settings.json file
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True

# test settings
parameter_name = 'h_water'

document = Document()
IMGWDatasetRepository.downloadYearlyDatasets(years_range, parameter_name)

dataset_for_years = DatasetProvider.provideDataForDailyFlowsAndStatesInYears(years_range, city_name, river_name)
StanyGlowneTable = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForFirstDegree(years_range, city_name, river_name, parameter_name)

StanyGlowne1StopniaTableGenerator.appendStanyGlowneTableToDocument(document, StanyGlowneTable)

ReportTestUtils.saveTestDocumentFileAndPrintFileName(document)
