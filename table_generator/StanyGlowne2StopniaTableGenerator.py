from table_generator import TableGenerator
from table_generator.TableGenerator import addHeadersToTable


def prepareHeadersForStanyGlowneIIStopnia():
    NNW_header = ('NNW', 0, 0, 3, 2)
    SNW_header = ('SNW', 0, 2, 3, 2)
    WNW_header = ('WNW', 0, 4, 3, 2)
    NSW_header = ('NSW', 0, 6, 3, 2)
    SSW_header = ('SSW', 0, 8, 3, 2)
    WSW_header = ('WSW', 0, 10, 3, 2)
    NWW_header = ('NWW', 0, 12, 3, 2)
    SWW_header = ('SWW', 0, 14, 3, 2)
    WWW_header = ('WWW', 0, 16, 3, 2)
    headers_definitions = [NNW_header, SNW_header, WNW_header, NSW_header, SSW_header, WSW_header, NWW_header, SWW_header, WWW_header]

    return headers_definitions


def __addTableContent(table, table_data_row):
    row_cells = table.add_row().cells
    cell_index_after_nnw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, omitZerosInInteger(table_data_row['NNW'][0]), 2)
    cell_index_after_snw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_nnw_cell, omitZerosInInteger(table_data_row['SNW'][0]), 2)
    cell_index_after_wnw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_snw_cell, omitZerosInInteger(table_data_row['WNW'][0]), 2)
    cell_index_after_nsw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_wnw_cell, omitZerosInInteger(table_data_row['NSW'][0]), 2)
    cell_index_after_ssw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_nsw_cell, omitZerosInInteger(table_data_row['SSW'][0]), 2)
    cell_index_after_wsw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_ssw_cell, omitZerosInInteger(table_data_row['WSW'][0]), 2)
    cell_index_after_nww_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_wsw_cell, omitZerosInInteger(table_data_row['NWW'][0]), 2)
    cell_index_after_sww_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_nww_cell, omitZerosInInteger(table_data_row['SWW'][0]), 2)
    cell_index_after_www_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_sww_cell, omitZerosInInteger(table_data_row['WWW'][0]), 2)


def omitZerosInInteger(number_in_cell):
    if number_in_cell == int(number_in_cell):
        return int(number_in_cell)
    return number_in_cell


def appendStanyGlowneIIStopniaTableToDocument(document, table_content):
    number_of_columns = 18
    number_of_rows_for_headers_cells = 3
    headers_for_stany_glowne_II_stopnia_table = prepareHeadersForStanyGlowneIIStopnia()
    StanyGlowneIIStopniaTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    StanyGlowneIIStopniaTable.style = 'Table Grid'

    addHeadersToTable(StanyGlowneIIStopniaTable, headers_for_stany_glowne_II_stopnia_table)
    __addTableContent(StanyGlowneIIStopniaTable, table_content)
