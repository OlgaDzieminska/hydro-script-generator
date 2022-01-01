from table_generator import TableGenerator


def __prepareHeadersForObliczenieObjetosciISumObjetosci():
    rok_header = ('Rok', 0, 0, 3, 2)
    miesiac_header = ('Miesiąc', 0, 2, 3, 2)
    liczba_dni_w_miesiacu_header = ('Liczba dni w miesiącu n', 0, 4, 3, 3)
    SQ_header = ('SQ [m\u00B3/s]', 0, 7, 3, 4)
    V_header = ('V [mln m\u00B3]', 0, 11, 3, 4)
    SumV_header = ('\u03a3 V [mln m\u00B3]', 0, 15, 3, 4)

    headers_definitions = [rok_header, miesiac_header, liczba_dni_w_miesiacu_header, SQ_header, V_header, SumV_header]

    return headers_definitions


def __addTableContent(table, table_content):
    for index, table_data_row in table_content.iterrows():
        row_cells = table.add_row().cells
        cell_index_after_year_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, int(table_data_row['year']), 2)
        cell_index_after_month_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_year_cell, int(table_data_row['month']), 2)
        cell_index_after_days_in_month_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_month_cell,
                                                                                            int(table_data_row['days_in_month']), 3)
        cell_index_after_mean_flow_monthly_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_days_in_month_cell,
                                                                                                round(table_data_row['mean_flow_monthly'], 3), 4)
        cell_index_after_mean_V_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_mean_flow_monthly_cell,
                                                                                     round(table_data_row['mean_V'], 2), 4)
        cell_index_after_V_sum_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_mean_V_cell, round(table_data_row['V_sum'], 2),
                                                                                    4)


def appendObliczenieObjetosciISumObjetosciTableToDocument(document, table_content):
    number_of_columns = 19
    number_of_rows_for_headers_cells = 3
    headers_for_obliczenie_objetosci_i_sum_objetosci_table = __prepareHeadersForObliczenieObjetosciISumObjetosci()
    ObliczenieObjetosciISumObjetosci = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    ObliczenieObjetosciISumObjetosci.style = 'Table Grid'

    TableGenerator.addHeadersToTable(ObliczenieObjetosciISumObjetosci, headers_for_obliczenie_objetosci_i_sum_objetosci_table)
    __addTableContent(ObliczenieObjetosciISumObjetosci, table_content)
