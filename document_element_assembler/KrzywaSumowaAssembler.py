from chart_generator import KrzywaSumowaWUkladzieProstokatnym as chart_generator
from dataset_provider import DatasetForKrzywaSumowaWUkładzieProstokątnymProvider as dataset_provider
from document_element_assembler import DocumentAssembler


def addElement(document, index_of_element, dataset_for_years, years_range):
    inner_index_of_element = 1

    dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym = dataset_provider.provideDatasetForKrzywaSumowaWUkladzieProstokatnym(dataset_for_years)
    file_name, chart_name = chart_generator.printKrzywaSumowaWUkladzieProstokatnym(dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym, years_range)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, chart_name)
    DocumentAssembler.addChartToDocument(document, file_name)
