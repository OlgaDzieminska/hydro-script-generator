from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

SIGMA_SIGN = '\u03A3'


def __fillAndMergeCells(table, cell_content, start_row_position, start_column_position, row_span, column_span):
    parent_cell = table.cell(start_row_position, start_column_position)
    paragraph = parent_cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.style.font.size = Pt(8)
    run = paragraph.add_run(cell_content)
    run.bold = True
    for row_idx in range(start_row_position, start_row_position + row_span):
        parent_cell = table.cell(row_idx, start_column_position)
        for column_idx in range(start_column_position, start_column_position + column_span):
            parent_cell.merge(table.cell(row_idx, column_idx))
        if row_idx != start_row_position:
            parent_cell.merge(table.cell(row_idx - 1, start_column_position))


def addHeadersToTable(table, headers_definitions):
    for cell_content, start_row_position, start_column_position, row_span, column_span in headers_definitions:
        __fillAndMergeCells(table, cell_content, start_row_position, start_column_position, row_span, column_span)
