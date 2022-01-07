import locale

import util
from dataset_provider import DataFrameForStanyGlowne, DatasetProvider
from dataset_repository import IMGWDatasetRepository
from document_element_assembler import DocumentAssembler, KrzywaSumowaAndSrednieMiesieczneNatezeniaAssembler, KrzywaKonsumpcyjnaAssembler, StanyGlowneAssembler, \
    KrzyweSumCzasowTrwaniaAssembler, KrzywaWahanCodziennychIStanowAssembler, PrawdopodobienstwoWystapieniaPrzeplywowMaksymalnychAssembler

# print greetings message and load required data from file and user interface
util.print_greetings()
settings_from_file = util.loadSettingsFromFile()
include_first_row_for_higher_in_frequency_table = settings_from_file['include_first_row_for_higher_in_frequency_table']
common_range_of_states_for_multiannual = settings_from_file['common_range_of_states_for_multiannual']
river_name, city_name, year_from, year_to, year_of_krzywa_wahan_stanow_i_przeplywow_codziennych, first_year_of_multiannual_period = util.fetch_request_data_from_UI()

# prepare variables and directories
locale.getpreferredencoding(do_setlocale=True)
index_of_element = 1
years_range = range(year_from, year_to + 1)
util.createRequiredDirectoriesIfDoesNotExists()

# download data from internet
print('Pobieranie zbioru danych z internetu')
IMGWDatasetRepository.downloadRequiredDataFromInternet(years_range)

# create datasets
print('Generowanie zbioru danych')
dataset_for_years = DatasetProvider.provideDataForDailyFlowsAndStatesInYears(years_range, city_name, river_name)
main_states_first_degree = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForFirstDegree(years_range, city_name, river_name, 'h_water')
main_states_second_degree = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForSecondDegree(main_states_first_degree)

# create and add elements to document in particular order
quantity_of_elements_group = 6
document = DocumentAssembler.createDocumentWithFirstPage(city_name, river_name)

util.printProgressBar(index_of_element, 12, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono', length=50)
StanyGlowneAssembler.addStanyGlownePages(document, index_of_element, main_states_first_degree, main_states_second_degree, river_name,
                                         city_name,
                                         year_from, year_to)
index_of_element += 1
util.printProgressBar(index_of_element, quantity_of_elements_group, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono',
                      length=50)
KrzyweSumCzasowTrwaniaAssembler.addHistogramsAndCzestoscWystapieniaAndSumyCzasowTrwaniaElements(document, index_of_element, main_states_first_degree,
                                                                                                river_name, city_name, first_year_of_multiannual_period,
                                                                                                dataset_for_years,
                                                                                                include_first_row_for_higher_in_frequency_table,
                                                                                                common_range_of_states_for_multiannual)
index_of_element += 1
util.printProgressBar(index_of_element, quantity_of_elements_group, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono',
                      length=50)
KrzywaWahanCodziennychIStanowAssembler.addElement(document, index_of_element, dataset_for_years[year_of_krzywa_wahan_stanow_i_przeplywow_codziennych],
                                                  year_of_krzywa_wahan_stanow_i_przeplywow_codziennych, river_name, city_name)
index_of_element += 1
util.printProgressBar(index_of_element, quantity_of_elements_group, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono',
                      length=50)
KrzywaSumowaAndSrednieMiesieczneNatezeniaAssembler.addElements(document, index_of_element, dataset_for_years, years_range, river_name, city_name)

index_of_element += 1
util.printProgressBar(index_of_element, quantity_of_elements_group, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono',
                      length=50)
KrzywaKonsumpcyjnaAssembler.addElements(document, index_of_element, dataset_for_years, years_range)

index_of_element += 1
util.printProgressBar(index_of_element, quantity_of_elements_group, prefix='Tworzenie i dodawanie tabel i wykresów do dokumentu:', suffix='Ukończono',
                      length=50)
PrawdopodobienstwoWystapieniaPrzeplywowMaksymalnychAssembler.addElements(document, index_of_element, dataset_for_years, year_from, year_to, years_range,
                                                                         river_name, city_name)

print('Zakończono tworzenie operatu.')
# save document
document.save(util.provideOutputFileName())
input('Wciśnij Enter aby zamknąć okno...')
