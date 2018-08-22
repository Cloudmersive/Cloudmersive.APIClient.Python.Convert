# cloudmersive_convert_api_client.EditDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_document_begin_editing**](EditDocumentApi.md#edit_document_begin_editing) | **POST** /convert/edit/begin-editing | Begin editing a document
[**edit_document_docx_get_headers_and_footers**](EditDocumentApi.md#edit_document_docx_get_headers_and_footers) | **POST** /convert/edit/docx/get-headers-and-footers | Get content of a footer from a DOCX
[**edit_document_docx_get_styles**](EditDocumentApi.md#edit_document_docx_get_styles) | **POST** /convert/edit/docx/get-styles | Get styles from a DOCX
[**edit_document_docx_get_tables**](EditDocumentApi.md#edit_document_docx_get_tables) | **POST** /convert/edit/docx/get-tables | Get tables in DOCX
[**edit_document_docx_insert_image**](EditDocumentApi.md#edit_document_docx_insert_image) | **POST** /convert/edit/docx/insert-image | Insert image into a DOCX
[**edit_document_docx_insert_table**](EditDocumentApi.md#edit_document_docx_insert_table) | **POST** /convert/edit/docx/insert-table | Insert a new table into a DOCX
[**edit_document_docx_remove_headers_and_footers**](EditDocumentApi.md#edit_document_docx_remove_headers_and_footers) | **POST** /convert/edit/docx/remove-headers-and-footers | Remove headers and footers from DOCX
[**edit_document_docx_replace**](EditDocumentApi.md#edit_document_docx_replace) | **POST** /convert/edit/docx/replace-all | Replace string in DOCX
[**edit_document_docx_set_footer**](EditDocumentApi.md#edit_document_docx_set_footer) | **POST** /convert/edit/docx/set-footer | Set the footer in a DOCX
[**edit_document_docx_set_header**](EditDocumentApi.md#edit_document_docx_set_header) | **POST** /convert/edit/docx/set-header | Set the header in a DOCX
[**edit_document_finish_editing**](EditDocumentApi.md#edit_document_finish_editing) | **POST** /convert/edit/finish-editing | Download result from document editing
[**edit_document_pptx_replace**](EditDocumentApi.md#edit_document_pptx_replace) | **POST** /convert/edit/pptx/replace-all | Replace string in PPTX


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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_headers_and_footers**
> GetDocxHeadersAndFootersResponse edit_document_docx_get_headers_and_footers(req_config)

Get content of a footer from a DOCX

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
req_config = cloudmersive_convert_api_client.GetDocxHeadersAndFootersRequest() # GetDocxHeadersAndFootersRequest | 

try:
    # Get content of a footer from a DOCX
    api_response = api_instance.edit_document_docx_get_headers_and_footers(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_headers_and_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxHeadersAndFootersRequest**](GetDocxHeadersAndFootersRequest.md)|  | 

### Return type

[**GetDocxHeadersAndFootersResponse**](GetDocxHeadersAndFootersResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_styles**
> GetDocxStylesResponse edit_document_docx_get_styles(req_config)

Get styles from a DOCX

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
req_config = cloudmersive_convert_api_client.GetDocxStylesRequest() # GetDocxStylesRequest | 

try:
    # Get styles from a DOCX
    api_response = api_instance.edit_document_docx_get_styles(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxStylesRequest**](GetDocxStylesRequest.md)|  | 

### Return type

[**GetDocxStylesResponse**](GetDocxStylesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_get_tables**
> GetDocxTablesResponse edit_document_docx_get_tables(req_config)

Get tables in DOCX

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
req_config = cloudmersive_convert_api_client.GetDocxTablesRequest() # GetDocxTablesRequest | 

try:
    # Get tables in DOCX
    api_response = api_instance.edit_document_docx_get_tables(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**GetDocxTablesRequest**](GetDocxTablesRequest.md)|  | 

### Return type

[**GetDocxTablesResponse**](GetDocxTablesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_image**
> DocxInsertImageResponse edit_document_docx_insert_image(req_config)

Insert image into a DOCX

Set the footer in a Word Document (DOCX)

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
req_config = cloudmersive_convert_api_client.DocxInsertImageRequest() # DocxInsertImageRequest | 

try:
    # Insert image into a DOCX
    api_response = api_instance.edit_document_docx_insert_image(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxInsertImageRequest**](DocxInsertImageRequest.md)|  | 

### Return type

[**DocxInsertImageResponse**](DocxInsertImageResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_insert_table**
> InsertDocxTablesResponse edit_document_docx_insert_table(req_config)

Insert a new table into a DOCX

Adds a new table into a DOCX and returns the result

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
req_config = cloudmersive_convert_api_client.InsertDocxTablesRequest() # InsertDocxTablesRequest | 

try:
    # Insert a new table into a DOCX
    api_response = api_instance.edit_document_docx_insert_table(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_insert_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**InsertDocxTablesRequest**](InsertDocxTablesRequest.md)|  | 

### Return type

[**InsertDocxTablesResponse**](InsertDocxTablesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_remove_headers_and_footers**
> RemoveDocxHeadersAndFootersResponse edit_document_docx_remove_headers_and_footers(req_config)

Remove headers and footers from DOCX

Remove all headers, or footers, or both from a Word Document (DOCX)

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
req_config = cloudmersive_convert_api_client.RemoveDocxHeadersAndFootersRequest() # RemoveDocxHeadersAndFootersRequest | 

try:
    # Remove headers and footers from DOCX
    api_response = api_instance.edit_document_docx_remove_headers_and_footers(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_remove_headers_and_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**RemoveDocxHeadersAndFootersRequest**](RemoveDocxHeadersAndFootersRequest.md)|  | 

### Return type

[**RemoveDocxHeadersAndFootersResponse**](RemoveDocxHeadersAndFootersResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_replace**
> str edit_document_docx_replace(req_config)

Replace string in DOCX

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
req_config = cloudmersive_convert_api_client.ReplaceStringRequest() # ReplaceStringRequest | 

try:
    # Replace string in DOCX
    api_response = api_instance.edit_document_docx_replace(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**ReplaceStringRequest**](ReplaceStringRequest.md)|  | 

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

Set the footer in a DOCX

Set the footer in a Word Document (DOCX)

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
req_config = cloudmersive_convert_api_client.DocxSetFooterRequest() # DocxSetFooterRequest | 

try:
    # Set the footer in a DOCX
    api_response = api_instance.edit_document_docx_set_footer(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxSetFooterRequest**](DocxSetFooterRequest.md)|  | 

### Return type

[**DocxSetFooterResponse**](DocxSetFooterResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_document_docx_set_header**
> DocxSetHeaderResponse edit_document_docx_set_header(req_config)

Set the header in a DOCX

Set the header in a Word Document (DOCX)

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
req_config = cloudmersive_convert_api_client.DocxSetHeaderRequest() # DocxSetHeaderRequest | 

try:
    # Set the header in a DOCX
    api_response = api_instance.edit_document_docx_set_header(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_docx_set_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**DocxSetHeaderRequest**](DocxSetHeaderRequest.md)|  | 

### Return type

[**DocxSetHeaderResponse**](DocxSetHeaderResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

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
req_config = cloudmersive_convert_api_client.FinishEditingRequest() # FinishEditingRequest | 

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
 **req_config** | [**FinishEditingRequest**](FinishEditingRequest.md)|  | 

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

Replace string in PPTX

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
req_config = cloudmersive_convert_api_client.ReplaceStringRequest() # ReplaceStringRequest | 

try:
    # Replace string in PPTX
    api_response = api_instance.edit_document_pptx_replace(req_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditDocumentApi->edit_document_pptx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_config** | [**ReplaceStringRequest**](ReplaceStringRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

