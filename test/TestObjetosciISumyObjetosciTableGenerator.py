import os
from random import randint

from docx import Document

from dataset_provider import DatasetProvider
from dataset_provider.DataFrameForObliczenieObjetosciOrazSumObjetosci import createDataFrameForObliczenieObjestosciOrazSumObjetosciTable
from table_generator.ObjetosciISumyObjetosciTableGenerator import appendObliczenieObjetosciISumObjetosciTableToDocument

os.chdir("../")

# User input
my_city = "Nowy Sącz"
my_river = "Dunajec"
years_range = range(1982, 1991 + 1)

# loaded settings from project_settings.json file
include_first_row_for_higher_in_frequency_table = True
common_range_of_states_for_multiannual = True

# test settings
parameter_name = 'Q'

document = Document()
dataset_for_years = DatasetProvider.provideDataForDailyFlowsAndStatesInYears(years_range, my_city, my_river)

df_for_objetosci_i_sumy_objetosci_table = createDataFrameForObliczenieObjestosciOrazSumObjetosciTable(dataset_for_years, save_to_file=False)

appendObliczenieObjetosciISumObjetosciTableToDocument(document, df_for_objetosci_i_sumy_objetosci_table)
doc_name_iter = randint(0, 100)

document_output_filepath = 'temp/' + str(doc_name_iter) + '.docx'
document.save(document_output_filepath)
print('Saved document to:' + document_output_filepath)
