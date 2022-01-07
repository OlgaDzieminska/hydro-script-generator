from dataset_provider import DataFrameForCiagChronologicznyPrzeplywowMaksymalnych, DataFrameForCiagRozdzielczyPrzeplywowMaksymalnych
from document_element_assembler import DocumentAssembler
from table_generator import CiagChronologicznyTableGenerator, CiagRozdzielczyTableGenerator


def addElements(document, index_of_element, dataset_for_years, year_from, year_to, years_range, river_name, city_name):
    inner_index_of_element = 1

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    stany_glowne_table_title = 'Ciąg chronologiczny przepływów maksymalnych roczny dla okresu %d-%d, rzeka: %s, przekrój: %s' % (
        year_from, year_to, river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, stany_glowne_table_title)
    ciag_chronologiczny_dataset = DataFrameForCiagChronologicznyPrzeplywowMaksymalnych.provide(dataset_for_years, years_range)
    CiagChronologicznyTableGenerator.appendTable(document, ciag_chronologiczny_dataset)

    inner_index_of_element += 1
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    stany_glowne_II_stopnia_table_title = 'Ciąg rozdzielczy malejący przepływów maksymalnych rocznych dla okresu %d-%d, rzeka: %s, przekrój: %s' % (
        year_from, year_to, river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, stany_glowne_II_stopnia_table_title)
    ciag_rozdzielczy_dataset = DataFrameForCiagRozdzielczyPrzeplywowMaksymalnych.provide(dataset_for_years, years_range)
    CiagRozdzielczyTableGenerator.appendTable(document, ciag_rozdzielczy_dataset)
