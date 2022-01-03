import os

from docx import Document

from dataset_provider import DataFrameForKrzywaKonsumpcyjna
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears
from operat_report_tests import ReportTestUtils
from operat_report_tests.ReportTestUtils import TEST_CITY_NAME, TEST_RIVER_NAME
from table_generator import KrzywaKonsumpcyjnaTableGenerator

########
os.chdir('../')
years_range = range(1982, 1991 + 1)
document = Document()

dataset_for_years = provideDataForDailyFlowsAndStatesInYears(years_range, TEST_CITY_NAME, TEST_RIVER_NAME)
df_for_krzywa_konsumpcyjna_table = DataFrameForKrzywaKonsumpcyjna.provide(dataset_for_years, years_range)

KrzywaKonsumpcyjnaTableGenerator.appendTable(document, df_for_krzywa_konsumpcyjna_table)

ReportTestUtils.saveTestDocumentFileAndPrintFileName(document)
