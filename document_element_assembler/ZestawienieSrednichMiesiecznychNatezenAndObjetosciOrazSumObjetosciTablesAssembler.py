import dataset_provider.DataFrameForSrednieMiesieczneNatezenPrzeplywuProvider as srednieMiesieczneDatasetProvider
import table_generator.SrednieMiesieczneNatezeniaPrzeplywuTableGenerator as srednieMiesieczneTableGenerator
from document_element_assembler import DocumentAssembler


def addElement(document, index_of_element, dataset_for_years, years_range, river_name, city_name):
    inner_index_of_element = 1
    srednie_miesieczne_dataset = srednieMiesieczneDatasetProvider.createDataFrameForSrednieMiesieczneNatezeniaPrzeplywuTable(dataset_for_years, False)

    document.add_page_break()
    textual_element_index = '%d.%d' % (index_of_element, inner_index_of_element)
    table_heading = 'Zestawienie średnich miesięcznych natężeń przepływu dla okresu %d-%d rzeka: %s, przekrój: %s' % (
        years_range[0], years_range[-1], river_name, city_name)
    DocumentAssembler.addHeadingToDocumentElement(document, textual_element_index, table_heading)
    srednieMiesieczneTableGenerator.appendZestawienieSrednichMiesiecznychNatezenPrzeplywuTableToDocument(document, srednie_miesieczne_dataset)
