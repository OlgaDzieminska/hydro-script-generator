from chart_generator import DailyFlowsAndStatesFluctuationCurveChart
from document_element_assembler import DocumentAssembler


def addElement(document, index_of_element, df_for_year, year_of_chart, river_name, city_name):
    inner_index_of_element = 1

    file_name, chart_name = DailyFlowsAndStatesFluctuationCurveChart.printDailyFlowsAndStatesFluctuationCurveChart(df_for_year['Q'], df_for_year['h_water'],
                                                                                                                   river_name,
                                                                                                                   city_name, year_of_chart)
    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, chart_name)
    DocumentAssembler.addChartToDocument(document, file_name)
