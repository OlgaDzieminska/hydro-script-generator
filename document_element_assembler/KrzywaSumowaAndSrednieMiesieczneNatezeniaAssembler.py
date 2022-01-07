from chart_generator.KrzywaSumowaWUkladzieProstokatnym import printKrzywaSumowaWUkladzieProstokatnym
from dataset_provider.DataFrameForObliczenieObjetosciOrazSumObjetosci import createDataFrameForObliczenieObjestosciOrazSumObjetosciTable
from dataset_provider.DataFrameForSrednieMiesieczneNatezenPrzeplywuProvider import createDataFrameForSrednieMiesieczneNatezeniaPrzeplywuTable
from dataset_provider.DatasetForKrzywaSumowaWUkładzieProstokątnymProvider import provideDatasetForKrzywaSumowaWUkladzieProstokatnym
from document_element_assembler import DocumentAssembler
from table_generator import ObjetosciISumyObjetosciTableGenerator, SrednieMiesieczneNatezeniaPrzeplywuTableGenerator


def addElements(document, index_of_element, dataset_for_years, years_range, river_name, city_name):
    inner_index_of_element = 1
    addKrzywaSumowaChart(document, index_of_element, dataset_for_years, years_range, inner_index_of_element)

    inner_index_of_element += 1
    addZestawienieSrednichMiesiecznychNatezenTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element, river_name, city_name)

    inner_index_of_element += 1
    addObliczenieObjetosciOrazSumObjetosciTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element, river_name, city_name)


def addKrzywaSumowaChart(document, index_of_element, dataset_for_years, years_range, inner_index_of_element):
    dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym = provideDatasetForKrzywaSumowaWUkladzieProstokatnym(dataset_for_years)
    file_name, chart_name = printKrzywaSumowaWUkladzieProstokatnym(dataset_for_chart_krzywa_sumowa_w_ukladzie_prostokatnym, years_range)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, chart_name)
    DocumentAssembler.addChartToDocument(document, file_name)


def addZestawienieSrednichMiesiecznychNatezenTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element, river_name, city_name):
    srednie_miesieczne_dataset = createDataFrameForSrednieMiesieczneNatezeniaPrzeplywuTable(dataset_for_years, False)
    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    table_heading = 'Zestawienie średnich miesięcznych natężeń przepływu dla okresu %d-%d rzeka: %s, przekrój: %s' % (
        years_range[0], years_range[-1], river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, table_heading)
    SrednieMiesieczneNatezeniaPrzeplywuTableGenerator.appendZestawienieSrednichMiesiecznychNatezenPrzeplywuTableToDocument(document, srednie_miesieczne_dataset)


def addObliczenieObjetosciOrazSumObjetosciTable(document, index_of_element, dataset_for_years, years_range, inner_index_of_element, river_name, city_name):
    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    table_heading = 'Obliczenie objętości oraz sum objętości dla okresu %d-%d rzeka: %s, przekrój: %s' % (
        years_range[0], years_range[-1], river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, table_heading)
    df_for_objetosci_i_sumy_objetosci_table = createDataFrameForObliczenieObjestosciOrazSumObjetosciTable(dataset_for_years, save_to_file=False)
    ObjetosciISumyObjetosciTableGenerator.appendObliczenieObjetosciISumObjetosciTableToDocument(document, df_for_objetosci_i_sumy_objetosci_table)
