# cloudmersive_convert_api_client.EditDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_document_begin_editing**](EditDocumentApi.md#edit_document_begin_editing) | **POST** /convert/edit/begin-editing | Begin editing a document
[**edit_document_docx_accept_all_track_changes**](EditDocumentApi.md#edit_document_docx_accept_all_track_changes) | **POST** /convert/edit/docx/track-changes/accept-all | Accept all tracked changes, revisions in a Word DOCX document
[**edit_document_docx_body**](EditDocumentApi.md#edit_document_docx_body) | **POST** /convert/edit/docx/get-body | Get body from a Word DOCX document
[**edit_document_docx_create_blank_document**](EditDocumentApi.md#edit_document_docx_create_blank_document) | **POST** /convert/edit/docx/create/blank | Create a blank Word DOCX document
[**edit_document_docx_delete_pages**](EditDocumentApi.md#edit_document_docx_delete_pages) | **POST** /convert/edit/docx/delete-pages | Delete, remove pages from a Word DOCX document
[**edit_document_docx_delete_table_row**](EditDocumentApi.md#edit_document_docx_delete_table_row) | **POST** /convert/edit/docx/delete-table-row | Deletes a table row in an existing table in a Word DOCX document
[**edit_document_docx_delete_table_row_range**](EditDocumentApi.md#edit_document_docx_delete_table_row_range) | **POST** /convert/edit/docx/delete-table-row/range | Deletes a range of multiple table rows in an existing table in a Word DOCX document
[**edit_document_docx_disable_track_changes**](EditDocumentApi.md#edit_document_docx_disable_track_changes) | **POST** /convert/edit/docx/track-changes/disable | Disable track changes, revisions in a Word DOCX document
[**edit_document_docx_enable_track_changes**](EditDocumentApi.md#edit_document_docx_enable_track_changes) | **POST** /convert/edit/docx/track-changes/enable | Enable track changes, revisions in a Word DOCX document
[**edit_document_docx_find_paragraph**](EditDocumentApi.md#edit_document_docx_find_paragraph) | **POST** /convert/edit/docx/find/paragraph | Find matching paragraphs in a Word DOCX document
[**edit_document_docx_get_comments**](EditDocumentApi.md#edit_document_docx_get_comments) | **POST** /convert/edit/docx/get-comments/flat-list | Get comments from a Word DOCX document as a flat list
[**edit_document_docx_get_comments_hierarchical**](EditDocumentApi.md#edit_document_docx_get_comments_hierarchical) | **POST** /convert/edit/docx/get-comments/hierarchical | Get comments from a Word DOCX document hierarchically
[**edit_document_docx_get_headers_and_footers**](EditDocumentApi.md#edit_document_docx_get_headers_and_footers) | **POST** /convert/edit/docx/get-headers-and-footers | Get content of a footer from a Word DOCX document
[**edit_document_docx_get_images**](EditDocumentApi.md#edit_document_docx_get_images) | **POST** /convert/edit/docx/get-images | Get images from a Word DOCX document
[**edit_document_docx_get_macro_information**](EditDocumentApi.md#edit_document_docx_get_macro_information) | **POST** /convert/edit/docx/get-macros | Get macro information from a Word DOCX/DOCM document
[**edit_document_docx_get_metadata_properties**](EditDocumentApi.md#edit_document_docx_get_metadata_properties) | **POST** /convert/edit/docx/get-metadata | Get all metadata properties in Word DOCX document
[**edit_document_docx_get_sections**](EditDocumentApi.md#edit_document_docx_get_sections) | **POST** /convert/edit/docx/get-sections | Get sections from a Word DOCX document
[**edit_document_docx_get_styles**](EditDocumentApi.md#edit_document_docx_get_styles) | **POST** /convert/edit/docx/get-styles | Get styles from a Word DOCX document
[**edit_document_docx_get_table_by_index**](EditDocumentApi.md#edit_document_docx_get_table_by_index) | **POST** /convert/edit/docx/get-table/by-index | Get a specific table by index in a Word DOCX document
[**edit_document_docx_get_table_row**](EditDocumentApi.md#edit_document_docx_get_table_row) | **POST** /convert/edit/docx/get-table-row | Gets the contents of an existing table row in an existing table in a Word DOCX document
[**edit_document_docx_get_tables**](EditDocumentApi.md#edit_document_docx_get_tables) | **POST** /convert/edit/docx/get-tables | Get all tables in Word DOCX document
[**edit_document_docx_insert_comment_on_paragraph**](EditDocumentApi.md#edit_document_docx_insert_comment_on_paragraph) | **POST** /convert/edit/docx/insert-comment/on/paragraph | Insert a new comment into a Word DOCX document attached to a paragraph
[**edit_document_docx_insert_image**](EditDocumentApi.md#edit_document_docx_insert_image) | **POST** /convert/edit/docx/insert-image | Insert image into a Word DOCX document
[**edit_document_docx_insert_paragraph**](EditDocumentApi.md#edit_document_docx_insert_paragraph) | **POST** /convert/edit/docx/insert-paragraph | Insert a new paragraph into a Word DOCX document
[**edit_document_docx_insert_table**](EditDocumentApi.md#edit_document_docx_insert_table) | **POST** /convert/edit/docx/insert-table | Insert a new table into a Word DOCX document
[**edit_document_docx_insert_table_row**](EditDocumentApi.md#edit_document_docx_insert_table_row) | **POST** /convert/edit/docx/insert-table-row | Insert a new row into an existing table in a Word DOCX document
[**edit_document_docx_pages**](EditDocumentApi.md#edit_document_docx_pages) | **POST** /convert/edit/docx/get-pages | Get pages and content from a Word DOCX document
[**edit_document_docx_remove_all_comments**](EditDocumentApi.md#edit_document_docx_remove_all_comments) | **POST** /convert/edit/docx/comments/remove-all | Remove all comments from a Word DOCX document
[**edit_document_docx_remove_headers_and_footers**](EditDocumentApi.md#edit_document_docx_remove_headers_and_footers) | **POST** /convert/edit/docx/remove-headers-and-footers | Remove headers and footers from Word DOCX document
[**edit_document_docx_remove_object**](EditDocumentApi.md#edit_document_docx_remove_object) | **POST** /convert/edit/docx/remove-object | Delete any object in a Word DOCX document
[**edit_document_docx_replace**](EditDocumentApi.md#edit_document_docx_replace) | **POST** /convert/edit/docx/replace-all | Replace string in Word DOCX document
[**edit_document_docx_replace_multi**](EditDocumentApi.md#edit_document_docx_replace_multi) | **POST** /convert/edit/docx/replace-all/multi | Replace multiple strings in Word DOCX document
[**edit_document_docx_replace_paragraph**](EditDocumentApi.md#edit_document_docx_replace_paragraph) | **POST** /convert/edit/docx/replace/paragraph | Replace matching paragraphs in a Word DOCX document
[**edit_document_docx_set_custom_metadata_properties**](EditDocumentApi.md#edit_document_docx_set_custom_metadata_properties) | **POST** /convert/edit/docx/set-metadata/custom-property | Set custom property metadata properties in Word DOCX document
[**edit_document_docx_set_footer**](EditDocumentApi.md#edit_document_docx_set_footer) | **POST** /convert/edit/docx/set-footer | Set the footer in a Word DOCX document
[**edit_document_docx_set_footer_add_page_number**](EditDocumentApi.md#edit_document_docx_set_footer_add_page_number) | **POST** /convert/edit/docx/set-footer/add-page-number | Add page number to footer in a Word DOCX document
[**edit_document_docx_set_header**](EditDocumentApi.md#edit_document_docx_set_header) | **POST** /convert/edit/docx/set-header | Set the header in a Word DOCX document
[**edit_document_docx_update_table_cell**](EditDocumentApi.md#edit_document_docx_update_table_cell) | **POST** /convert/edit/docx/update-table-cell | Update, set contents of a table cell in an existing table in a Word DOCX document
[**edit_document_docx_update_table_row**](EditDocumentApi.md#edit_document_docx_update_table_row) | **POST** /convert/edit/docx/update-table-row | Update, set contents of a table row in an existing table in a Word DOCX document
[**edit_document_finish_editing**](EditDocumentApi.md#edit_document_finish_editing) | **POST** /convert/edit/finish-editing | Finish editing document, and download result from document editing
[**edit_document_pptx_delete_slides**](EditDocumentApi.md#edit_document_pptx_delete_slides) | **POST** /convert/edit/pptx/delete-slides | Delete, remove slides from a PowerPoint PPTX presentation document
[**edit_document_pptx_get_macro_information**](EditDocumentApi.md#edit_document_pptx_get_macro_information) | **POST** /convert/edit/pptx/get-macros | Get macro information from a PowerPoint PPTX/PPTM presentation document
[**edit_document_pptx_replace**](EditDocumentApi.md#edit_document_pptx_replace) | **POST** /convert/edit/pptx/replace-all | Replace string in PowerPoint PPTX presentation
[**edit_document_xlsx_append_row**](EditDocumentApi.md#edit_document_xlsx_append_row) | **POST** /convert/edit/xlsx/append-row | Append row to a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_clear_cell_by_index**](EditDocumentApi.md#edit_document_xlsx_clear_cell_by_index) | **POST** /convert/edit/xlsx/clear-cell/by-index | Clear cell contents in an Excel XLSX spreadsheet, worksheet by index
[**edit_document_xlsx_clear_row**](EditDocumentApi.md#edit_document_xlsx_clear_row) | **POST** /convert/edit/xlsx/clear-row | Clear row from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_create_blank_spreadsheet**](EditDocumentApi.md#edit_document_xlsx_create_blank_spreadsheet) | **POST** /convert/edit/xlsx/create/blank | Create a blank Excel XLSX spreadsheet
[**edit_document_xlsx_create_spreadsheet_from_data**](EditDocumentApi.md#edit_document_xlsx_create_spreadsheet_from_data) | **POST** /convert/edit/xlsx/create/from/data | Create a new Excel XLSX spreadsheet from column and row data
[**edit_document_xlsx_delete_worksheet**](EditDocumentApi.md#edit_document_xlsx_delete_worksheet) | **POST** /convert/edit/xlsx/delete-worksheet | Delete, remove worksheet from an Excel XLSX spreadsheet document
[**edit_document_xlsx_disable_shared_workbook**](EditDocumentApi.md#edit_document_xlsx_disable_shared_workbook) | **POST** /convert/edit/xlsx/configuration/disable-shared-workbook | Disable Shared Workbook (legacy) in Excel XLSX spreadsheet
[**edit_document_xlsx_enable_shared_workbook**](EditDocumentApi.md#edit_document_xlsx_enable_shared_workbook) | **POST** /convert/edit/xlsx/configuration/enable-shared-workbook | Enable Shared Workbook (legacy) in Excel XLSX spreadsheet
[**edit_document_xlsx_get_cell_by_identifier**](EditDocumentApi.md#edit_document_xlsx_get_cell_by_identifier) | **POST** /convert/edit/xlsx/get-cell/by-identifier | Get cell from an Excel XLSX spreadsheet, worksheet by cell identifier
[**edit_document_xlsx_get_cell_by_index**](EditDocumentApi.md#edit_document_xlsx_get_cell_by_index) | **POST** /convert/edit/xlsx/get-cell/by-index | Get cell from an Excel XLSX spreadsheet, worksheet by index
[**edit_document_xlsx_get_columns**](EditDocumentApi.md#edit_document_xlsx_get_columns) | **POST** /convert/edit/xlsx/get-columns | Get columns from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_images**](EditDocumentApi.md#edit_document_xlsx_get_images) | **POST** /convert/edit/xlsx/get-images | Get images from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_macro_information**](EditDocumentApi.md#edit_document_xlsx_get_macro_information) | **POST** /convert/edit/xlsx/get-macros | Get macro information from a Excel XLSX/XLSM spreadsheet, worksheet
[**edit_document_xlsx_get_rows_and_cells**](EditDocumentApi.md#edit_document_xlsx_get_rows_and_cells) | **POST** /convert/edit/xlsx/get-rows-and-cells | Get rows and cells from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_specific_row**](EditDocumentApi.md#edit_document_xlsx_get_specific_row) | **POST** /convert/edit/xlsx/get-specific-row | Get a specific row from a Excel XLSX spreadsheet, worksheet by path
[**edit_document_xlsx_get_styles**](EditDocumentApi.md#edit_document_xlsx_get_styles) | **POST** /convert/edit/xlsx/get-styles | Get styles from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_worksheets**](EditDocumentApi.md#edit_document_xlsx_get_worksheets) | **POST** /convert/edit/xlsx/get-worksheets | Get worksheets from a Excel XLSX spreadsheet
[**edit_document_xlsx_insert_worksheet**](EditDocumentApi.md#edit_document_xlsx_insert_worksheet) | **POST** /convert/edit/xlsx/insert-worksheet | Insert a new worksheet into an Excel XLSX spreadsheet
[**edit_document_xlsx_rename_worksheet**](EditDocumentApi.md#edit_document_xlsx_rename_worksheet) | **POST** /convert/edit/xlsx/rename-worksheet | Rename a specific worksheet in a Excel XLSX spreadsheet
[**edit_document_xlsx_set_cell_by_identifier**](EditDocumentApi.md#edit_document_xlsx_set_cell_by_identifier) | **POST** /convert/edit/xlsx/set-cell/by-identifier | Set, update cell contents in an Excel XLSX spreadsheet, worksheet by cell identifier
[**edit_document_xlsx_set_cell_by_index**](EditDocumentApi.md#edit_document_xlsx_set_cell_by_index) | **POST** /convert/edit/xlsx/set-cell/by-index | Set, update cell contents in an Excel XLSX spreadsheet, worksheet by index


# **edit_document_begin_editing**
> str edit_document_begin_editing(input_file)

Begin editing a document

Uploads a document to Cloudmersive to begin a series of one or more editing operations.  To edit a document, first call Begin Editing on the document.  Then perform operations on the document using the secure URL returned from BeginEditing, such as Word DOCX Delete Pages and Insert Table.  Finally, perform finish editing on the URL to return the resulting edited document.  The editing URL is temporary and only stored in-memory cache, and will automatically expire from the cache after 30 minutes, and cannot be directly accessed.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Begin editing a document
    api_response = api_instance.edit_document_begin_editing(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_begin_editing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_accept_all_track_changes**
> str edit_document_docx_accept_all_track_changes(input_file)

Accept all tracked changes, revisions in a Word DOCX document

Accepts all tracked changes and revisions in a Word DOCX document.  This will accept all pending changes in the document when tracked changes is turned on.  Track changes will remain on (if it is on) after this oepration is completed.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Accept all tracked changes, revisions in a Word DOCX document
    api_response = api_instance.edit_document_docx_accept_all_track_changes(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_accept_all_track_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_body**
> GetDocxBodyResponse edit_document_docx_body(req_config)

Get body from a Word DOCX document

Returns the body defined in the Word Document (DOCX) format file; this is the main content part of a DOCX document

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxBodyRequest() # GetDocxBodyRequest | Document input request

try:
    # Get body from a Word DOCX document
    api_response = api_instance.edit_document_docx_body(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_body: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxBodyRequest**](GetDocxBodyRequest.md)| Document input request | 

### Return type

[**GetDocxBodyResponse**](GetDocxBodyResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_create_blank_document**
> CreateBlankDocxResponse edit_document_docx_create_blank_document(input)

Create a blank Word DOCX document

Returns a blank Word DOCX Document format file.  The file is blank, with no contents.  Use additional editing commands such as Insert Paragraph or Insert Table or Insert Image to populate the document.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.CreateBlankDocxRequest() # CreateBlankDocxRequest | Document input request

try:
    # Create a blank Word DOCX document
    api_response = api_instance.edit_document_docx_create_blank_document(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_create_blank_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**CreateBlankDocxRequest**](CreateBlankDocxRequest.md)| Document input request | 

### Return type

[**CreateBlankDocxResponse**](CreateBlankDocxResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_delete_pages**
> str edit_document_docx_delete_pages(req_config)

Delete, remove pages from a Word DOCX document

Returns the edited Word Document in the Word Document (DOCX) format file with the specified pages removed

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.RemoveDocxPagesRequest() # RemoveDocxPagesRequest | Document input request

try:
    # Delete, remove pages from a Word DOCX document
    api_response = api_instance.edit_document_docx_delete_pages(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_delete_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**RemoveDocxPagesRequest**](RemoveDocxPagesRequest.md)| Document input request | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_delete_table_row**
> DeleteDocxTableRowResponse edit_document_docx_delete_table_row(req_config)

Deletes a table row in an existing table in a Word DOCX document

Deletes an existing table row in a Word DOCX Document and returns the result.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DeleteDocxTableRowRequest() # DeleteDocxTableRowRequest | Document input request

try:
    # Deletes a table row in an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_delete_table_row(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_delete_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DeleteDocxTableRowRequest**](DeleteDocxTableRowRequest.md)| Document input request | 

### Return type

[**DeleteDocxTableRowResponse**](DeleteDocxTableRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_delete_table_row_range**
> DeleteDocxTableRowRangeResponse edit_document_docx_delete_table_row_range(req_config)

Deletes a range of multiple table rows in an existing table in a Word DOCX document

Deletes a range of 1 or more existing table rows in a Word DOCX Document and returns the result.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DeleteDocxTableRowRangeRequest() # DeleteDocxTableRowRangeRequest | Document input request

try:
    # Deletes a range of multiple table rows in an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_delete_table_row_range(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_delete_table_row_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DeleteDocxTableRowRangeRequest**](DeleteDocxTableRowRangeRequest.md)| Document input request | 

### Return type

[**DeleteDocxTableRowRangeResponse**](DeleteDocxTableRowRangeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_disable_track_changes**
> str edit_document_docx_disable_track_changes(input_file)

Disable track changes, revisions in a Word DOCX document

Diables tracking of changes and revisions in a Word DOCX document, and accepts any pending changes.  Users editing the document will no longer see changes tracked automatically.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Disable track changes, revisions in a Word DOCX document
    api_response = api_instance.edit_document_docx_disable_track_changes(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_disable_track_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_enable_track_changes**
> str edit_document_docx_enable_track_changes(input_file)

Enable track changes, revisions in a Word DOCX document

Enables tracking of changes and revisions in a Word DOCX document.  Users editing the document will see changes tracked automatically, with edits highlighted, and the ability to accept or reject changes made to the document.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Enable track changes, revisions in a Word DOCX document
    api_response = api_instance.edit_document_docx_enable_track_changes(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_enable_track_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_find_paragraph**
> FindDocxParagraphResponse edit_document_docx_find_paragraph(req_config)

Find matching paragraphs in a Word DOCX document

Returns the paragraphs defined in the Word Document (DOCX) format file that match the input criteria

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.FindDocxParagraphRequest() # FindDocxParagraphRequest | Document input request

try:
    # Find matching paragraphs in a Word DOCX document
    api_response = api_instance.edit_document_docx_find_paragraph(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_find_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**FindDocxParagraphRequest**](FindDocxParagraphRequest.md)| Document input request | 

### Return type

[**FindDocxParagraphResponse**](FindDocxParagraphResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_comments**
> GetDocxCommentsResponse edit_document_docx_get_comments(req_config)

Get comments from a Word DOCX document as a flat list

Returns the comments and review annotations stored in the Word Document (DOCX) format file as a flattened list (not as a hierarchy of comments and replies).

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxGetCommentsRequest() # GetDocxGetCommentsRequest | Document input request

try:
    # Get comments from a Word DOCX document as a flat list
    api_response = api_instance.edit_document_docx_get_comments(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxGetCommentsRequest**](GetDocxGetCommentsRequest.md)| Document input request | 

### Return type

[**GetDocxCommentsResponse**](GetDocxCommentsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_comments_hierarchical**
> GetDocxCommentsHierarchicalResponse edit_document_docx_get_comments_hierarchical(req_config)

Get comments from a Word DOCX document hierarchically

Returns the comments and review annotations stored in the Word Document (DOCX) format file hierarchically, where reply comments are nested as children under top-level comments in the results returned.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxGetCommentsHierarchicalRequest() # GetDocxGetCommentsHierarchicalRequest | Document input request

try:
    # Get comments from a Word DOCX document hierarchically
    api_response = api_instance.edit_document_docx_get_comments_hierarchical(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_comments_hierarchical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxGetCommentsHierarchicalRequest**](GetDocxGetCommentsHierarchicalRequest.md)| Document input request | 

### Return type

[**GetDocxCommentsHierarchicalResponse**](GetDocxCommentsHierarchicalResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_headers_and_footers**
> GetDocxHeadersAndFootersResponse edit_document_docx_get_headers_and_footers(req_config)

Get content of a footer from a Word DOCX document

Returns the footer content from a Word Document (DOCX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxHeadersAndFootersRequest() # GetDocxHeadersAndFootersRequest | Document input request

try:
    # Get content of a footer from a Word DOCX document
    api_response = api_instance.edit_document_docx_get_headers_and_footers(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_headers_and_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxHeadersAndFootersRequest**](GetDocxHeadersAndFootersRequest.md)| Document input request | 

### Return type

[**GetDocxHeadersAndFootersResponse**](GetDocxHeadersAndFootersResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_images**
> GetDocxImagesResponse edit_document_docx_get_images(req_config)

Get images from a Word DOCX document

Returns the images defined in the Word Document (DOCX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxImagesRequest() # GetDocxImagesRequest | Document input request

try:
    # Get images from a Word DOCX document
    api_response = api_instance.edit_document_docx_get_images(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxImagesRequest**](GetDocxImagesRequest.md)| Document input request | 

### Return type

[**GetDocxImagesResponse**](GetDocxImagesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_macro_information**
> GetMacrosResponse edit_document_docx_get_macro_information(input_file)

Get macro information from a Word DOCX/DOCM document

Returns information about the Macros (e.g. VBA) defined in the Word Document

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Get macro information from a Word DOCX/DOCM document
    api_response = api_instance.edit_document_docx_get_macro_information(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_macro_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**GetMacrosResponse**](GetMacrosResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_metadata_properties**
> GetDocxMetadataPropertiesResponse edit_document_docx_get_metadata_properties(input_file)

Get all metadata properties in Word DOCX document

Returns all the metadata properties in an Office Word Document (docx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Get all metadata properties in Word DOCX document
    api_response = api_instance.edit_document_docx_get_metadata_properties(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_metadata_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**GetDocxMetadataPropertiesResponse**](GetDocxMetadataPropertiesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_sections**
> GetDocxSectionsResponse edit_document_docx_get_sections(req_config)

Get sections from a Word DOCX document

Returns the sections defined in the Word Document (DOCX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxSectionsRequest() # GetDocxSectionsRequest | Document input request

try:
    # Get sections from a Word DOCX document
    api_response = api_instance.edit_document_docx_get_sections(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxSectionsRequest**](GetDocxSectionsRequest.md)| Document input request | 

### Return type

[**GetDocxSectionsResponse**](GetDocxSectionsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_styles**
> GetDocxStylesResponse edit_document_docx_get_styles(req_config)

Get styles from a Word DOCX document

Returns the styles defined in the Word Document (DOCX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxStylesRequest() # GetDocxStylesRequest | Document input request

try:
    # Get styles from a Word DOCX document
    api_response = api_instance.edit_document_docx_get_styles(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxStylesRequest**](GetDocxStylesRequest.md)| Document input request | 

### Return type

[**GetDocxStylesResponse**](GetDocxStylesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_table_by_index**
> GetDocxTableByIndexResponse edit_document_docx_get_table_by_index(req_config)

Get a specific table by index in a Word DOCX document

Returns the specific table object by its 0-based index in an Office Word Document (DOCX)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxTableByIndexRequest() # GetDocxTableByIndexRequest | Document input request

try:
    # Get a specific table by index in a Word DOCX document
    api_response = api_instance.edit_document_docx_get_table_by_index(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_table_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxTableByIndexRequest**](GetDocxTableByIndexRequest.md)| Document input request | 

### Return type

[**GetDocxTableByIndexResponse**](GetDocxTableByIndexResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_table_row**
> GetDocxTableRowResponse edit_document_docx_get_table_row(req_config)

Gets the contents of an existing table row in an existing table in a Word DOCX document

Gets the contents of an existing table row in a Word DOCX Document and returns the result.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxTableRowRequest() # GetDocxTableRowRequest | Document input request

try:
    # Gets the contents of an existing table row in an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_get_table_row(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxTableRowRequest**](GetDocxTableRowRequest.md)| Document input request | 

### Return type

[**GetDocxTableRowResponse**](GetDocxTableRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_tables**
> GetDocxTablesResponse edit_document_docx_get_tables(req_config)

Get all tables in Word DOCX document

Returns all the table objects in an Office Word Document (docx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxTablesRequest() # GetDocxTablesRequest | Document input request

try:
    # Get all tables in Word DOCX document
    api_response = api_instance.edit_document_docx_get_tables(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxTablesRequest**](GetDocxTablesRequest.md)| Document input request | 

### Return type

[**GetDocxTablesResponse**](GetDocxTablesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_comment_on_paragraph**
> InsertDocxCommentOnParagraphResponse edit_document_docx_insert_comment_on_paragraph(req_config)

Insert a new comment into a Word DOCX document attached to a paragraph

Adds a new comment into a Word DOCX document attached to a paragraph and returns the result.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxInsertCommentOnParagraphRequest() # DocxInsertCommentOnParagraphRequest | Document input request

try:
    # Insert a new comment into a Word DOCX document attached to a paragraph
    api_response = api_instance.edit_document_docx_insert_comment_on_paragraph(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_comment_on_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxInsertCommentOnParagraphRequest**](DocxInsertCommentOnParagraphRequest.md)| Document input request | 

### Return type

[**InsertDocxCommentOnParagraphResponse**](InsertDocxCommentOnParagraphResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_image**
> DocxInsertImageResponse edit_document_docx_insert_image(req_config)

Insert image into a Word DOCX document

Set the footer in a Word Document (DOCX).  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxInsertImageRequest() # DocxInsertImageRequest | Document input request

try:
    # Insert image into a Word DOCX document
    api_response = api_instance.edit_document_docx_insert_image(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxInsertImageRequest**](DocxInsertImageRequest.md)| Document input request | 

### Return type

[**DocxInsertImageResponse**](DocxInsertImageResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_paragraph**
> InsertDocxInsertParagraphResponse edit_document_docx_insert_paragraph(req_config)

Insert a new paragraph into a Word DOCX document

Adds a new paragraph into a DOCX and returns the result.  You can insert at the beginning/end of a document, or before/after an existing object using its Path (location within the document).  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.InsertDocxInsertParagraphRequest() # InsertDocxInsertParagraphRequest | Document input request

try:
    # Insert a new paragraph into a Word DOCX document
    api_response = api_instance.edit_document_docx_insert_paragraph(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**InsertDocxInsertParagraphRequest**](InsertDocxInsertParagraphRequest.md)| Document input request | 

### Return type

[**InsertDocxInsertParagraphResponse**](InsertDocxInsertParagraphResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_table**
> InsertDocxTablesResponse edit_document_docx_insert_table(req_config)

Insert a new table into a Word DOCX document

Adds a new table into a DOCX and returns the result.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.InsertDocxTablesRequest() # InsertDocxTablesRequest | Document input request

try:
    # Insert a new table into a Word DOCX document
    api_response = api_instance.edit_document_docx_insert_table(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**InsertDocxTablesRequest**](InsertDocxTablesRequest.md)| Document input request | 

### Return type

[**InsertDocxTablesResponse**](InsertDocxTablesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_table_row**
> InsertDocxTableRowResponse edit_document_docx_insert_table_row(req_config)

Insert a new row into an existing table in a Word DOCX document

Adds a new table row into a DOCX Document and returns the result.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.InsertDocxTableRowRequest() # InsertDocxTableRowRequest | Document input request

try:
    # Insert a new row into an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_insert_table_row(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**InsertDocxTableRowRequest**](InsertDocxTableRowRequest.md)| Document input request | 

### Return type

[**InsertDocxTableRowResponse**](InsertDocxTableRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_pages**
> GetDocxPagesResponse edit_document_docx_pages(req_config)

Get pages and content from a Word DOCX document

Returns the pages and contents of each page defined in the Word Document (DOCX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.GetDocxPagesRequest() # GetDocxPagesRequest | Document input request

try:
    # Get pages and content from a Word DOCX document
    api_response = api_instance.edit_document_docx_pages(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxPagesRequest**](GetDocxPagesRequest.md)| Document input request | 

### Return type

[**GetDocxPagesResponse**](GetDocxPagesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_remove_all_comments**
> str edit_document_docx_remove_all_comments(input_file)

Remove all comments from a Word DOCX document

Removes all of the comments from a Word Document.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Remove all comments from a Word DOCX document
    api_response = api_instance.edit_document_docx_remove_all_comments(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_remove_all_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_remove_headers_and_footers**
> RemoveDocxHeadersAndFootersResponse edit_document_docx_remove_headers_and_footers(req_config)

Remove headers and footers from Word DOCX document

Remove all headers, or footers, or both from a Word Document (DOCX).  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.RemoveDocxHeadersAndFootersRequest() # RemoveDocxHeadersAndFootersRequest | Document input request

try:
    # Remove headers and footers from Word DOCX document
    api_response = api_instance.edit_document_docx_remove_headers_and_footers(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_remove_headers_and_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**RemoveDocxHeadersAndFootersRequest**](RemoveDocxHeadersAndFootersRequest.md)| Document input request | 

### Return type

[**RemoveDocxHeadersAndFootersResponse**](RemoveDocxHeadersAndFootersResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_remove_object**
> DocxRemoveObjectResponse edit_document_docx_remove_object(req_config)

Delete any object in a Word DOCX document

Delete any object, such as a paragraph, table, image, etc. from a Word Document (DOCX).  Pass in the Path of the object you would like to delete.  You can call other functions such as Get-Tables, Get-Images, Get-Body, etc. to get the paths of the objects in the document.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxRemoveObjectRequest() # DocxRemoveObjectRequest | Document input request

try:
    # Delete any object in a Word DOCX document
    api_response = api_instance.edit_document_docx_remove_object(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_remove_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxRemoveObjectRequest**](DocxRemoveObjectRequest.md)| Document input request | 

### Return type

[**DocxRemoveObjectResponse**](DocxRemoveObjectResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_replace**
> str edit_document_docx_replace(req_config)

Replace string in Word DOCX document

Replace all instances of a string in an Office Word Document (docx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.ReplaceStringRequest() # ReplaceStringRequest | Document string replacement configuration input

try:
    # Replace string in Word DOCX document
    api_response = api_instance.edit_document_docx_replace(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**ReplaceStringRequest**](ReplaceStringRequest.md)| Document string replacement configuration input | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_replace_multi**
> str edit_document_docx_replace_multi(req_config)

Replace multiple strings in Word DOCX document

Replace all instances of multiple strings in an Office Word Document (docx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.MultiReplaceStringRequest() # MultiReplaceStringRequest | Document string replacement configuration input

try:
    # Replace multiple strings in Word DOCX document
    api_response = api_instance.edit_document_docx_replace_multi(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_replace_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**MultiReplaceStringRequest**](MultiReplaceStringRequest.md)| Document string replacement configuration input | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_replace_paragraph**
> ReplaceDocxParagraphResponse edit_document_docx_replace_paragraph(req_config)

Replace matching paragraphs in a Word DOCX document

Returns the edited Word Document (DOCX) format file with the matching paragraphs replaced as requested.  Replace a paragraph with another object such as an image.  Useful for performing templating operations.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.ReplaceDocxParagraphRequest() # ReplaceDocxParagraphRequest | Document input request

try:
    # Replace matching paragraphs in a Word DOCX document
    api_response = api_instance.edit_document_docx_replace_paragraph(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_replace_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**ReplaceDocxParagraphRequest**](ReplaceDocxParagraphRequest.md)| Document input request | 

### Return type

[**ReplaceDocxParagraphResponse**](ReplaceDocxParagraphResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_set_custom_metadata_properties**
> str edit_document_docx_set_custom_metadata_properties(input)

Set custom property metadata properties in Word DOCX document

Sets the custom property metadata for the metadata properties in an Office Word Document (docx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.DocxSetCustomMetadataPropertiesRequest() # DocxSetCustomMetadataPropertiesRequest | 

try:
    # Set custom property metadata properties in Word DOCX document
    api_response = api_instance.edit_document_docx_set_custom_metadata_properties(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_custom_metadata_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DocxSetCustomMetadataPropertiesRequest**](DocxSetCustomMetadataPropertiesRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_set_footer**
> DocxSetFooterResponse edit_document_docx_set_footer(req_config)

Set the footer in a Word DOCX document

Set the footer in a Word Document (DOCX).  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxSetFooterRequest() # DocxSetFooterRequest | Document input request

try:
    # Set the footer in a Word DOCX document
    api_response = api_instance.edit_document_docx_set_footer(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxSetFooterRequest**](DocxSetFooterRequest.md)| Document input request | 

### Return type

[**DocxSetFooterResponse**](DocxSetFooterResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_set_footer_add_page_number**
> DocxSetFooterResponse edit_document_docx_set_footer_add_page_number(req_config)

Add page number to footer in a Word DOCX document

Set the footer in a Word Document (DOCX) to contain a page number.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxSetFooterAddPageNumberRequest() # DocxSetFooterAddPageNumberRequest | Document input request

try:
    # Add page number to footer in a Word DOCX document
    api_response = api_instance.edit_document_docx_set_footer_add_page_number(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_footer_add_page_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxSetFooterAddPageNumberRequest**](DocxSetFooterAddPageNumberRequest.md)| Document input request | 

### Return type

[**DocxSetFooterResponse**](DocxSetFooterResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_set_header**
> DocxSetHeaderResponse edit_document_docx_set_header(req_config)

Set the header in a Word DOCX document

Set the header in a Word Document (DOCX).  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.DocxSetHeaderRequest() # DocxSetHeaderRequest | Document input request

try:
    # Set the header in a Word DOCX document
    api_response = api_instance.edit_document_docx_set_header(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxSetHeaderRequest**](DocxSetHeaderRequest.md)| Document input request | 

### Return type

[**DocxSetHeaderResponse**](DocxSetHeaderResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_update_table_cell**
> UpdateDocxTableCellResponse edit_document_docx_update_table_cell(req_config)

Update, set contents of a table cell in an existing table in a Word DOCX document

Sets the contents of a table cell into a DOCX Document and returns the result.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.UpdateDocxTableCellRequest() # UpdateDocxTableCellRequest | Document input request

try:
    # Update, set contents of a table cell in an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_update_table_cell(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_update_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**UpdateDocxTableCellRequest**](UpdateDocxTableCellRequest.md)| Document input request | 

### Return type

[**UpdateDocxTableCellResponse**](UpdateDocxTableCellResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_update_table_row**
> UpdateDocxTableRowResponse edit_document_docx_update_table_row(req_config)

Update, set contents of a table row in an existing table in a Word DOCX document

Sets the contents of a table row into a DOCX Document and returns the result.  Call Finish Editing on the output URL to complete the operation.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.UpdateDocxTableRowRequest() # UpdateDocxTableRowRequest | Document input request

try:
    # Update, set contents of a table row in an existing table in a Word DOCX document
    api_response = api_instance.edit_document_docx_update_table_row(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_update_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**UpdateDocxTableRowRequest**](UpdateDocxTableRowRequest.md)| Document input request | 

### Return type

[**UpdateDocxTableRowResponse**](UpdateDocxTableRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_finish_editing**
> str edit_document_finish_editing(req_config)

Finish editing document, and download result from document editing

Once done editing a document, download the result.  Begin editing a document by calling begin-editing, then perform operations, then call finish-editing to get the result.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.FinishEditingRequest() # FinishEditingRequest | Cloudmersive Document URL to complete editing on

try:
    # Finish editing document, and download result from document editing
    api_response = api_instance.edit_document_finish_editing(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_finish_editing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**FinishEditingRequest**](FinishEditingRequest.md)| Cloudmersive Document URL to complete editing on | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_pptx_delete_slides**
> str edit_document_pptx_delete_slides(req_config)

Delete, remove slides from a PowerPoint PPTX presentation document

Edits the input PowerPoint PPTX presentation document to remove the specified slides

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.RemovePptxSlidesRequest() # RemovePptxSlidesRequest | Presentation input request

try:
    # Delete, remove slides from a PowerPoint PPTX presentation document
    api_response = api_instance.edit_document_pptx_delete_slides(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_pptx_delete_slides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**RemovePptxSlidesRequest**](RemovePptxSlidesRequest.md)| Presentation input request | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_pptx_get_macro_information**
> GetMacrosResponse edit_document_pptx_get_macro_information(input_file)

Get macro information from a PowerPoint PPTX/PPTM presentation document

Returns information about the Macros (e.g. VBA) defined in the PowerPoint Document

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Get macro information from a PowerPoint PPTX/PPTM presentation document
    api_response = api_instance.edit_document_pptx_get_macro_information(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_pptx_get_macro_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**GetMacrosResponse**](GetMacrosResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_pptx_replace**
> str edit_document_pptx_replace(req_config)

Replace string in PowerPoint PPTX presentation

Replace all instances of a string in an Office PowerPoint Document (pptx)

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.ReplaceStringRequest() # ReplaceStringRequest | Replacement document configuration input

try:
    # Replace string in PowerPoint PPTX presentation
    api_response = api_instance.edit_document_pptx_replace(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_pptx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**ReplaceStringRequest**](ReplaceStringRequest.md)| Replacement document configuration input | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_append_row**
> AppendXlsxRowResponse edit_document_xlsx_append_row(input)

Append row to a Excel XLSX spreadsheet, worksheet

Appends a row to the end of an Excel Spreadsheet worksheet.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.AppendXlsxRowRequest() # AppendXlsxRowRequest | Document input request

try:
    # Append row to a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_append_row(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_append_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**AppendXlsxRowRequest**](AppendXlsxRowRequest.md)| Document input request | 

### Return type

[**AppendXlsxRowResponse**](AppendXlsxRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_clear_cell_by_index**
> ClearXlsxCellResponse edit_document_xlsx_clear_cell_by_index(input)

Clear cell contents in an Excel XLSX spreadsheet, worksheet by index

Clears, sets to blank, the contents of a specific cell in an Excel XLSX spreadsheet, worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.ClearXlsxCellRequest() # ClearXlsxCellRequest | Document input request

try:
    # Clear cell contents in an Excel XLSX spreadsheet, worksheet by index
    api_response = api_instance.edit_document_xlsx_clear_cell_by_index(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_clear_cell_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ClearXlsxCellRequest**](ClearXlsxCellRequest.md)| Document input request | 

### Return type

[**ClearXlsxCellResponse**](ClearXlsxCellResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_clear_row**
> ClearXlsxRowResponse edit_document_xlsx_clear_row(input)

Clear row from a Excel XLSX spreadsheet, worksheet

Clears data from a specific row in the Excel Spreadsheet worksheet, leaving a blank row. Use the Get Rows And Cells API to enumerate available rows in a spreadsheet.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.ClearXlsxRowRequest() # ClearXlsxRowRequest | Document input request

try:
    # Clear row from a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_clear_row(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_clear_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ClearXlsxRowRequest**](ClearXlsxRowRequest.md)| Document input request | 

### Return type

[**ClearXlsxRowResponse**](ClearXlsxRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_create_blank_spreadsheet**
> CreateBlankSpreadsheetResponse edit_document_xlsx_create_blank_spreadsheet(input)

Create a blank Excel XLSX spreadsheet

Returns a blank Excel XLSX Spreadsheet (XLSX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.CreateBlankSpreadsheetRequest() # CreateBlankSpreadsheetRequest | Document input request

try:
    # Create a blank Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_create_blank_spreadsheet(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_create_blank_spreadsheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**CreateBlankSpreadsheetRequest**](CreateBlankSpreadsheetRequest.md)| Document input request | 

### Return type

[**CreateBlankSpreadsheetResponse**](CreateBlankSpreadsheetResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_create_spreadsheet_from_data**
> CreateSpreadsheetFromDataResponse edit_document_xlsx_create_spreadsheet_from_data(input)

Create a new Excel XLSX spreadsheet from column and row data

Returns a new Excel XLSX Spreadsheet (XLSX) format file populated with column and row data specified as input

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.CreateSpreadsheetFromDataRequest() # CreateSpreadsheetFromDataRequest | Document input request

try:
    # Create a new Excel XLSX spreadsheet from column and row data
    api_response = api_instance.edit_document_xlsx_create_spreadsheet_from_data(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_create_spreadsheet_from_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**CreateSpreadsheetFromDataRequest**](CreateSpreadsheetFromDataRequest.md)| Document input request | 

### Return type

[**CreateSpreadsheetFromDataResponse**](CreateSpreadsheetFromDataResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_delete_worksheet**
> str edit_document_xlsx_delete_worksheet(req_config)

Delete, remove worksheet from an Excel XLSX spreadsheet document

Edits the input Excel XLSX spreadsheet document to remove the specified worksheet (tab).  Use the Get Worksheets API to enumerate available worksheets in a spreadsheet.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
req_config = cloudmersive_convert_api_client.RemoveXlsxWorksheetRequest() # RemoveXlsxWorksheetRequest | Spreadsheet input request

try:
    # Delete, remove worksheet from an Excel XLSX spreadsheet document
    api_response = api_instance.edit_document_xlsx_delete_worksheet(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_delete_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**RemoveXlsxWorksheetRequest**](RemoveXlsxWorksheetRequest.md)| Spreadsheet input request | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_disable_shared_workbook**
> DisableSharedWorkbookResponse edit_document_xlsx_disable_shared_workbook(input)

Disable Shared Workbook (legacy) in Excel XLSX spreadsheet

Disable the Shared Workbook (legacy) mode in an Excel XLSX spreadsheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.DisableSharedWorkbookRequest() # DisableSharedWorkbookRequest | Document input request

try:
    # Disable Shared Workbook (legacy) in Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_disable_shared_workbook(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_disable_shared_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DisableSharedWorkbookRequest**](DisableSharedWorkbookRequest.md)| Document input request | 

### Return type

[**DisableSharedWorkbookResponse**](DisableSharedWorkbookResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_enable_shared_workbook**
> EnableSharedWorkbookResponse edit_document_xlsx_enable_shared_workbook(input)

Enable Shared Workbook (legacy) in Excel XLSX spreadsheet

Enables the Shared Workbook (legacy) mode in an Excel XLSX spreadsheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.EnableSharedWorkbookRequest() # EnableSharedWorkbookRequest | Document input request

try:
    # Enable Shared Workbook (legacy) in Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_enable_shared_workbook(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_enable_shared_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**EnableSharedWorkbookRequest**](EnableSharedWorkbookRequest.md)| Document input request | 

### Return type

[**EnableSharedWorkbookResponse**](EnableSharedWorkbookResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_cell_by_identifier**
> GetXlsxCellByIdentifierResponse edit_document_xlsx_get_cell_by_identifier(input)

Get cell from an Excel XLSX spreadsheet, worksheet by cell identifier

Returns the value of a specific cell based on its identifier (e.g. A1, B22, C33, etc.) in the Excel Spreadsheet worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxCellByIdentifierRequest() # GetXlsxCellByIdentifierRequest | Document input request

try:
    # Get cell from an Excel XLSX spreadsheet, worksheet by cell identifier
    api_response = api_instance.edit_document_xlsx_get_cell_by_identifier(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_cell_by_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxCellByIdentifierRequest**](GetXlsxCellByIdentifierRequest.md)| Document input request | 

### Return type

[**GetXlsxCellByIdentifierResponse**](GetXlsxCellByIdentifierResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_cell_by_index**
> GetXlsxCellResponse edit_document_xlsx_get_cell_by_index(input)

Get cell from an Excel XLSX spreadsheet, worksheet by index

Returns the value and definition of a specific cell in a specific row in the Excel Spreadsheet worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxCellRequest() # GetXlsxCellRequest | Document input request

try:
    # Get cell from an Excel XLSX spreadsheet, worksheet by index
    api_response = api_instance.edit_document_xlsx_get_cell_by_index(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_cell_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxCellRequest**](GetXlsxCellRequest.md)| Document input request | 

### Return type

[**GetXlsxCellResponse**](GetXlsxCellResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_columns**
> GetXlsxColumnsResponse edit_document_xlsx_get_columns(input)

Get columns from a Excel XLSX spreadsheet, worksheet

Returns the columns defined in the Excel Spreadsheet worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxColumnsRequest() # GetXlsxColumnsRequest | Document input request

try:
    # Get columns from a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_get_columns(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxColumnsRequest**](GetXlsxColumnsRequest.md)| Document input request | 

### Return type

[**GetXlsxColumnsResponse**](GetXlsxColumnsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_images**
> GetXlsxImagesResponse edit_document_xlsx_get_images(input)

Get images from a Excel XLSX spreadsheet, worksheet

Returns the images defined in the Excel Spreadsheet worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxImagesRequest() # GetXlsxImagesRequest | Document input request

try:
    # Get images from a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_get_images(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxImagesRequest**](GetXlsxImagesRequest.md)| Document input request | 

### Return type

[**GetXlsxImagesResponse**](GetXlsxImagesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_macro_information**
> GetMacrosResponse edit_document_xlsx_get_macro_information(input_file)

Get macro information from a Excel XLSX/XLSM spreadsheet, worksheet

Returns information about the Macros (e.g. VBA) defined in the Excel Spreadsheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Get macro information from a Excel XLSX/XLSM spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_get_macro_information(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_macro_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**GetMacrosResponse**](GetMacrosResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_rows_and_cells**
> GetXlsxRowsAndCellsResponse edit_document_xlsx_get_rows_and_cells(input)

Get rows and cells from a Excel XLSX spreadsheet, worksheet

Returns the rows and cells defined in the Excel Spreadsheet worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxRowsAndCellsRequest() # GetXlsxRowsAndCellsRequest | Document input request

try:
    # Get rows and cells from a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_get_rows_and_cells(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_rows_and_cells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxRowsAndCellsRequest**](GetXlsxRowsAndCellsRequest.md)| Document input request | 

### Return type

[**GetXlsxRowsAndCellsResponse**](GetXlsxRowsAndCellsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_specific_row**
> GetXlsxSpecificRowResponse edit_document_xlsx_get_specific_row(input)

Get a specific row from a Excel XLSX spreadsheet, worksheet by path

Returns the specific row and its cells defined in the Excel Spreadsheet worksheet based on the specified path.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxSpecificRowRequest() # GetXlsxSpecificRowRequest | Document input request

try:
    # Get a specific row from a Excel XLSX spreadsheet, worksheet by path
    api_response = api_instance.edit_document_xlsx_get_specific_row(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_specific_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxSpecificRowRequest**](GetXlsxSpecificRowRequest.md)| Document input request | 

### Return type

[**GetXlsxSpecificRowResponse**](GetXlsxSpecificRowResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_styles**
> GetXlsxStylesResponse edit_document_xlsx_get_styles(input)

Get styles from a Excel XLSX spreadsheet, worksheet

Returns the style defined in the Excel Spreadsheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxStylesRequest() # GetXlsxStylesRequest | Document input request

try:
    # Get styles from a Excel XLSX spreadsheet, worksheet
    api_response = api_instance.edit_document_xlsx_get_styles(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxStylesRequest**](GetXlsxStylesRequest.md)| Document input request | 

### Return type

[**GetXlsxStylesResponse**](GetXlsxStylesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_get_worksheets**
> GetXlsxWorksheetsResponse edit_document_xlsx_get_worksheets(input)

Get worksheets from a Excel XLSX spreadsheet

Returns the worksheets (tabs) defined in the Excel Spreadsheet (XLSX) format file

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.GetXlsxWorksheetsRequest() # GetXlsxWorksheetsRequest | Document input request

try:
    # Get worksheets from a Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_get_worksheets(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_get_worksheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetXlsxWorksheetsRequest**](GetXlsxWorksheetsRequest.md)| Document input request | 

### Return type

[**GetXlsxWorksheetsResponse**](GetXlsxWorksheetsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_insert_worksheet**
> InsertXlsxWorksheetResponse edit_document_xlsx_insert_worksheet(input)

Insert a new worksheet into an Excel XLSX spreadsheet

Inserts a new worksheet into an Excel Spreadsheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.InsertXlsxWorksheetRequest() # InsertXlsxWorksheetRequest | Document input request

try:
    # Insert a new worksheet into an Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_insert_worksheet(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_insert_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**InsertXlsxWorksheetRequest**](InsertXlsxWorksheetRequest.md)| Document input request | 

### Return type

[**InsertXlsxWorksheetResponse**](InsertXlsxWorksheetResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_rename_worksheet**
> RenameXlsxWorksheetResponse edit_document_xlsx_rename_worksheet(input)

Rename a specific worksheet in a Excel XLSX spreadsheet

Edits the input Excel XLSX spreadsheet document to rename a specified worksheet (tab).  Use the Get Worksheets API to enumerate available worksheets in a spreadsheet.

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.RenameXlsxWorksheetRequest() # RenameXlsxWorksheetRequest | Document input request

try:
    # Rename a specific worksheet in a Excel XLSX spreadsheet
    api_response = api_instance.edit_document_xlsx_rename_worksheet(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_rename_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**RenameXlsxWorksheetRequest**](RenameXlsxWorksheetRequest.md)| Document input request | 

### Return type

[**RenameXlsxWorksheetResponse**](RenameXlsxWorksheetResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_set_cell_by_identifier**
> SetXlsxCellByIdentifierResponse edit_document_xlsx_set_cell_by_identifier(input)

Set, update cell contents in an Excel XLSX spreadsheet, worksheet by cell identifier

Sets, updates the contents of a specific cell in an Excel XLSX spreadsheet, worksheet using its cell identifier (e.g. A1, B22, C33) in the worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.SetXlsxCellByIdentifierRequest() # SetXlsxCellByIdentifierRequest | Document input request

try:
    # Set, update cell contents in an Excel XLSX spreadsheet, worksheet by cell identifier
    api_response = api_instance.edit_document_xlsx_set_cell_by_identifier(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_set_cell_by_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SetXlsxCellByIdentifierRequest**](SetXlsxCellByIdentifierRequest.md)| Document input request | 

### Return type

[**SetXlsxCellByIdentifierResponse**](SetXlsxCellByIdentifierResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_xlsx_set_cell_by_index**
> SetXlsxCellResponse edit_document_xlsx_set_cell_by_index(input)

Set, update cell contents in an Excel XLSX spreadsheet, worksheet by index

Sets, updates the contents of a specific cell in an Excel XLSX spreadsheet, worksheet

### Example
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
api_instance = cloudmersive_convert_api_client.EditDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.SetXlsxCellRequest() # SetXlsxCellRequest | Document input request

try:
    # Set, update cell contents in an Excel XLSX spreadsheet, worksheet by index
    api_response = api_instance.edit_document_xlsx_set_cell_by_index(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_xlsx_set_cell_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SetXlsxCellRequest**](SetXlsxCellRequest.md)| Document input request | 

### Return type

[**SetXlsxCellResponse**](SetXlsxCellResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

