# cloudmersive_convert_api_client.SplitDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**split_document_docx**](SplitDocumentApi.md#split_document_docx) | **POST** /convert/split/docx | Split a single Word Document DOCX into Separate Documents by Page
[**split_document_pdf_by_page**](SplitDocumentApi.md#split_document_pdf_by_page) | **POST** /convert/split/pdf | Split a PDF file into separate PDF files, one per page
[**split_document_pptx**](SplitDocumentApi.md#split_document_pptx) | **POST** /convert/split/pptx | Split a single PowerPoint Presentation PPTX into Separate Slides
[**split_document_txt_by_line**](SplitDocumentApi.md#split_document_txt_by_line) | **POST** /convert/split/txt/by-line | Split a single Text file (txt) into lines
[**split_document_txt_by_string**](SplitDocumentApi.md#split_document_txt_by_string) | **POST** /convert/split/txt/by-string | Split a single Text file (txt) by a string delimiter
[**split_document_xlsx**](SplitDocumentApi.md#split_document_xlsx) | **POST** /convert/split/xlsx | Split a single Excel XLSX into Separate Worksheets


# **split_document_docx**
> SplitDocxDocumentResult split_document_docx(input_file, return_document_contents=return_document_contents)

Split a single Word Document DOCX into Separate Documents by Page

Split a Word DOCX Document, comprised of multiple pages into separate Word DOCX document files, with each containing exactly one page.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
return_document_contents = true # bool | Set to true to return the contents of each Worksheet directly, set to false to only return URLs to each resulting document.  Default is true. (optional)

try:
    # Split a single Word Document DOCX into Separate Documents by Page
    api_response = api_instance.split_document_docx(input_file, return_document_contents=return_document_contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_docx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **return_document_contents** | **bool**| Set to true to return the contents of each Worksheet directly, set to false to only return URLs to each resulting document.  Default is true. | [optional] 

### Return type

[**SplitDocxDocumentResult**](SplitDocxDocumentResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document_pdf_by_page**
> SplitPdfResult split_document_pdf_by_page(input_file, return_document_contents=return_document_contents)

Split a PDF file into separate PDF files, one per page

Split an input PDF file into separate pages, comprised of one PDF file per page.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
return_document_contents = true # bool | Set to true to directly return all of the document contents in the DocumentContents field; set to false to return contents as temporary URLs (more efficient for large operations).  Default is false. (optional)

try:
    # Split a PDF file into separate PDF files, one per page
    api_response = api_instance.split_document_pdf_by_page(input_file, return_document_contents=return_document_contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_pdf_by_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **return_document_contents** | **bool**| Set to true to directly return all of the document contents in the DocumentContents field; set to false to return contents as temporary URLs (more efficient for large operations).  Default is false. | [optional] 

### Return type

[**SplitPdfResult**](SplitPdfResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document_pptx**
> SplitPptxPresentationResult split_document_pptx(input_file, return_document_contents=return_document_contents)

Split a single PowerPoint Presentation PPTX into Separate Slides

Split an PowerPoint PPTX Presentation, comprised of multiple slides into separate PowerPoint PPTX presentation files, with each containing exactly one slide.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
return_document_contents = true # bool | Set to true to return the contents of each presentation directly, set to false to only return URLs to each resulting presentation.  Default is true. (optional)

try:
    # Split a single PowerPoint Presentation PPTX into Separate Slides
    api_response = api_instance.split_document_pptx(input_file, return_document_contents=return_document_contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_pptx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **return_document_contents** | **bool**| Set to true to return the contents of each presentation directly, set to false to only return URLs to each resulting presentation.  Default is true. | [optional] 

### Return type

[**SplitPptxPresentationResult**](SplitPptxPresentationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document_txt_by_line**
> SplitTextDocumentByLinesResult split_document_txt_by_line(input_file)

Split a single Text file (txt) into lines

Split a Text (txt) Document by line, returning each line separately in order.  Supports multiple types of newlines.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Split a single Text file (txt) into lines
    api_response = api_instance.split_document_txt_by_line(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_txt_by_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**SplitTextDocumentByLinesResult**](SplitTextDocumentByLinesResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document_txt_by_string**
> SplitTextDocumentByStringResult split_document_txt_by_string(input_file, split_delimiter, skip_empty_elements=skip_empty_elements)

Split a single Text file (txt) by a string delimiter

Split a Text (txt) Document by a string delimiter, returning each component of the string as an array of strings.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
split_delimiter = 'split_delimiter_example' # str | Required; String to split up the input file on
skip_empty_elements = true # bool | Optional; If true, empty elements will be skipped in the output (optional)

try:
    # Split a single Text file (txt) by a string delimiter
    api_response = api_instance.split_document_txt_by_string(input_file, split_delimiter, skip_empty_elements=skip_empty_elements)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_txt_by_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **split_delimiter** | **str**| Required; String to split up the input file on | 
 **skip_empty_elements** | **bool**| Optional; If true, empty elements will be skipped in the output | [optional] 

### Return type

[**SplitTextDocumentByStringResult**](SplitTextDocumentByStringResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document_xlsx**
> SplitXlsxWorksheetResult split_document_xlsx(input_file, return_document_contents=return_document_contents)

Split a single Excel XLSX into Separate Worksheets

Split an Excel XLSX Spreadsheet, comprised of multiple Worksheets (or Tabs) into separate Excel XLSX spreadsheet files, with each containing exactly one Worksheet.

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
api_instance = cloudmersive_convert_api_client.SplitDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
return_document_contents = true # bool | Set to true to return the contents of each Worksheet directly, set to false to only return URLs to each resulting worksheet.  Default is true. (optional)

try:
    # Split a single Excel XLSX into Separate Worksheets
    api_response = api_instance.split_document_xlsx(input_file, return_document_contents=return_document_contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SplitDocumentApi->split_document_xlsx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **return_document_contents** | **bool**| Set to true to return the contents of each Worksheet directly, set to false to only return URLs to each resulting worksheet.  Default is true. | [optional] 

### Return type

[**SplitXlsxWorksheetResult**](SplitXlsxWorksheetResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

