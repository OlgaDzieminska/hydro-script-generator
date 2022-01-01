import os

from chart_generator.KrzywaSumowaWUkladzieProstokatnym import printKrzywaSumowaWUkladzieProstokatnym
from dataset_provider.DatasetForKrzywaSumowaWUkładzieProstokątnymProvider import provideDatasetForKrzywaSumowaWUkladzieProstokatnym
from dataset_provider.DatasetProvider import provideDataForDailyFlowsAndStatesInYears

os.chdir("../")
# User input
city_name = "NOWY SĄCZ"
river_name = "Dunajec"
years_range = range(1982, 1991 + 1)

# test settings
parameter_name = 'Q'

# download files from internet via DatasetDownloader
# omitted as files were downloaded earlier

# Fetch data from files and compose into dictionary of data frames for each year
dataset_for_years = provideDataForDailyFlowsAndStatesInYears(years_range, city_name, river_name)

dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym = provideDatasetForKrzywaSumowaWUkladzieProstokatnym(dataset_for_years)

printKrzywaSumowaWUkladzieProstokatnym(dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym, years_range)
