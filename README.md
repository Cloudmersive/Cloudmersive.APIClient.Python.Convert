# cloudmersive_convert_api_client
Convert API lets you effortlessly convert file formats and types.

This Python package provides a native API client for [Cloudmersive Document Conversion](https://www.cloudmersive.com/convert-api)

- API version: v1
- Package version: 2.3.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_convert_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_convert_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_convert_api_client.CompareDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Compare Two Word DOCX
    api_response = api_instance.compare_document_docx(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompareDocumentApi->compare_document_docx: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompareDocumentApi* | [**compare_document_docx**](docs/CompareDocumentApi.md#compare_document_docx) | **POST** /convert/compare/docx | Compare Two Word DOCX
*ConvertDataApi* | [**convert_data_csv_to_json**](docs/ConvertDataApi.md#convert_data_csv_to_json) | **POST** /convert/csv/to/json | Convert CSV to JSON conversion
*ConvertDataApi* | [**convert_data_json_to_xml**](docs/ConvertDataApi.md#convert_data_json_to_xml) | **POST** /convert/json/to/xml | Convert JSON to XML conversion
*ConvertDataApi* | [**convert_data_xls_to_json**](docs/ConvertDataApi.md#convert_data_xls_to_json) | **POST** /convert/xls/to/json | Convert Excel (97-2003) XLS to JSON conversion
*ConvertDataApi* | [**convert_data_xlsx_to_json**](docs/ConvertDataApi.md#convert_data_xlsx_to_json) | **POST** /convert/xlsx/to/json | Convert Excel XLSX to JSON conversion
*ConvertDataApi* | [**convert_data_xml_edit_add_attribute_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_edit_add_attribute_with_x_path) | **POST** /convert/xml/edit/xpath/add-attribute | Adds an attribute to all XML nodes matching XPath expression
*ConvertDataApi* | [**convert_data_xml_edit_add_child_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_edit_add_child_with_x_path) | **POST** /convert/xml/edit/xpath/add-child | Adds an XML node as a child to XML nodes matching XPath expression
*ConvertDataApi* | [**convert_data_xml_edit_remove_all_child_nodes_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_edit_remove_all_child_nodes_with_x_path) | **POST** /convert/xml/edit/xpath/remove-all-children | Removes, deletes all children of nodes matching XPath expression, but does not remove the nodes
*ConvertDataApi* | [**convert_data_xml_edit_replace_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_edit_replace_with_x_path) | **POST** /convert/xml/edit/xpath/replace | Replaces XML nodes matching XPath expression with new node
*ConvertDataApi* | [**convert_data_xml_edit_set_value_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_edit_set_value_with_x_path) | **POST** /convert/xml/edit/xpath/set-value | Sets the value contents of XML nodes matching XPath expression
*ConvertDataApi* | [**convert_data_xml_filter_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_filter_with_x_path) | **POST** /convert/xml/select/xpath | Filter, select XML nodes using XPath expression, get results
*ConvertDataApi* | [**convert_data_xml_query_with_x_query**](docs/ConvertDataApi.md#convert_data_xml_query_with_x_query) | **POST** /convert/xml/query/xquery | Query an XML file using XQuery query, get results
*ConvertDataApi* | [**convert_data_xml_query_with_x_query_multi**](docs/ConvertDataApi.md#convert_data_xml_query_with_x_query_multi) | **POST** /convert/xml/query/xquery/multi | Query multiple XML files using XQuery query, get results
*ConvertDataApi* | [**convert_data_xml_remove_with_x_path**](docs/ConvertDataApi.md#convert_data_xml_remove_with_x_path) | **POST** /convert/xml/edit/xpath/remove | Remove, delete XML nodes and items matching XPath expression
*ConvertDataApi* | [**convert_data_xml_to_json**](docs/ConvertDataApi.md#convert_data_xml_to_json) | **POST** /convert/xml/to/json | Convert XML to JSON conversion
*ConvertDataApi* | [**convert_data_xml_transform_with_xslt_to_xml**](docs/ConvertDataApi.md#convert_data_xml_transform_with_xslt_to_xml) | **POST** /convert/xml/transform/xslt/to/xml | Transform XML document file with XSLT into a new XML document
*ConvertDocumentApi* | [**convert_document_autodetect_get_info**](docs/ConvertDocumentApi.md#convert_document_autodetect_get_info) | **POST** /convert/autodetect/get-info | Get document type information
*ConvertDocumentApi* | [**convert_document_autodetect_to_pdf**](docs/ConvertDocumentApi.md#convert_document_autodetect_to_pdf) | **POST** /convert/autodetect/to/pdf | Convert Document to PDF
*ConvertDocumentApi* | [**convert_document_autodetect_to_png_array**](docs/ConvertDocumentApi.md#convert_document_autodetect_to_png_array) | **POST** /convert/autodetect/to/png | Convert Document to PNG array
*ConvertDocumentApi* | [**convert_document_autodetect_to_txt**](docs/ConvertDocumentApi.md#convert_document_autodetect_to_txt) | **POST** /convert/autodetect/to/txt | Convert Document to Text (txt)
*ConvertDocumentApi* | [**convert_document_csv_to_xlsx**](docs/ConvertDocumentApi.md#convert_document_csv_to_xlsx) | **POST** /convert/csv/to/xlsx | Convert CSV to Excel XLSX Spreadsheet
*ConvertDocumentApi* | [**convert_document_doc_to_docx**](docs/ConvertDocumentApi.md#convert_document_doc_to_docx) | **POST** /convert/doc/to/docx | Convert Word DOC (97-03) Document to DOCX
*ConvertDocumentApi* | [**convert_document_doc_to_pdf**](docs/ConvertDocumentApi.md#convert_document_doc_to_pdf) | **POST** /convert/doc/to/pdf | Convert Word DOC (97-03) Document to PDF
*ConvertDocumentApi* | [**convert_document_docx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_docx_to_pdf) | **POST** /convert/docx/to/pdf | Convert Word DOCX Document to PDF
*ConvertDocumentApi* | [**convert_document_docx_to_txt**](docs/ConvertDocumentApi.md#convert_document_docx_to_txt) | **POST** /convert/docx/to/txt | Convert Word DOCX Document to Text (txt)
*ConvertDocumentApi* | [**convert_document_html_to_pdf**](docs/ConvertDocumentApi.md#convert_document_html_to_pdf) | **POST** /convert/html/to/pdf | Convert HTML document file to PDF Document
*ConvertDocumentApi* | [**convert_document_html_to_png**](docs/ConvertDocumentApi.md#convert_document_html_to_png) | **POST** /convert/html/to/png | Convert HTML document file to PNG image array
*ConvertDocumentApi* | [**convert_document_html_to_txt**](docs/ConvertDocumentApi.md#convert_document_html_to_txt) | **POST** /convert/html/to/txt | HTML Document file to Text (txt)
*ConvertDocumentApi* | [**convert_document_pdf_to_docx**](docs/ConvertDocumentApi.md#convert_document_pdf_to_docx) | **POST** /convert/pdf/to/docx | Convert PDF to Word DOCX Document
*ConvertDocumentApi* | [**convert_document_pdf_to_docx_rasterize**](docs/ConvertDocumentApi.md#convert_document_pdf_to_docx_rasterize) | **POST** /convert/pdf/to/docx/rasterize | Convert PDF to Word DOCX Document based on rasterized version of the PDF
*ConvertDocumentApi* | [**convert_document_pdf_to_png_array**](docs/ConvertDocumentApi.md#convert_document_pdf_to_png_array) | **POST** /convert/pdf/to/png | Convert PDF to PNG Image Array
*ConvertDocumentApi* | [**convert_document_pdf_to_png_single**](docs/ConvertDocumentApi.md#convert_document_pdf_to_png_single) | **POST** /convert/pdf/to/png/merge-single | Convert PDF to Single PNG image
*ConvertDocumentApi* | [**convert_document_pdf_to_pptx**](docs/ConvertDocumentApi.md#convert_document_pdf_to_pptx) | **POST** /convert/pdf/to/pptx | Convert PDF to PowerPoint PPTX Presentation
*ConvertDocumentApi* | [**convert_document_pdf_to_txt**](docs/ConvertDocumentApi.md#convert_document_pdf_to_txt) | **POST** /convert/pdf/to/txt | Convert PDF Document to Text (txt)
*ConvertDocumentApi* | [**convert_document_png_array_to_pdf**](docs/ConvertDocumentApi.md#convert_document_png_array_to_pdf) | **POST** /convert/png/to/pdf | Convert PNG Array to PDF
*ConvertDocumentApi* | [**convert_document_ppt_to_pdf**](docs/ConvertDocumentApi.md#convert_document_ppt_to_pdf) | **POST** /convert/ppt/to/pdf | Convert PowerPoint PPT (97-03) Presentation to PDF
*ConvertDocumentApi* | [**convert_document_ppt_to_pptx**](docs/ConvertDocumentApi.md#convert_document_ppt_to_pptx) | **POST** /convert/ppt/to/pptx | Convert PowerPoint PPT (97-03) Presentation to PPTX
*ConvertDocumentApi* | [**convert_document_pptx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_pptx_to_pdf) | **POST** /convert/pptx/to/pdf | Convert PowerPoint PPTX Presentation to PDF
*ConvertDocumentApi* | [**convert_document_pptx_to_txt**](docs/ConvertDocumentApi.md#convert_document_pptx_to_txt) | **POST** /convert/pptx/to/txt | Convert PowerPoint PPTX Presentation to Text (txt)
*ConvertDocumentApi* | [**convert_document_xls_to_csv**](docs/ConvertDocumentApi.md#convert_document_xls_to_csv) | **POST** /convert/xls/to/csv | Convert Excel XLS (97-03) Spreadsheet to CSV
*ConvertDocumentApi* | [**convert_document_xls_to_pdf**](docs/ConvertDocumentApi.md#convert_document_xls_to_pdf) | **POST** /convert/xls/to/pdf | Convert Excel XLS (97-03) Spreadsheet to PDF
*ConvertDocumentApi* | [**convert_document_xls_to_xlsx**](docs/ConvertDocumentApi.md#convert_document_xls_to_xlsx) | **POST** /convert/xls/to/xlsx | Convert Excel XLS (97-03) Spreadsheet to XLSX
*ConvertDocumentApi* | [**convert_document_xlsx_to_csv**](docs/ConvertDocumentApi.md#convert_document_xlsx_to_csv) | **POST** /convert/xlsx/to/csv | Convert Excel XLSX Spreadsheet to CSV
*ConvertDocumentApi* | [**convert_document_xlsx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_xlsx_to_pdf) | **POST** /convert/xlsx/to/pdf | Convert Excel XLSX Spreadsheet to PDF
*ConvertDocumentApi* | [**convert_document_xlsx_to_txt**](docs/ConvertDocumentApi.md#convert_document_xlsx_to_txt) | **POST** /convert/xlsx/to/txt | Convert Excel XLSX Spreadsheet to Text (txt)
*ConvertImageApi* | [**convert_image_get_image_info**](docs/ConvertImageApi.md#convert_image_get_image_info) | **POST** /convert/image/get-info | Get information about an image
*ConvertImageApi* | [**convert_image_image_format_convert**](docs/ConvertImageApi.md#convert_image_image_format_convert) | **POST** /convert/image/{format1}/to/{format2} | Image format conversion
*ConvertImageApi* | [**convert_image_image_set_dpi**](docs/ConvertImageApi.md#convert_image_image_set_dpi) | **POST** /convert/image/set-dpi/{dpi} | Change image DPI
*ConvertImageApi* | [**convert_image_multipage_image_format_convert**](docs/ConvertImageApi.md#convert_image_multipage_image_format_convert) | **POST** /convert/image-multipage/{format1}/to/{format2} | Multi-page image format conversion
*ConvertTemplateApi* | [**convert_template_apply_docx_template**](docs/ConvertTemplateApi.md#convert_template_apply_docx_template) | **POST** /convert/template/docx/apply | Apply Word DOCX template
*ConvertTemplateApi* | [**convert_template_apply_html_template**](docs/ConvertTemplateApi.md#convert_template_apply_html_template) | **POST** /convert/template/html/apply | Apply HTML template
*ConvertWebApi* | [**convert_web_html_to_docx**](docs/ConvertWebApi.md#convert_web_html_to_docx) | **POST** /convert/html/to/docx | Convert HTML to Word DOCX Document
*ConvertWebApi* | [**convert_web_html_to_pdf**](docs/ConvertWebApi.md#convert_web_html_to_pdf) | **POST** /convert/web/html/to/pdf | Convert HTML string to PDF
*ConvertWebApi* | [**convert_web_html_to_png**](docs/ConvertWebApi.md#convert_web_html_to_png) | **POST** /convert/web/html/to/png | Convert HTML string to PNG screenshot
*ConvertWebApi* | [**convert_web_html_to_txt**](docs/ConvertWebApi.md#convert_web_html_to_txt) | **POST** /convert/web/url/to/txt | Convert website URL page to text (txt)
*ConvertWebApi* | [**convert_web_html_to_txt_0**](docs/ConvertWebApi.md#convert_web_html_to_txt_0) | **POST** /convert/web/html/to/txt | Convert HTML string to text (txt)
*ConvertWebApi* | [**convert_web_md_to_html**](docs/ConvertWebApi.md#convert_web_md_to_html) | **POST** /convert/web/md/to/html | Convert Markdown to HTML
*ConvertWebApi* | [**convert_web_url_to_pdf**](docs/ConvertWebApi.md#convert_web_url_to_pdf) | **POST** /convert/web/url/to/pdf | Convert a URL to PDF
*ConvertWebApi* | [**convert_web_url_to_screenshot**](docs/ConvertWebApi.md#convert_web_url_to_screenshot) | **POST** /convert/web/url/to/screenshot | Take screenshot of URL
*EditDocumentApi* | [**edit_document_begin_editing**](docs/EditDocumentApi.md#edit_document_begin_editing) | **POST** /convert/edit/begin-editing | Begin editing a document
*EditDocumentApi* | [**edit_document_docx_body**](docs/EditDocumentApi.md#edit_document_docx_body) | **POST** /convert/edit/docx/get-body | Get body from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_create_blank_document**](docs/EditDocumentApi.md#edit_document_docx_create_blank_document) | **POST** /convert/edit/docx/create/blank | Create a blank Word DOCX document
*EditDocumentApi* | [**edit_document_docx_delete_pages**](docs/EditDocumentApi.md#edit_document_docx_delete_pages) | **POST** /convert/edit/docx/delete-pages | Delete, remove pages from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_delete_table_row**](docs/EditDocumentApi.md#edit_document_docx_delete_table_row) | **POST** /convert/edit/docx/delete-table-row | Deletes a table row in an existing table in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_headers_and_footers**](docs/EditDocumentApi.md#edit_document_docx_get_headers_and_footers) | **POST** /convert/edit/docx/get-headers-and-footers | Get content of a footer from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_images**](docs/EditDocumentApi.md#edit_document_docx_get_images) | **POST** /convert/edit/docx/get-images | Get images from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_sections**](docs/EditDocumentApi.md#edit_document_docx_get_sections) | **POST** /convert/edit/docx/get-sections | Get sections from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_styles**](docs/EditDocumentApi.md#edit_document_docx_get_styles) | **POST** /convert/edit/docx/get-styles | Get styles from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_table_by_index**](docs/EditDocumentApi.md#edit_document_docx_get_table_by_index) | **POST** /convert/edit/docx/get-table/by-index | Get a specific table by index in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_table_row**](docs/EditDocumentApi.md#edit_document_docx_get_table_row) | **POST** /convert/edit/docx/get-table-row | Gets the contents of an existing table row in an existing table in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_get_tables**](docs/EditDocumentApi.md#edit_document_docx_get_tables) | **POST** /convert/edit/docx/get-tables | Get all tables in Word DOCX document
*EditDocumentApi* | [**edit_document_docx_insert_image**](docs/EditDocumentApi.md#edit_document_docx_insert_image) | **POST** /convert/edit/docx/insert-image | Insert image into a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_insert_paragraph**](docs/EditDocumentApi.md#edit_document_docx_insert_paragraph) | **POST** /convert/edit/docx/insert-paragraph | Insert a new paragraph into a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_insert_table**](docs/EditDocumentApi.md#edit_document_docx_insert_table) | **POST** /convert/edit/docx/insert-table | Insert a new table into a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_insert_table_row**](docs/EditDocumentApi.md#edit_document_docx_insert_table_row) | **POST** /convert/edit/docx/insert-table-row | Insert a new row into an existing table in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_pages**](docs/EditDocumentApi.md#edit_document_docx_pages) | **POST** /convert/edit/docx/get-pages | Get pages and content from a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_remove_headers_and_footers**](docs/EditDocumentApi.md#edit_document_docx_remove_headers_and_footers) | **POST** /convert/edit/docx/remove-headers-and-footers | Remove headers and footers from Word DOCX document
*EditDocumentApi* | [**edit_document_docx_remove_object**](docs/EditDocumentApi.md#edit_document_docx_remove_object) | **POST** /convert/edit/docx/remove-object | Delete any object in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_replace**](docs/EditDocumentApi.md#edit_document_docx_replace) | **POST** /convert/edit/docx/replace-all | Replace string in Word DOCX document
*EditDocumentApi* | [**edit_document_docx_set_footer**](docs/EditDocumentApi.md#edit_document_docx_set_footer) | **POST** /convert/edit/docx/set-footer | Set the footer in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_set_footer_add_page_number**](docs/EditDocumentApi.md#edit_document_docx_set_footer_add_page_number) | **POST** /convert/edit/docx/set-footer/add-page-number | Add page number to footer in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_set_header**](docs/EditDocumentApi.md#edit_document_docx_set_header) | **POST** /convert/edit/docx/set-header | Set the header in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_update_table_cell**](docs/EditDocumentApi.md#edit_document_docx_update_table_cell) | **POST** /convert/edit/docx/update-table-cell | Update, set contents of a table cell in an existing table in a Word DOCX document
*EditDocumentApi* | [**edit_document_docx_update_table_row**](docs/EditDocumentApi.md#edit_document_docx_update_table_row) | **POST** /convert/edit/docx/update-table-row | Update, set contents of a table row in an existing table in a Word DOCX document
*EditDocumentApi* | [**edit_document_finish_editing**](docs/EditDocumentApi.md#edit_document_finish_editing) | **POST** /convert/edit/finish-editing | Download result from document editing
*EditDocumentApi* | [**edit_document_pptx_delete_slides**](docs/EditDocumentApi.md#edit_document_pptx_delete_slides) | **POST** /convert/edit/pptx/delete-slides | Delete, remove slides from a PowerPoint PPTX presentation document
*EditDocumentApi* | [**edit_document_pptx_replace**](docs/EditDocumentApi.md#edit_document_pptx_replace) | **POST** /convert/edit/pptx/replace-all | Replace string in PowerPoint PPTX presentation
*EditDocumentApi* | [**edit_document_xlsx_clear_cell_by_index**](docs/EditDocumentApi.md#edit_document_xlsx_clear_cell_by_index) | **POST** /convert/edit/xlsx/clear-cell/by-index | Clear cell contents in an Excel XLSX spreadsheet, worksheet by index
*EditDocumentApi* | [**edit_document_xlsx_create_blank_spreadsheet**](docs/EditDocumentApi.md#edit_document_xlsx_create_blank_spreadsheet) | **POST** /convert/edit/xlsx/create/blank | Create a blank Excel XLSX spreadsheet
*EditDocumentApi* | [**edit_document_xlsx_create_spreadsheet_from_data**](docs/EditDocumentApi.md#edit_document_xlsx_create_spreadsheet_from_data) | **POST** /convert/edit/xlsx/create/from/data | Create a new Excel XLSX spreadsheet from column and row data
*EditDocumentApi* | [**edit_document_xlsx_delete_worksheet**](docs/EditDocumentApi.md#edit_document_xlsx_delete_worksheet) | **POST** /convert/edit/xlsx/delete-worksheet | Delete, remove worksheet from an Excel XLSX spreadsheet document
*EditDocumentApi* | [**edit_document_xlsx_get_cell_by_index**](docs/EditDocumentApi.md#edit_document_xlsx_get_cell_by_index) | **POST** /convert/edit/xlsx/get-cell/by-index | Get cell from an Excel XLSX spreadsheet, worksheet by index
*EditDocumentApi* | [**edit_document_xlsx_get_columns**](docs/EditDocumentApi.md#edit_document_xlsx_get_columns) | **POST** /convert/edit/xlsx/get-columns | Get rows and cells from a Excel XLSX spreadsheet, worksheet
*EditDocumentApi* | [**edit_document_xlsx_get_images**](docs/EditDocumentApi.md#edit_document_xlsx_get_images) | **POST** /convert/edit/xlsx/get-images | Get images from a Excel XLSX spreadsheet, worksheet
*EditDocumentApi* | [**edit_document_xlsx_get_rows_and_cells**](docs/EditDocumentApi.md#edit_document_xlsx_get_rows_and_cells) | **POST** /convert/edit/xlsx/get-rows-and-cells | Get rows and cells from a Excel XLSX spreadsheet, worksheet
*EditDocumentApi* | [**edit_document_xlsx_get_styles**](docs/EditDocumentApi.md#edit_document_xlsx_get_styles) | **POST** /convert/edit/xlsx/get-styles | Get styles from a Excel XLSX spreadsheet, worksheet
*EditDocumentApi* | [**edit_document_xlsx_get_worksheets**](docs/EditDocumentApi.md#edit_document_xlsx_get_worksheets) | **POST** /convert/edit/xlsx/get-worksheets | Get worksheets from a Excel XLSX spreadsheet
*EditDocumentApi* | [**edit_document_xlsx_insert_worksheet**](docs/EditDocumentApi.md#edit_document_xlsx_insert_worksheet) | **POST** /convert/edit/xlsx/insert-worksheet | Insert a new worksheet into an Excel XLSX spreadsheet
*EditDocumentApi* | [**edit_document_xlsx_set_cell_by_index**](docs/EditDocumentApi.md#edit_document_xlsx_set_cell_by_index) | **POST** /convert/edit/xlsx/set-cell/by-index | Set, update cell contents in an Excel XLSX spreadsheet, worksheet by index
*EditPdfApi* | [**edit_pdf_add_annotations**](docs/EditPdfApi.md#edit_pdf_add_annotations) | **POST** /convert/edit/pdf/annotations/add-item | Add one or more PDF annotations, comments in the PDF document
*EditPdfApi* | [**edit_pdf_decrypt**](docs/EditPdfApi.md#edit_pdf_decrypt) | **POST** /convert/edit/pdf/decrypt | Decrypt and password-protect a PDF
*EditPdfApi* | [**edit_pdf_delete_pages**](docs/EditPdfApi.md#edit_pdf_delete_pages) | **POST** /convert/edit/pdf/pages/delete | Remove / delete pages from a PDF document
*EditPdfApi* | [**edit_pdf_encrypt**](docs/EditPdfApi.md#edit_pdf_encrypt) | **POST** /convert/edit/pdf/encrypt | Encrypt and password-protect a PDF
*EditPdfApi* | [**edit_pdf_get_annotations**](docs/EditPdfApi.md#edit_pdf_get_annotations) | **POST** /convert/edit/pdf/annotations/list | Get PDF annotations, including comments in the document
*EditPdfApi* | [**edit_pdf_get_form_fields**](docs/EditPdfApi.md#edit_pdf_get_form_fields) | **POST** /convert/edit/pdf/form/get-fields | Gets PDF Form fields and values
*EditPdfApi* | [**edit_pdf_get_metadata**](docs/EditPdfApi.md#edit_pdf_get_metadata) | **POST** /convert/edit/pdf/get-metadata | Get PDF document metadata
*EditPdfApi* | [**edit_pdf_get_pdf_text_by_pages**](docs/EditPdfApi.md#edit_pdf_get_pdf_text_by_pages) | **POST** /convert/edit/pdf/pages/get-text | Get text in a PDF document by page
*EditPdfApi* | [**edit_pdf_insert_pages**](docs/EditPdfApi.md#edit_pdf_insert_pages) | **POST** /convert/edit/pdf/pages/insert | Insert / copy pages from one PDF document into another
*EditPdfApi* | [**edit_pdf_rasterize**](docs/EditPdfApi.md#edit_pdf_rasterize) | **POST** /convert/edit/pdf/rasterize | Rasterize a PDF to an image-based PDF
*EditPdfApi* | [**edit_pdf_remove_all_annotations**](docs/EditPdfApi.md#edit_pdf_remove_all_annotations) | **POST** /convert/edit/pdf/annotations/remove-all | Remove all PDF annotations, including comments in the document
*EditPdfApi* | [**edit_pdf_remove_annotation_item**](docs/EditPdfApi.md#edit_pdf_remove_annotation_item) | **POST** /convert/edit/pdf/annotations/remove-item | Remove a specific PDF annotation, comment in the document
*EditPdfApi* | [**edit_pdf_rotate_all_pages**](docs/EditPdfApi.md#edit_pdf_rotate_all_pages) | **POST** /convert/edit/pdf/pages/rotate/all | Rotate all pages in a PDF document
*EditPdfApi* | [**edit_pdf_rotate_page_range**](docs/EditPdfApi.md#edit_pdf_rotate_page_range) | **POST** /convert/edit/pdf/pages/rotate/page-range | Rotate a range, subset of pages in a PDF document
*EditPdfApi* | [**edit_pdf_set_form_fields**](docs/EditPdfApi.md#edit_pdf_set_form_fields) | **POST** /convert/edit/pdf/form/set-fields | Sets ands fills PDF Form field values
*EditPdfApi* | [**edit_pdf_set_metadata**](docs/EditPdfApi.md#edit_pdf_set_metadata) | **POST** /convert/edit/pdf/set-metadata | Sets PDF document metadata
*EditPdfApi* | [**edit_pdf_set_permissions**](docs/EditPdfApi.md#edit_pdf_set_permissions) | **POST** /convert/edit/pdf/encrypt/set-permissions | Encrypt, password-protect and set restricted permissions on a PDF
*EditPdfApi* | [**edit_pdf_watermark_text**](docs/EditPdfApi.md#edit_pdf_watermark_text) | **POST** /convert/edit/pdf/watermark/text | Add a text watermark to a PDF
*MergeDocumentApi* | [**merge_document_docx**](docs/MergeDocumentApi.md#merge_document_docx) | **POST** /convert/merge/docx | Merge Two Word DOCX Together
*MergeDocumentApi* | [**merge_document_docx_multi**](docs/MergeDocumentApi.md#merge_document_docx_multi) | **POST** /convert/merge/docx/multi | Merge Multple Word DOCX Together
*MergeDocumentApi* | [**merge_document_pdf**](docs/MergeDocumentApi.md#merge_document_pdf) | **POST** /convert/merge/pdf | Merge Two PDF Files Together
*MergeDocumentApi* | [**merge_document_pdf_multi**](docs/MergeDocumentApi.md#merge_document_pdf_multi) | **POST** /convert/merge/pdf/multi | Merge Multple PDF Files Together
*MergeDocumentApi* | [**merge_document_png**](docs/MergeDocumentApi.md#merge_document_png) | **POST** /convert/merge/png/vertical | Merge Multple PNG Files Together
*MergeDocumentApi* | [**merge_document_pptx**](docs/MergeDocumentApi.md#merge_document_pptx) | **POST** /convert/merge/pptx | Merge Two PowerPoint PPTX Together
*MergeDocumentApi* | [**merge_document_pptx_multi**](docs/MergeDocumentApi.md#merge_document_pptx_multi) | **POST** /convert/merge/pptx/multi | Merge Multple PowerPoint PPTX Together
*MergeDocumentApi* | [**merge_document_xlsx**](docs/MergeDocumentApi.md#merge_document_xlsx) | **POST** /convert/merge/xlsx | Merge Two Excel XLSX Together
*MergeDocumentApi* | [**merge_document_xlsx_multi**](docs/MergeDocumentApi.md#merge_document_xlsx_multi) | **POST** /convert/merge/xlsx/multi | Merge Multple Excel XLSX Together
*SplitDocumentApi* | [**split_document_docx**](docs/SplitDocumentApi.md#split_document_docx) | **POST** /convert/split/docx | Split a single Word Document DOCX into Separate Documents by Page
*SplitDocumentApi* | [**split_document_pdf_by_page**](docs/SplitDocumentApi.md#split_document_pdf_by_page) | **POST** /convert/split/pdf | Split a PDF file into separate PDF files, one per page
*SplitDocumentApi* | [**split_document_pptx**](docs/SplitDocumentApi.md#split_document_pptx) | **POST** /convert/split/pptx | Split a single PowerPoint Presentation PPTX into Separate Slides
*SplitDocumentApi* | [**split_document_xlsx**](docs/SplitDocumentApi.md#split_document_xlsx) | **POST** /convert/split/xlsx | Split a single Excel XLSX into Separate Worksheets
*ValidateDocumentApi* | [**validate_document_autodetect_validation**](docs/ValidateDocumentApi.md#validate_document_autodetect_validation) | **POST** /convert/validate/autodetect | Autodetect content type and validate
*ValidateDocumentApi* | [**validate_document_docx_validation**](docs/ValidateDocumentApi.md#validate_document_docx_validation) | **POST** /convert/validate/docx | Validate a Word document (DOCX)
*ValidateDocumentApi* | [**validate_document_executable_validation**](docs/ValidateDocumentApi.md#validate_document_executable_validation) | **POST** /convert/validate/executable | Validate if a file is executable
*ValidateDocumentApi* | [**validate_document_json_validation**](docs/ValidateDocumentApi.md#validate_document_json_validation) | **POST** /convert/validate/json | Validate a JSON file
*ValidateDocumentApi* | [**validate_document_pdf_validation**](docs/ValidateDocumentApi.md#validate_document_pdf_validation) | **POST** /convert/validate/pdf | Validate a PDF document file
*ValidateDocumentApi* | [**validate_document_pptx_validation**](docs/ValidateDocumentApi.md#validate_document_pptx_validation) | **POST** /convert/validate/pptx | Validate a PowerPoint presentation (PPTX)
*ValidateDocumentApi* | [**validate_document_xlsx_validation**](docs/ValidateDocumentApi.md#validate_document_xlsx_validation) | **POST** /convert/validate/xlsx | Validate a Excel document (XLSX)
*ValidateDocumentApi* | [**validate_document_xml_validation**](docs/ValidateDocumentApi.md#validate_document_xml_validation) | **POST** /convert/validate/xml | Validate an XML file
*ViewerToolsApi* | [**viewer_tools_create_simple**](docs/ViewerToolsApi.md#viewer_tools_create_simple) | **POST** /convert/viewer/create/web/simple | Create a web-based viewer


## Documentation For Models

 - [AddPdfAnnotationRequest](docs/AddPdfAnnotationRequest.md)
 - [AlternateFileFormatCandidate](docs/AlternateFileFormatCandidate.md)
 - [AutodetectDocumentValidationResult](docs/AutodetectDocumentValidationResult.md)
 - [AutodetectGetInfoResult](docs/AutodetectGetInfoResult.md)
 - [AutodetectToPngResult](docs/AutodetectToPngResult.md)
 - [ClearXlsxCellRequest](docs/ClearXlsxCellRequest.md)
 - [ClearXlsxCellResponse](docs/ClearXlsxCellResponse.md)
 - [ConvertedPngPage](docs/ConvertedPngPage.md)
 - [CreateBlankDocxRequest](docs/CreateBlankDocxRequest.md)
 - [CreateBlankDocxResponse](docs/CreateBlankDocxResponse.md)
 - [CreateBlankSpreadsheetRequest](docs/CreateBlankSpreadsheetRequest.md)
 - [CreateBlankSpreadsheetResponse](docs/CreateBlankSpreadsheetResponse.md)
 - [CreateSpreadsheetFromDataRequest](docs/CreateSpreadsheetFromDataRequest.md)
 - [CreateSpreadsheetFromDataResponse](docs/CreateSpreadsheetFromDataResponse.md)
 - [DeleteDocxTableRowRequest](docs/DeleteDocxTableRowRequest.md)
 - [DeleteDocxTableRowResponse](docs/DeleteDocxTableRowResponse.md)
 - [DocumentValidationError](docs/DocumentValidationError.md)
 - [DocumentValidationResult](docs/DocumentValidationResult.md)
 - [DocxBody](docs/DocxBody.md)
 - [DocxCellStyle](docs/DocxCellStyle.md)
 - [DocxFooter](docs/DocxFooter.md)
 - [DocxHeader](docs/DocxHeader.md)
 - [DocxImage](docs/DocxImage.md)
 - [DocxInsertImageRequest](docs/DocxInsertImageRequest.md)
 - [DocxInsertImageResponse](docs/DocxInsertImageResponse.md)
 - [DocxPage](docs/DocxPage.md)
 - [DocxParagraph](docs/DocxParagraph.md)
 - [DocxRemoveObjectRequest](docs/DocxRemoveObjectRequest.md)
 - [DocxRemoveObjectResponse](docs/DocxRemoveObjectResponse.md)
 - [DocxRun](docs/DocxRun.md)
 - [DocxSection](docs/DocxSection.md)
 - [DocxSetFooterAddPageNumberRequest](docs/DocxSetFooterAddPageNumberRequest.md)
 - [DocxSetFooterRequest](docs/DocxSetFooterRequest.md)
 - [DocxSetFooterResponse](docs/DocxSetFooterResponse.md)
 - [DocxSetHeaderRequest](docs/DocxSetHeaderRequest.md)
 - [DocxSetHeaderResponse](docs/DocxSetHeaderResponse.md)
 - [DocxStyle](docs/DocxStyle.md)
 - [DocxTable](docs/DocxTable.md)
 - [DocxTableCell](docs/DocxTableCell.md)
 - [DocxTableRow](docs/DocxTableRow.md)
 - [DocxTemplateApplicationRequest](docs/DocxTemplateApplicationRequest.md)
 - [DocxTemplateOperation](docs/DocxTemplateOperation.md)
 - [DocxText](docs/DocxText.md)
 - [ExifValue](docs/ExifValue.md)
 - [FinishEditingRequest](docs/FinishEditingRequest.md)
 - [GetDocxBodyRequest](docs/GetDocxBodyRequest.md)
 - [GetDocxBodyResponse](docs/GetDocxBodyResponse.md)
 - [GetDocxHeadersAndFootersRequest](docs/GetDocxHeadersAndFootersRequest.md)
 - [GetDocxHeadersAndFootersResponse](docs/GetDocxHeadersAndFootersResponse.md)
 - [GetDocxImagesRequest](docs/GetDocxImagesRequest.md)
 - [GetDocxImagesResponse](docs/GetDocxImagesResponse.md)
 - [GetDocxPagesRequest](docs/GetDocxPagesRequest.md)
 - [GetDocxPagesResponse](docs/GetDocxPagesResponse.md)
 - [GetDocxSectionsRequest](docs/GetDocxSectionsRequest.md)
 - [GetDocxSectionsResponse](docs/GetDocxSectionsResponse.md)
 - [GetDocxStylesRequest](docs/GetDocxStylesRequest.md)
 - [GetDocxStylesResponse](docs/GetDocxStylesResponse.md)
 - [GetDocxTableByIndexRequest](docs/GetDocxTableByIndexRequest.md)
 - [GetDocxTableByIndexResponse](docs/GetDocxTableByIndexResponse.md)
 - [GetDocxTableRowRequest](docs/GetDocxTableRowRequest.md)
 - [GetDocxTableRowResponse](docs/GetDocxTableRowResponse.md)
 - [GetDocxTablesRequest](docs/GetDocxTablesRequest.md)
 - [GetDocxTablesResponse](docs/GetDocxTablesResponse.md)
 - [GetImageInfoResult](docs/GetImageInfoResult.md)
 - [GetPdfAnnotationsResult](docs/GetPdfAnnotationsResult.md)
 - [GetXlsxCellRequest](docs/GetXlsxCellRequest.md)
 - [GetXlsxCellResponse](docs/GetXlsxCellResponse.md)
 - [GetXlsxColumnsRequest](docs/GetXlsxColumnsRequest.md)
 - [GetXlsxColumnsResponse](docs/GetXlsxColumnsResponse.md)
 - [GetXlsxImagesRequest](docs/GetXlsxImagesRequest.md)
 - [GetXlsxImagesResponse](docs/GetXlsxImagesResponse.md)
 - [GetXlsxRowsAndCellsRequest](docs/GetXlsxRowsAndCellsRequest.md)
 - [GetXlsxRowsAndCellsResponse](docs/GetXlsxRowsAndCellsResponse.md)
 - [GetXlsxStylesRequest](docs/GetXlsxStylesRequest.md)
 - [GetXlsxStylesResponse](docs/GetXlsxStylesResponse.md)
 - [GetXlsxWorksheetsRequest](docs/GetXlsxWorksheetsRequest.md)
 - [GetXlsxWorksheetsResponse](docs/GetXlsxWorksheetsResponse.md)
 - [HtmlMdResult](docs/HtmlMdResult.md)
 - [HtmlTemplateApplicationRequest](docs/HtmlTemplateApplicationRequest.md)
 - [HtmlTemplateApplicationResponse](docs/HtmlTemplateApplicationResponse.md)
 - [HtmlTemplateOperation](docs/HtmlTemplateOperation.md)
 - [HtmlToOfficeRequest](docs/HtmlToOfficeRequest.md)
 - [HtmlToPdfRequest](docs/HtmlToPdfRequest.md)
 - [HtmlToPngRequest](docs/HtmlToPngRequest.md)
 - [HtmlToTextRequest](docs/HtmlToTextRequest.md)
 - [HtmlToTextResponse](docs/HtmlToTextResponse.md)
 - [InsertDocxInsertParagraphRequest](docs/InsertDocxInsertParagraphRequest.md)
 - [InsertDocxInsertParagraphResponse](docs/InsertDocxInsertParagraphResponse.md)
 - [InsertDocxTableRowRequest](docs/InsertDocxTableRowRequest.md)
 - [InsertDocxTableRowResponse](docs/InsertDocxTableRowResponse.md)
 - [InsertDocxTablesRequest](docs/InsertDocxTablesRequest.md)
 - [InsertDocxTablesResponse](docs/InsertDocxTablesResponse.md)
 - [InsertXlsxWorksheetRequest](docs/InsertXlsxWorksheetRequest.md)
 - [InsertXlsxWorksheetResponse](docs/InsertXlsxWorksheetResponse.md)
 - [MultipageImageFormatConversionResult](docs/MultipageImageFormatConversionResult.md)
 - [PageConversionResult](docs/PageConversionResult.md)
 - [PdfAnnotation](docs/PdfAnnotation.md)
 - [PdfDocument](docs/PdfDocument.md)
 - [PdfFormField](docs/PdfFormField.md)
 - [PdfFormFields](docs/PdfFormFields.md)
 - [PdfMetadata](docs/PdfMetadata.md)
 - [PdfPageText](docs/PdfPageText.md)
 - [PdfTextByPageResult](docs/PdfTextByPageResult.md)
 - [PdfToPngResult](docs/PdfToPngResult.md)
 - [PresentationResult](docs/PresentationResult.md)
 - [RemoveDocxHeadersAndFootersRequest](docs/RemoveDocxHeadersAndFootersRequest.md)
 - [RemoveDocxHeadersAndFootersResponse](docs/RemoveDocxHeadersAndFootersResponse.md)
 - [RemoveDocxPagesRequest](docs/RemoveDocxPagesRequest.md)
 - [RemovePptxSlidesRequest](docs/RemovePptxSlidesRequest.md)
 - [RemoveXlsxWorksheetRequest](docs/RemoveXlsxWorksheetRequest.md)
 - [ReplaceStringRequest](docs/ReplaceStringRequest.md)
 - [ScreenshotRequest](docs/ScreenshotRequest.md)
 - [SetFormFieldValue](docs/SetFormFieldValue.md)
 - [SetPdfFormFieldsRequest](docs/SetPdfFormFieldsRequest.md)
 - [SetPdfMetadataRequest](docs/SetPdfMetadataRequest.md)
 - [SetXlsxCellRequest](docs/SetXlsxCellRequest.md)
 - [SetXlsxCellResponse](docs/SetXlsxCellResponse.md)
 - [SplitDocumentResult](docs/SplitDocumentResult.md)
 - [SplitDocxDocumentResult](docs/SplitDocxDocumentResult.md)
 - [SplitPdfResult](docs/SplitPdfResult.md)
 - [SplitPptxPresentationResult](docs/SplitPptxPresentationResult.md)
 - [SplitXlsxWorksheetResult](docs/SplitXlsxWorksheetResult.md)
 - [TextConversionResult](docs/TextConversionResult.md)
 - [UpdateDocxTableCellRequest](docs/UpdateDocxTableCellRequest.md)
 - [UpdateDocxTableCellResponse](docs/UpdateDocxTableCellResponse.md)
 - [UpdateDocxTableRowRequest](docs/UpdateDocxTableRowRequest.md)
 - [UpdateDocxTableRowResponse](docs/UpdateDocxTableRowResponse.md)
 - [UrlToTextRequest](docs/UrlToTextRequest.md)
 - [UrlToTextResponse](docs/UrlToTextResponse.md)
 - [ViewerResponse](docs/ViewerResponse.md)
 - [WorksheetResult](docs/WorksheetResult.md)
 - [XlsxImage](docs/XlsxImage.md)
 - [XlsxSpreadsheetCell](docs/XlsxSpreadsheetCell.md)
 - [XlsxSpreadsheetColumn](docs/XlsxSpreadsheetColumn.md)
 - [XlsxSpreadsheetRow](docs/XlsxSpreadsheetRow.md)
 - [XlsxWorksheet](docs/XlsxWorksheet.md)
 - [XmlAddAttributeWithXPathResult](docs/XmlAddAttributeWithXPathResult.md)
 - [XmlAddChildWithXPathResult](docs/XmlAddChildWithXPathResult.md)
 - [XmlFilterWithXPathResult](docs/XmlFilterWithXPathResult.md)
 - [XmlQueryWithXQueryMultiResult](docs/XmlQueryWithXQueryMultiResult.md)
 - [XmlQueryWithXQueryResult](docs/XmlQueryWithXQueryResult.md)
 - [XmlRemoveAllChildrenWithXPathResult](docs/XmlRemoveAllChildrenWithXPathResult.md)
 - [XmlRemoveWithXPathResult](docs/XmlRemoveWithXPathResult.md)
 - [XmlReplaceWithXPathResult](docs/XmlReplaceWithXPathResult.md)
 - [XmlSetValueWithXPathResult](docs/XmlSetValueWithXPathResult.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



