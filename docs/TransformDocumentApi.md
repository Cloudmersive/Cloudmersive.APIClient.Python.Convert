# cloudmersive_convert_api_client.TransformDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transform_document_docx_replace**](TransformDocumentApi.md#transform_document_docx_replace) | **POST** /convert/transform/docx/replace-all | Replace string in Word DOCX document
[**transform_document_pptx_replace**](TransformDocumentApi.md#transform_document_pptx_replace) | **POST** /convert/transform/pptx/replace-all | Replace string in PowerPoint PPTX presentation


# **transform_document_docx_replace**
> str transform_document_docx_replace(match_string, replace_string, input_file=input_file, input_file_url=input_file_url, match_case=match_case)

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
api_instance = cloudmersive_convert_api_client.TransformDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
match_string = 'match_string_example' # str | String to search for and match against, to be replaced
replace_string = 'replace_string_example' # str | String to replace the matched values with
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). (optional)
match_case = true # bool | Optional: True if the case should be matched, false for case insensitive match. Default is false. (optional)

try:
    # Replace string in Word DOCX document
    api_response = api_instance.transform_document_docx_replace(match_string, replace_string, input_file=input_file, input_file_url=input_file_url, match_case=match_case)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransformDocumentApi->transform_document_docx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_string** | **str**| String to search for and match against, to be replaced | 
 **replace_string** | **str**| String to replace the matched values with | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
 **match_case** | **bool**| Optional: True if the case should be matched, false for case insensitive match. Default is false. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_document_pptx_replace**
> str transform_document_pptx_replace(match_string, replace_string, input_file=input_file, input_file_url=input_file_url, match_case=match_case)

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
api_instance = cloudmersive_convert_api_client.TransformDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
match_string = 'match_string_example' # str | String to search for and match against, to be replaced
replace_string = 'replace_string_example' # str | String to replace the matched values with
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). (optional)
match_case = true # bool | Optional: True if the case should be matched, false for case insensitive match. Default is false. (optional)

try:
    # Replace string in PowerPoint PPTX presentation
    api_response = api_instance.transform_document_pptx_replace(match_string, replace_string, input_file=input_file, input_file_url=input_file_url, match_case=match_case)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransformDocumentApi->transform_document_pptx_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_string** | **str**| String to search for and match against, to be replaced | 
 **replace_string** | **str**| String to replace the matched values with | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
 **match_case** | **bool**| Optional: True if the case should be matched, false for case insensitive match. Default is false. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

