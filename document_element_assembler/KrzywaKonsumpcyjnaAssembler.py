from chart_generator import KrzywaPrzeplywuFromApproximation
from dataset_provider import DataFrameForKrzywaKonsumpcyjna
from document_element_assembler import DocumentAssembler
from table_generator import KrzywaKonsumpcyjnaTableGenerator


def addElements(document, index_of_element, dataset_for_years, years_range):
    inner_index_of_element = 1

    inner_index_of_element += 1
    addKrzywaKonsumpcyjnaTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element)

    inner_index_of_element += 1
    addKApproximatedKrzywaKonsumpcyjnaChart(document, index_of_element, dataset_for_years, years_range, inner_index_of_element)


def addKrzywaKonsumpcyjnaTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element):
    df_for_krzywa_konsumpcyjna_table = DataFrameForKrzywaKonsumpcyjna.provide(dataset_for_years, years_range)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    stany_glowne_table_title = 'Aproksymacja krzywej potęgowej metodą najmniejszych kwadratów'
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, stany_glowne_table_title)
    KrzywaKonsumpcyjnaTableGenerator.appendTable(document, df_for_krzywa_konsumpcyjna_table)


def addKApproximatedKrzywaKonsumpcyjnaChart(document, index_of_element, dataset_for_years, years_range, inner_index_of_element):
    df_for_krzywa_konsumpcyjna_table = DataFrameForKrzywaKonsumpcyjna.provide(dataset_for_years, years_range)  #
    approximated_krzywa_przeplywu_chart_filename, krzywa_przeplywu_chart_name = KrzywaPrzeplywuFromApproximation.generateChart(df_for_krzywa_konsumpcyjna_table)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, krzywa_przeplywu_chart_name)
    DocumentAssembler.addChartToDocument(document, approximated_krzywa_przeplywu_chart_filename)
