# cloudmersive_convert_api_client.EditDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_document_begin_editing**](EditDocumentApi.md#edit_document_begin_editing) | **POST** /convert/edit/begin-editing | Begin editing a document
[**edit_document_docx_body**](EditDocumentApi.md#edit_document_docx_body) | **POST** /convert/edit/docx/get-body | Get body from a Word DOCX document
[**edit_document_docx_get_headers_and_footers**](EditDocumentApi.md#edit_document_docx_get_headers_and_footers) | **POST** /convert/edit/docx/get-headers-and-footers | Get content of a footer from a Word DOCX document
[**edit_document_docx_get_images**](EditDocumentApi.md#edit_document_docx_get_images) | **POST** /convert/edit/docx/get-images | Get images from a Word DOCX document
[**edit_document_docx_get_sections**](EditDocumentApi.md#edit_document_docx_get_sections) | **POST** /convert/edit/docx/get-sections | Get sections from a Word DOCX document
[**edit_document_docx_get_styles**](EditDocumentApi.md#edit_document_docx_get_styles) | **POST** /convert/edit/docx/get-styles | Get styles from a Word DOCX document
[**edit_document_docx_get_tables**](EditDocumentApi.md#edit_document_docx_get_tables) | **POST** /convert/edit/docx/get-tables | Get tables in Word DOCX document
[**edit_document_docx_insert_image**](EditDocumentApi.md#edit_document_docx_insert_image) | **POST** /convert/edit/docx/insert-image | Insert image into a Word DOCX document
[**edit_document_docx_insert_paragraph**](EditDocumentApi.md#edit_document_docx_insert_paragraph) | **POST** /convert/edit/docx/insert-paragraph | Insert a new paragraph into a Word DOCX document
[**edit_document_docx_insert_table**](EditDocumentApi.md#edit_document_docx_insert_table) | **POST** /convert/edit/docx/insert-table | Insert a new table into a Word DOCX document
[**edit_document_docx_remove_headers_and_footers**](EditDocumentApi.md#edit_document_docx_remove_headers_and_footers) | **POST** /convert/edit/docx/remove-headers-and-footers | Remove headers and footers from Word DOCX document
[**edit_document_docx_remove_object**](EditDocumentApi.md#edit_document_docx_remove_object) | **POST** /convert/edit/docx/remove-object | Delete any object in a Word DOCX document
[**edit_document_docx_replace**](EditDocumentApi.md#edit_document_docx_replace) | **POST** /convert/edit/docx/replace-all | Replace string in Word DOCX document
[**edit_document_docx_set_footer**](EditDocumentApi.md#edit_document_docx_set_footer) | **POST** /convert/edit/docx/set-footer | Set the footer in a Word DOCX document
[**edit_document_docx_set_footer_add_page_number**](EditDocumentApi.md#edit_document_docx_set_footer_add_page_number) | **POST** /convert/edit/docx/set-footer/add-page-number | Add page number to footer in a Word DOCX document
[**edit_document_docx_set_header**](EditDocumentApi.md#edit_document_docx_set_header) | **POST** /convert/edit/docx/set-header | Set the header in a Word DOCX document
[**edit_document_finish_editing**](EditDocumentApi.md#edit_document_finish_editing) | **POST** /convert/edit/finish-editing | Download result from document editing
[**edit_document_pptx_replace**](EditDocumentApi.md#edit_document_pptx_replace) | **POST** /convert/edit/pptx/replace-all | Replace string in PowerPoint PPTX presentation
[**edit_document_xlsx_get_columns**](EditDocumentApi.md#edit_document_xlsx_get_columns) | **POST** /convert/edit/xlsx/get-columns | Get rows and cells from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_images**](EditDocumentApi.md#edit_document_xlsx_get_images) | **POST** /convert/edit/xlsx/get-images | Get images from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_rows_and_cells**](EditDocumentApi.md#edit_document_xlsx_get_rows_and_cells) | **POST** /convert/edit/xlsx/get-rows-and-cells | Get rows and cells from a Word XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_styles**](EditDocumentApi.md#edit_document_xlsx_get_styles) | **POST** /convert/edit/xlsx/get-styles | Get styles from a Excel XLSX spreadsheet, worksheet
[**edit_document_xlsx_get_worksheets**](EditDocumentApi.md#edit_document_xlsx_get_worksheets) | **POST** /convert/edit/xlsx/get-worksheets | Get worksheets from a Excel XLSX spreadsheet
[**edit_document_xlsx_insert_worksheet**](EditDocumentApi.md#edit_document_xlsx_insert_worksheet) | **POST** /convert/edit/xlsx/insert-worksheet | Insert a new worksheet into an Excel XLSX spreadsheet


# **edit_document_begin_editing**
> str edit_document_begin_editing(input_file)

Begin editing a document

Uploads a document to Cloudmersive to begin a series of one or more editing operations

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

# **edit_document_docx_get_tables**
> GetDocxTablesResponse edit_document_docx_get_tables(req_config)

Get tables in Word DOCX document

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
    # Get tables in Word DOCX document
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

# **edit_document_finish_editing**
> str edit_document_finish_editing(req_config)

Download result from document editing

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
    # Download result from document editing
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

# **edit_document_xlsx_get_columns**
> GetXlsxColumnsResponse edit_document_xlsx_get_columns(input)

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
input = cloudmersive_convert_api_client.GetXlsxColumnsRequest() # GetXlsxColumnsRequest | Document input request

try:
    # Get rows and cells from a Excel XLSX spreadsheet, worksheet
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

# **edit_document_xlsx_get_rows_and_cells**
> GetXlsxRowsAndCellsResponse edit_document_xlsx_get_rows_and_cells(input)

Get rows and cells from a Word XLSX spreadsheet, worksheet

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
    # Get rows and cells from a Word XLSX spreadsheet, worksheet
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

