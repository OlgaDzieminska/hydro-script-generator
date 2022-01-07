import os

from docx import Document

from dataset_provider import DataFrameForCiagChronologicznyPrzeplywowMaksymalnych, DataFrameForCiagRozdzielczyPrzeplywowMaksymalnych
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears
from operat_report_tests import ReportTestUtils
from operat_report_tests.ReportTestUtils import TEST_CITY_NAME, TEST_RIVER_NAME
from table_generator import CiagChronologicznyTableGenerator, CiagRozdzielczyTableGenerator

years_range = range(1982, 1991 + 1)
operat_document = Document()

########
os.chdir('../')
dataset_for_years = provideDataForDailyFlowsAndStatesInYears(years_range, TEST_CITY_NAME, TEST_RIVER_NAME)

ciag_chronologiczny_dataset = DataFrameForCiagChronologicznyPrzeplywowMaksymalnych.provide(dataset_for_years, years_range)
ciag_rozdzielczy_dataset = DataFrameForCiagRozdzielczyPrzeplywowMaksymalnych.provide(dataset_for_years, years_range)

CiagChronologicznyTableGenerator.appendTable(operat_document, ciag_chronologiczny_dataset)
CiagRozdzielczyTableGenerator.appendTable(operat_document, ciag_rozdzielczy_dataset)
ReportTestUtils.saveTestDocumentFileAndPrintFileName(operat_document)
