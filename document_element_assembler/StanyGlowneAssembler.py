from chart_generator import MainStatesFluctuationCurveForYears
from dataset_provider import DataFrameForStanyGlowne
from document_element_assembler import DocumentAssembler
from table_generator import StanyGlowne1StopniaTableGenerator, StanyGlowne2StopniaTableGenerator


def addStanyGlownePages(document, index_of_element, main_states_first_degree, main_states_second_degree, river_name, city_name, year_from, year_to):
    inner_index_of_element = 1
    years_range = range(year_from, year_to + 1)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    stany_glowne_table_title = 'Stany główne I stopnia w wieloleciu %d-%d, rzeka: %s, przekrój: %s' % (year_from, year_to, river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, stany_glowne_table_title)
    StanyGlowneTable = DataFrameForStanyGlowne.provideDataForYearlyFlowsAndStatesInYearsForFirstDegree(years_range, city_name, river_name, 'h_water')
    StanyGlowne1StopniaTableGenerator.appendStanyGlowneTableToDocument(document, StanyGlowneTable)

    inner_index_of_element += 1
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    stany_glowne_II_stopnia_table_title = 'Stany główne II stopnia w wieloleciu %d-%d, rzeka: %s, przekrój: %s' % (year_from, year_to, river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, stany_glowne_II_stopnia_table_title)
    StanyGlowne2StopniaTableGenerator.appendStanyGlowneIIStopniaTableToDocument(document, main_states_second_degree)

    document.add_page_break()
    inner_index_of_element += 1
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    addMainStatesFluctuationCurveForYears(document, textual_element_index, main_states_first_degree, main_states_second_degree, river_name,
                                          city_name, year_from, year_to)


def addMainStatesFluctuationCurveForYears(document, index_of_element, main_states_first_degree,
                                          main_states_second_degree,
                                          river_name, city_name,
                                          year_from, year_to):
    krzywa_wahan_stanow_glownych_1_stopnia_chart_filename, krzywa_wahan_stanow_glownych_1_stopnia_chart_title = \
        MainStatesFluctuationCurveForYears.printMainStatesFluctuationCurveForYears(
            main_states_first_degree,
            main_states_second_degree,
            river_name, city_name,
            year_from, year_to)
    DocumentAssembler.addHeadingToDocumentElement(document, index_of_element, krzywa_wahan_stanow_glownych_1_stopnia_chart_title)
    DocumentAssembler.addChartToDocument(document, krzywa_wahan_stanow_glownych_1_stopnia_chart_filename)
