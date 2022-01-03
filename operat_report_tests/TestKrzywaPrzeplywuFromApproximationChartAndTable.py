import os

from chart_generator import KrzywaPrzeplywuFromApproximation
from dataset_provider import DataFrameForKrzywaKonsumpcyjna
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears
from operat_report_tests.ReportTestUtils import TEST_CITY_NAME, TEST_RIVER_NAME

########
os.chdir('../')
years_range = range(1982, 1991 + 1)

dataset_for_years = provideDataForDailyFlowsAndStatesInYears(years_range, TEST_CITY_NAME, TEST_RIVER_NAME)
df_for_krzywa_konsumpcyjna_table = DataFrameForKrzywaKonsumpcyjna.provide(dataset_for_years, years_range)  #

KrzywaPrzeplywuFromApproximation.generateChart(df_for_krzywa_konsumpcyjna_table)
