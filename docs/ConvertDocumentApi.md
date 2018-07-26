# cloudmersive_convert_api_client.ConvertDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document_autodetect_to_pdf**](ConvertDocumentApi.md#convert_document_autodetect_to_pdf) | **POST** /convert/autodetect/to/pdf | Convert Document to PDF
[**convert_document_docx_to_pdf**](ConvertDocumentApi.md#convert_document_docx_to_pdf) | **POST** /convert/docx/to/pdf | Word DOCX to PDF
[**convert_document_pptx_to_pdf**](ConvertDocumentApi.md#convert_document_pptx_to_pdf) | **POST** /convert/pptx/to/pdf | PowerPoint PPTX to PDF
[**convert_document_xlsx_to_csv**](ConvertDocumentApi.md#convert_document_xlsx_to_csv) | **POST** /convert/xlsx/to/csv | Excel XLSX to CSV
[**convert_document_xlsx_to_pdf**](ConvertDocumentApi.md#convert_document_xlsx_to_pdf) | **POST** /convert/xlsx/to/pdf | Excel XLSX to PDF


# **convert_document_autodetect_to_pdf**
> object convert_document_autodetect_to_pdf(input_file)

Convert Document to PDF

Automatically detect file type and convert it to PDF.

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
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert Document to PDF
    api_response = api_instance.convert_document_autodetect_to_pdf(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_autodetect_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document_docx_to_pdf**
> object convert_document_docx_to_pdf(input_file)

Word DOCX to PDF

Convert Office Word Documents (docx) to standard PDF

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
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Word DOCX to PDF
    api_response = api_instance.convert_document_docx_to_pdf(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_docx_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document_pptx_to_pdf**
> object convert_document_pptx_to_pdf(input_file)

PowerPoint PPTX to PDF

Convert Office PowerPoint Documents (pptx) to standard PDF

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
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # PowerPoint PPTX to PDF
    api_response = api_instance.convert_document_pptx_to_pdf(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_pptx_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document_xlsx_to_csv**
> object convert_document_xlsx_to_csv(input_file)

Excel XLSX to CSV

Convert Office Excel Workbooks (xlsx) to standard Comma-Separated Values (CSV) format.

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
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Excel XLSX to CSV
    api_response = api_instance.convert_document_xlsx_to_csv(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_xlsx_to_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document_xlsx_to_pdf**
> object convert_document_xlsx_to_pdf(input_file)

Excel XLSX to PDF

Convert Office Excel Workbooks (xlsx) to standard PDF.  Converts all worksheets in the workbook to PDF.

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
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Excel XLSX to PDF
    api_response = api_instance.convert_document_xlsx_to_pdf(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_xlsx_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

