# coding: utf-8

# flake8: noqa
"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from cloudmersive_convert_api_client.models.add_pdf_annotation_request import AddPdfAnnotationRequest
from cloudmersive_convert_api_client.models.alternate_file_format_candidate import AlternateFileFormatCandidate
from cloudmersive_convert_api_client.models.append_xlsx_row_request import AppendXlsxRowRequest
from cloudmersive_convert_api_client.models.append_xlsx_row_response import AppendXlsxRowResponse
from cloudmersive_convert_api_client.models.autodetect_document_validation_result import AutodetectDocumentValidationResult
from cloudmersive_convert_api_client.models.autodetect_get_info_result import AutodetectGetInfoResult
from cloudmersive_convert_api_client.models.autodetect_to_jpg_result import AutodetectToJpgResult
from cloudmersive_convert_api_client.models.autodetect_to_png_result import AutodetectToPngResult
from cloudmersive_convert_api_client.models.autodetect_to_thumbnails_result import AutodetectToThumbnailsResult
from cloudmersive_convert_api_client.models.base64_decode_request import Base64DecodeRequest
from cloudmersive_convert_api_client.models.base64_decode_response import Base64DecodeResponse
from cloudmersive_convert_api_client.models.base64_detect_request import Base64DetectRequest
from cloudmersive_convert_api_client.models.base64_detect_response import Base64DetectResponse
from cloudmersive_convert_api_client.models.base64_encode_request import Base64EncodeRequest
from cloudmersive_convert_api_client.models.base64_encode_response import Base64EncodeResponse
from cloudmersive_convert_api_client.models.change_line_ending_response import ChangeLineEndingResponse
from cloudmersive_convert_api_client.models.clear_xlsx_cell_request import ClearXlsxCellRequest
from cloudmersive_convert_api_client.models.clear_xlsx_cell_response import ClearXlsxCellResponse
from cloudmersive_convert_api_client.models.clear_xlsx_row_request import ClearXlsxRowRequest
from cloudmersive_convert_api_client.models.clear_xlsx_row_response import ClearXlsxRowResponse
from cloudmersive_convert_api_client.models.converted_jpg_page import ConvertedJpgPage
from cloudmersive_convert_api_client.models.converted_png_page import ConvertedPngPage
from cloudmersive_convert_api_client.models.create_blank_docx_request import CreateBlankDocxRequest
from cloudmersive_convert_api_client.models.create_blank_docx_response import CreateBlankDocxResponse
from cloudmersive_convert_api_client.models.create_blank_spreadsheet_request import CreateBlankSpreadsheetRequest
from cloudmersive_convert_api_client.models.create_blank_spreadsheet_response import CreateBlankSpreadsheetResponse
from cloudmersive_convert_api_client.models.create_spreadsheet_from_data_request import CreateSpreadsheetFromDataRequest
from cloudmersive_convert_api_client.models.create_spreadsheet_from_data_response import CreateSpreadsheetFromDataResponse
from cloudmersive_convert_api_client.models.create_zip_archive_request import CreateZipArchiveRequest
from cloudmersive_convert_api_client.models.csv_collection import CsvCollection
from cloudmersive_convert_api_client.models.csv_file_result import CsvFileResult
from cloudmersive_convert_api_client.models.delete_docx_table_row_range_request import DeleteDocxTableRowRangeRequest
from cloudmersive_convert_api_client.models.delete_docx_table_row_range_response import DeleteDocxTableRowRangeResponse
from cloudmersive_convert_api_client.models.delete_docx_table_row_request import DeleteDocxTableRowRequest
from cloudmersive_convert_api_client.models.delete_docx_table_row_response import DeleteDocxTableRowResponse
from cloudmersive_convert_api_client.models.detect_line_endings_response import DetectLineEndingsResponse
from cloudmersive_convert_api_client.models.disable_shared_workbook_request import DisableSharedWorkbookRequest
from cloudmersive_convert_api_client.models.disable_shared_workbook_response import DisableSharedWorkbookResponse
from cloudmersive_convert_api_client.models.document_validation_error import DocumentValidationError
from cloudmersive_convert_api_client.models.document_validation_result import DocumentValidationResult
from cloudmersive_convert_api_client.models.docx_body import DocxBody
from cloudmersive_convert_api_client.models.docx_cell_style import DocxCellStyle
from cloudmersive_convert_api_client.models.docx_comment import DocxComment
from cloudmersive_convert_api_client.models.docx_footer import DocxFooter
from cloudmersive_convert_api_client.models.docx_header import DocxHeader
from cloudmersive_convert_api_client.models.docx_image import DocxImage
from cloudmersive_convert_api_client.models.docx_insert_comment_on_paragraph_request import DocxInsertCommentOnParagraphRequest
from cloudmersive_convert_api_client.models.docx_insert_image_request import DocxInsertImageRequest
from cloudmersive_convert_api_client.models.docx_insert_image_response import DocxInsertImageResponse
from cloudmersive_convert_api_client.models.docx_metadata_custom_property import DocxMetadataCustomProperty
from cloudmersive_convert_api_client.models.docx_page import DocxPage
from cloudmersive_convert_api_client.models.docx_paragraph import DocxParagraph
from cloudmersive_convert_api_client.models.docx_remove_object_request import DocxRemoveObjectRequest
from cloudmersive_convert_api_client.models.docx_remove_object_response import DocxRemoveObjectResponse
from cloudmersive_convert_api_client.models.docx_run import DocxRun
from cloudmersive_convert_api_client.models.docx_section import DocxSection
from cloudmersive_convert_api_client.models.docx_set_custom_metadata_properties_request import DocxSetCustomMetadataPropertiesRequest
from cloudmersive_convert_api_client.models.docx_set_footer_add_page_number_request import DocxSetFooterAddPageNumberRequest
from cloudmersive_convert_api_client.models.docx_set_footer_request import DocxSetFooterRequest
from cloudmersive_convert_api_client.models.docx_set_footer_response import DocxSetFooterResponse
from cloudmersive_convert_api_client.models.docx_set_header_request import DocxSetHeaderRequest
from cloudmersive_convert_api_client.models.docx_set_header_response import DocxSetHeaderResponse
from cloudmersive_convert_api_client.models.docx_style import DocxStyle
from cloudmersive_convert_api_client.models.docx_table import DocxTable
from cloudmersive_convert_api_client.models.docx_table_cell import DocxTableCell
from cloudmersive_convert_api_client.models.docx_table_row import DocxTableRow
from cloudmersive_convert_api_client.models.docx_template_application_request import DocxTemplateApplicationRequest
from cloudmersive_convert_api_client.models.docx_template_operation import DocxTemplateOperation
from cloudmersive_convert_api_client.models.docx_text import DocxText
from cloudmersive_convert_api_client.models.docx_to_jpg_result import DocxToJpgResult
from cloudmersive_convert_api_client.models.docx_to_png_result import DocxToPngResult
from cloudmersive_convert_api_client.models.docx_top_level_comment import DocxTopLevelComment
from cloudmersive_convert_api_client.models.eml_attachment import EmlAttachment
from cloudmersive_convert_api_client.models.eml_to_html_result import EmlToHtmlResult
from cloudmersive_convert_api_client.models.eml_to_jpg_result import EmlToJpgResult
from cloudmersive_convert_api_client.models.eml_to_png_result import EmlToPngResult
from cloudmersive_convert_api_client.models.enable_shared_workbook_request import EnableSharedWorkbookRequest
from cloudmersive_convert_api_client.models.enable_shared_workbook_response import EnableSharedWorkbookResponse
from cloudmersive_convert_api_client.models.exif_value import ExifValue
from cloudmersive_convert_api_client.models.find_docx_paragraph_request import FindDocxParagraphRequest
from cloudmersive_convert_api_client.models.find_docx_paragraph_response import FindDocxParagraphResponse
from cloudmersive_convert_api_client.models.find_regex_match import FindRegexMatch
from cloudmersive_convert_api_client.models.find_string_match import FindStringMatch
from cloudmersive_convert_api_client.models.find_string_regex_request import FindStringRegexRequest
from cloudmersive_convert_api_client.models.find_string_regex_response import FindStringRegexResponse
from cloudmersive_convert_api_client.models.find_string_simple_request import FindStringSimpleRequest
from cloudmersive_convert_api_client.models.find_string_simple_response import FindStringSimpleResponse
from cloudmersive_convert_api_client.models.finish_editing_request import FinishEditingRequest
from cloudmersive_convert_api_client.models.get_docx_body_request import GetDocxBodyRequest
from cloudmersive_convert_api_client.models.get_docx_body_response import GetDocxBodyResponse
from cloudmersive_convert_api_client.models.get_docx_comments_hierarchical_response import GetDocxCommentsHierarchicalResponse
from cloudmersive_convert_api_client.models.get_docx_comments_response import GetDocxCommentsResponse
from cloudmersive_convert_api_client.models.get_docx_get_comments_hierarchical_request import GetDocxGetCommentsHierarchicalRequest
from cloudmersive_convert_api_client.models.get_docx_get_comments_request import GetDocxGetCommentsRequest
from cloudmersive_convert_api_client.models.get_docx_headers_and_footers_request import GetDocxHeadersAndFootersRequest
from cloudmersive_convert_api_client.models.get_docx_headers_and_footers_response import GetDocxHeadersAndFootersResponse
from cloudmersive_convert_api_client.models.get_docx_images_request import GetDocxImagesRequest
from cloudmersive_convert_api_client.models.get_docx_images_response import GetDocxImagesResponse
from cloudmersive_convert_api_client.models.get_docx_metadata_properties_response import GetDocxMetadataPropertiesResponse
from cloudmersive_convert_api_client.models.get_docx_pages_request import GetDocxPagesRequest
from cloudmersive_convert_api_client.models.get_docx_pages_response import GetDocxPagesResponse
from cloudmersive_convert_api_client.models.get_docx_sections_request import GetDocxSectionsRequest
from cloudmersive_convert_api_client.models.get_docx_sections_response import GetDocxSectionsResponse
from cloudmersive_convert_api_client.models.get_docx_styles_request import GetDocxStylesRequest
from cloudmersive_convert_api_client.models.get_docx_styles_response import GetDocxStylesResponse
from cloudmersive_convert_api_client.models.get_docx_table_by_index_request import GetDocxTableByIndexRequest
from cloudmersive_convert_api_client.models.get_docx_table_by_index_response import GetDocxTableByIndexResponse
from cloudmersive_convert_api_client.models.get_docx_table_row_request import GetDocxTableRowRequest
from cloudmersive_convert_api_client.models.get_docx_table_row_response import GetDocxTableRowResponse
from cloudmersive_convert_api_client.models.get_docx_tables_request import GetDocxTablesRequest
from cloudmersive_convert_api_client.models.get_docx_tables_response import GetDocxTablesResponse
from cloudmersive_convert_api_client.models.get_file_type_icon_result import GetFileTypeIconResult
from cloudmersive_convert_api_client.models.get_image_info_result import GetImageInfoResult
from cloudmersive_convert_api_client.models.get_macros_response import GetMacrosResponse
from cloudmersive_convert_api_client.models.get_pdf_annotations_result import GetPdfAnnotationsResult
from cloudmersive_convert_api_client.models.get_xlsx_cell_by_identifier_request import GetXlsxCellByIdentifierRequest
from cloudmersive_convert_api_client.models.get_xlsx_cell_by_identifier_response import GetXlsxCellByIdentifierResponse
from cloudmersive_convert_api_client.models.get_xlsx_cell_request import GetXlsxCellRequest
from cloudmersive_convert_api_client.models.get_xlsx_cell_response import GetXlsxCellResponse
from cloudmersive_convert_api_client.models.get_xlsx_columns_request import GetXlsxColumnsRequest
from cloudmersive_convert_api_client.models.get_xlsx_columns_response import GetXlsxColumnsResponse
from cloudmersive_convert_api_client.models.get_xlsx_images_request import GetXlsxImagesRequest
from cloudmersive_convert_api_client.models.get_xlsx_images_response import GetXlsxImagesResponse
from cloudmersive_convert_api_client.models.get_xlsx_rows_and_cells_request import GetXlsxRowsAndCellsRequest
from cloudmersive_convert_api_client.models.get_xlsx_rows_and_cells_response import GetXlsxRowsAndCellsResponse
from cloudmersive_convert_api_client.models.get_xlsx_specific_row_request import GetXlsxSpecificRowRequest
from cloudmersive_convert_api_client.models.get_xlsx_specific_row_response import GetXlsxSpecificRowResponse
from cloudmersive_convert_api_client.models.get_xlsx_styles_request import GetXlsxStylesRequest
from cloudmersive_convert_api_client.models.get_xlsx_styles_response import GetXlsxStylesResponse
from cloudmersive_convert_api_client.models.get_xlsx_worksheets_request import GetXlsxWorksheetsRequest
from cloudmersive_convert_api_client.models.get_xlsx_worksheets_response import GetXlsxWorksheetsResponse
from cloudmersive_convert_api_client.models.html_get_language_result import HtmlGetLanguageResult
from cloudmersive_convert_api_client.models.html_get_links_response import HtmlGetLinksResponse
from cloudmersive_convert_api_client.models.html_get_rel_canonical_url_result import HtmlGetRelCanonicalUrlResult
from cloudmersive_convert_api_client.models.html_get_sitemap_url_result import HtmlGetSitemapUrlResult
from cloudmersive_convert_api_client.models.html_hyperlink import HtmlHyperlink
from cloudmersive_convert_api_client.models.html_md_result import HtmlMdResult
from cloudmersive_convert_api_client.models.html_ssrf_threat_check_result import HtmlSsrfThreatCheckResult
from cloudmersive_convert_api_client.models.html_template_application_request import HtmlTemplateApplicationRequest
from cloudmersive_convert_api_client.models.html_template_application_response import HtmlTemplateApplicationResponse
from cloudmersive_convert_api_client.models.html_template_operation import HtmlTemplateOperation
from cloudmersive_convert_api_client.models.html_threat_link import HtmlThreatLink
from cloudmersive_convert_api_client.models.html_to_office_request import HtmlToOfficeRequest
from cloudmersive_convert_api_client.models.html_to_pdf_request import HtmlToPdfRequest
from cloudmersive_convert_api_client.models.html_to_png_request import HtmlToPngRequest
from cloudmersive_convert_api_client.models.html_to_text_request import HtmlToTextRequest
from cloudmersive_convert_api_client.models.html_to_text_response import HtmlToTextResponse
from cloudmersive_convert_api_client.models.insert_docx_comment_on_paragraph_response import InsertDocxCommentOnParagraphResponse
from cloudmersive_convert_api_client.models.insert_docx_insert_paragraph_request import InsertDocxInsertParagraphRequest
from cloudmersive_convert_api_client.models.insert_docx_insert_paragraph_response import InsertDocxInsertParagraphResponse
from cloudmersive_convert_api_client.models.insert_docx_table_row_request import InsertDocxTableRowRequest
from cloudmersive_convert_api_client.models.insert_docx_table_row_response import InsertDocxTableRowResponse
from cloudmersive_convert_api_client.models.insert_docx_tables_request import InsertDocxTablesRequest
from cloudmersive_convert_api_client.models.insert_docx_tables_response import InsertDocxTablesResponse
from cloudmersive_convert_api_client.models.insert_xlsx_worksheet_request import InsertXlsxWorksheetRequest
from cloudmersive_convert_api_client.models.insert_xlsx_worksheet_response import InsertXlsxWorksheetResponse
from cloudmersive_convert_api_client.models.keynote_to_jpg_result import KeynoteToJpgResult
from cloudmersive_convert_api_client.models.keynote_to_png_result import KeynoteToPngResult
from cloudmersive_convert_api_client.models.msg_attachment import MsgAttachment
from cloudmersive_convert_api_client.models.msg_to_html_result import MsgToHtmlResult
from cloudmersive_convert_api_client.models.msg_to_jpg_result import MsgToJpgResult
from cloudmersive_convert_api_client.models.msg_to_png_result import MsgToPngResult
from cloudmersive_convert_api_client.models.multi_replace_string_request import MultiReplaceStringRequest
from cloudmersive_convert_api_client.models.multipage_image_format_conversion_result import MultipageImageFormatConversionResult
from cloudmersive_convert_api_client.models.odp_to_jpg_result import OdpToJpgResult
from cloudmersive_convert_api_client.models.odp_to_png_result import OdpToPngResult
from cloudmersive_convert_api_client.models.ods_to_jpg_result import OdsToJpgResult
from cloudmersive_convert_api_client.models.ods_to_png_result import OdsToPngResult
from cloudmersive_convert_api_client.models.odt_to_jpg_result import OdtToJpgResult
from cloudmersive_convert_api_client.models.odt_to_png_result import OdtToPngResult
from cloudmersive_convert_api_client.models.page_conversion_result import PageConversionResult
from cloudmersive_convert_api_client.models.pdf_annotation import PdfAnnotation
from cloudmersive_convert_api_client.models.pdf_document import PdfDocument
from cloudmersive_convert_api_client.models.pdf_form_field import PdfFormField
from cloudmersive_convert_api_client.models.pdf_form_fields import PdfFormFields
from cloudmersive_convert_api_client.models.pdf_metadata import PdfMetadata
from cloudmersive_convert_api_client.models.pdf_page_text import PdfPageText
from cloudmersive_convert_api_client.models.pdf_text_by_page_result import PdfTextByPageResult
from cloudmersive_convert_api_client.models.pdf_to_jpg_result import PdfToJpgResult
from cloudmersive_convert_api_client.models.pdf_to_png_result import PdfToPngResult
from cloudmersive_convert_api_client.models.pptx_to_png_result import PptxToPngResult
from cloudmersive_convert_api_client.models.presentation_result import PresentationResult
from cloudmersive_convert_api_client.models.remove_docx_headers_and_footers_request import RemoveDocxHeadersAndFootersRequest
from cloudmersive_convert_api_client.models.remove_docx_headers_and_footers_response import RemoveDocxHeadersAndFootersResponse
from cloudmersive_convert_api_client.models.remove_docx_pages_request import RemoveDocxPagesRequest
from cloudmersive_convert_api_client.models.remove_html_from_text_request import RemoveHtmlFromTextRequest
from cloudmersive_convert_api_client.models.remove_html_from_text_response import RemoveHtmlFromTextResponse
from cloudmersive_convert_api_client.models.remove_pptx_slides_request import RemovePptxSlidesRequest
from cloudmersive_convert_api_client.models.remove_whitespace_from_text_request import RemoveWhitespaceFromTextRequest
from cloudmersive_convert_api_client.models.remove_whitespace_from_text_response import RemoveWhitespaceFromTextResponse
from cloudmersive_convert_api_client.models.remove_xlsx_worksheet_request import RemoveXlsxWorksheetRequest
from cloudmersive_convert_api_client.models.rename_xlsx_worksheet_request import RenameXlsxWorksheetRequest
from cloudmersive_convert_api_client.models.rename_xlsx_worksheet_response import RenameXlsxWorksheetResponse
from cloudmersive_convert_api_client.models.replace_docx_paragraph_request import ReplaceDocxParagraphRequest
from cloudmersive_convert_api_client.models.replace_docx_paragraph_response import ReplaceDocxParagraphResponse
from cloudmersive_convert_api_client.models.replace_string_regex_request import ReplaceStringRegexRequest
from cloudmersive_convert_api_client.models.replace_string_regex_response import ReplaceStringRegexResponse
from cloudmersive_convert_api_client.models.replace_string_request import ReplaceStringRequest
from cloudmersive_convert_api_client.models.replace_string_simple_request import ReplaceStringSimpleRequest
from cloudmersive_convert_api_client.models.replace_string_simple_response import ReplaceStringSimpleResponse
from cloudmersive_convert_api_client.models.rtf_to_jpg_result import RtfToJpgResult
from cloudmersive_convert_api_client.models.rtf_to_png_result import RtfToPngResult
from cloudmersive_convert_api_client.models.screenshot_request import ScreenshotRequest
from cloudmersive_convert_api_client.models.set_form_field_value import SetFormFieldValue
from cloudmersive_convert_api_client.models.set_pdf_form_fields_request import SetPdfFormFieldsRequest
from cloudmersive_convert_api_client.models.set_pdf_metadata_request import SetPdfMetadataRequest
from cloudmersive_convert_api_client.models.set_xlsx_cell_by_identifier_request import SetXlsxCellByIdentifierRequest
from cloudmersive_convert_api_client.models.set_xlsx_cell_by_identifier_response import SetXlsxCellByIdentifierResponse
from cloudmersive_convert_api_client.models.set_xlsx_cell_request import SetXlsxCellRequest
from cloudmersive_convert_api_client.models.set_xlsx_cell_response import SetXlsxCellResponse
from cloudmersive_convert_api_client.models.single_replace_string import SingleReplaceString
from cloudmersive_convert_api_client.models.split_document_result import SplitDocumentResult
from cloudmersive_convert_api_client.models.split_docx_document_result import SplitDocxDocumentResult
from cloudmersive_convert_api_client.models.split_pdf_result import SplitPdfResult
from cloudmersive_convert_api_client.models.split_pptx_presentation_result import SplitPptxPresentationResult
from cloudmersive_convert_api_client.models.split_text_document_by_lines_result import SplitTextDocumentByLinesResult
from cloudmersive_convert_api_client.models.split_text_document_by_string_result import SplitTextDocumentByStringResult
from cloudmersive_convert_api_client.models.split_xlsx_worksheet_result import SplitXlsxWorksheetResult
from cloudmersive_convert_api_client.models.text_conversion_result import TextConversionResult
from cloudmersive_convert_api_client.models.text_document_element import TextDocumentElement
from cloudmersive_convert_api_client.models.text_document_line import TextDocumentLine
from cloudmersive_convert_api_client.models.text_encoding_detect_response import TextEncodingDetectResponse
from cloudmersive_convert_api_client.models.thumbnail import Thumbnail
from cloudmersive_convert_api_client.models.update_docx_table_cell_request import UpdateDocxTableCellRequest
from cloudmersive_convert_api_client.models.update_docx_table_cell_response import UpdateDocxTableCellResponse
from cloudmersive_convert_api_client.models.update_docx_table_row_request import UpdateDocxTableRowRequest
from cloudmersive_convert_api_client.models.update_docx_table_row_response import UpdateDocxTableRowResponse
from cloudmersive_convert_api_client.models.url_to_pdf_request import UrlToPdfRequest
from cloudmersive_convert_api_client.models.url_to_text_request import UrlToTextRequest
from cloudmersive_convert_api_client.models.url_to_text_response import UrlToTextResponse
from cloudmersive_convert_api_client.models.viewer_response import ViewerResponse
from cloudmersive_convert_api_client.models.worksheet_result import WorksheetResult
from cloudmersive_convert_api_client.models.xlsx_image import XlsxImage
from cloudmersive_convert_api_client.models.xlsx_spreadsheet_cell import XlsxSpreadsheetCell
from cloudmersive_convert_api_client.models.xlsx_spreadsheet_column import XlsxSpreadsheetColumn
from cloudmersive_convert_api_client.models.xlsx_spreadsheet_row import XlsxSpreadsheetRow
from cloudmersive_convert_api_client.models.xlsx_to_png_result import XlsxToPngResult
from cloudmersive_convert_api_client.models.xlsx_worksheet import XlsxWorksheet
from cloudmersive_convert_api_client.models.xml_add_attribute_with_x_path_result import XmlAddAttributeWithXPathResult
from cloudmersive_convert_api_client.models.xml_add_child_with_x_path_result import XmlAddChildWithXPathResult
from cloudmersive_convert_api_client.models.xml_filter_with_x_path_result import XmlFilterWithXPathResult
from cloudmersive_convert_api_client.models.xml_query_with_x_query_multi_result import XmlQueryWithXQueryMultiResult
from cloudmersive_convert_api_client.models.xml_query_with_x_query_result import XmlQueryWithXQueryResult
from cloudmersive_convert_api_client.models.xml_remove_all_children_with_x_path_result import XmlRemoveAllChildrenWithXPathResult
from cloudmersive_convert_api_client.models.xml_remove_with_x_path_result import XmlRemoveWithXPathResult
from cloudmersive_convert_api_client.models.xml_replace_with_x_path_result import XmlReplaceWithXPathResult
from cloudmersive_convert_api_client.models.xml_set_value_with_x_path_result import XmlSetValueWithXPathResult
from cloudmersive_convert_api_client.models.xxe_threat_detection_result import XxeThreatDetectionResult
from cloudmersive_convert_api_client.models.zip_directory import ZipDirectory
from cloudmersive_convert_api_client.models.zip_encryption_advanced_request import ZipEncryptionAdvancedRequest
from cloudmersive_convert_api_client.models.zip_extract_response import ZipExtractResponse
from cloudmersive_convert_api_client.models.zip_file import ZipFile
