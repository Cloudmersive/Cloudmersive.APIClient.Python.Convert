# cloudmersive_convert_api_client.ValidateDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_document_autodetect_validation**](ValidateDocumentApi.md#validate_document_autodetect_validation) | **POST** /convert/validate/autodetect | Autodetect content type and validate
[**validate_document_docx_validation**](ValidateDocumentApi.md#validate_document_docx_validation) | **POST** /convert/validate/docx | Validate a Word document (DOCX)
[**validate_document_executable_validation**](ValidateDocumentApi.md#validate_document_executable_validation) | **POST** /convert/validate/executable | Validate if a file is executable
[**validate_document_json_validation**](ValidateDocumentApi.md#validate_document_json_validation) | **POST** /convert/validate/json | Validate a JSON file
[**validate_document_pdf_validation**](ValidateDocumentApi.md#validate_document_pdf_validation) | **POST** /convert/validate/pdf | Validate a PDF document file
[**validate_document_pptx_validation**](ValidateDocumentApi.md#validate_document_pptx_validation) | **POST** /convert/validate/pptx | Validate a PowerPoint presentation (PPTX)
[**validate_document_xlsx_validation**](ValidateDocumentApi.md#validate_document_xlsx_validation) | **POST** /convert/validate/xlsx | Validate a Excel document (XLSX)
[**validate_document_xml_validation**](ValidateDocumentApi.md#validate_document_xml_validation) | **POST** /convert/validate/xml | Validate an XML file


# **validate_document_autodetect_validation**
> AutodetectDocumentValidationResult validate_document_autodetect_validation(input_file)

Autodetect content type and validate

Automatically detect the type of content, verify and validate that the content is indeed fully valid at depth, and then report the validation result.

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Autodetect content type and validate
    api_response = api_instance.validate_document_autodetect_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_autodetect_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**AutodetectDocumentValidationResult**](AutodetectDocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_docx_validation**
> DocumentValidationResult validate_document_docx_validation(input_file)

Validate a Word document (DOCX)

Validate a Word document (DOCX); if the document is not valid, identifies the errors in the document

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate a Word document (DOCX)
    api_response = api_instance.validate_document_docx_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_docx_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_executable_validation**
> DocumentValidationResult validate_document_executable_validation(input_file)

Validate if a file is executable

Validate if an input file is a binary executable file; if the document is not valid

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate if a file is executable
    api_response = api_instance.validate_document_executable_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_executable_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_json_validation**
> DocumentValidationResult validate_document_json_validation(input_file)

Validate a JSON file

Validate a JSON (JavaScript Object Notation) document file; if the document is not valid, identifies the errors in the document

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate a JSON file
    api_response = api_instance.validate_document_json_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_json_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_pdf_validation**
> DocumentValidationResult validate_document_pdf_validation(input_file)

Validate a PDF document file

Validate a PDF document; if the document is not valid, identifies the errors in the document.  Also checks if the PDF is password protected.

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate a PDF document file
    api_response = api_instance.validate_document_pdf_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_pdf_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_pptx_validation**
> DocumentValidationResult validate_document_pptx_validation(input_file)

Validate a PowerPoint presentation (PPTX)

Validate a PowerPoint presentation (PPTX); if the document is not valid, identifies the errors in the document

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate a PowerPoint presentation (PPTX)
    api_response = api_instance.validate_document_pptx_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_pptx_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_xlsx_validation**
> DocumentValidationResult validate_document_xlsx_validation(input_file)

Validate a Excel document (XLSX)

Validate a Excel document (XLSX); if the document is not valid, identifies the errors in the document

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate a Excel document (XLSX)
    api_response = api_instance.validate_document_xlsx_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_xlsx_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_document_xml_validation**
> DocumentValidationResult validate_document_xml_validation(input_file)

Validate an XML file

Validate an XML document file; if the document is not valid, identifies the errors in the document

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
api_instance = cloudmersive_convert_api_client.ValidateDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Validate an XML file
    api_response = api_instance.validate_document_xml_validation(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateDocumentApi->validate_document_xml_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DocumentValidationResult**](DocumentValidationResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

