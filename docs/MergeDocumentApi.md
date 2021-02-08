# cloudmersive_convert_api_client.MergeDocumentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merge_document_docx**](MergeDocumentApi.md#merge_document_docx) | **POST** /convert/merge/docx | Merge Two Word DOCX Together
[**merge_document_docx_multi**](MergeDocumentApi.md#merge_document_docx_multi) | **POST** /convert/merge/docx/multi | Merge Multple Word DOCX Together
[**merge_document_html**](MergeDocumentApi.md#merge_document_html) | **POST** /convert/merge/html | Merge Two HTML (HTM) Files Together
[**merge_document_html_multi**](MergeDocumentApi.md#merge_document_html_multi) | **POST** /convert/merge/html/multi | Merge Multple HTML (HTM) Files Together
[**merge_document_pdf**](MergeDocumentApi.md#merge_document_pdf) | **POST** /convert/merge/pdf | Merge Two PDF Files Together
[**merge_document_pdf_multi**](MergeDocumentApi.md#merge_document_pdf_multi) | **POST** /convert/merge/pdf/multi | Merge Multple PDF Files Together
[**merge_document_png**](MergeDocumentApi.md#merge_document_png) | **POST** /convert/merge/png/vertical | Merge Two PNG Files Together
[**merge_document_png_multi**](MergeDocumentApi.md#merge_document_png_multi) | **POST** /convert/merge/png/vertical/multi | Merge Multple PNG Files Together
[**merge_document_pptx**](MergeDocumentApi.md#merge_document_pptx) | **POST** /convert/merge/pptx | Merge Two PowerPoint PPTX Together
[**merge_document_pptx_multi**](MergeDocumentApi.md#merge_document_pptx_multi) | **POST** /convert/merge/pptx/multi | Merge Multple PowerPoint PPTX Together
[**merge_document_txt**](MergeDocumentApi.md#merge_document_txt) | **POST** /convert/merge/txt | Merge Two Text (TXT) Files Together
[**merge_document_txt_multi**](MergeDocumentApi.md#merge_document_txt_multi) | **POST** /convert/merge/txt/multi | Merge Multple Text (TXT) Files Together
[**merge_document_xlsx**](MergeDocumentApi.md#merge_document_xlsx) | **POST** /convert/merge/xlsx | Merge Two Excel XLSX Together
[**merge_document_xlsx_multi**](MergeDocumentApi.md#merge_document_xlsx_multi) | **POST** /convert/merge/xlsx/multi | Merge Multple Excel XLSX Together


# **merge_document_docx**
> str merge_document_docx(input_file1, input_file2)

Merge Two Word DOCX Together

Combine two Office Word Documents (docx) into one single Office Word document

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two Word DOCX Together
    api_response = api_instance.merge_document_docx(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_docx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_docx_multi**
> str merge_document_docx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple Word DOCX Together

Combine multiple Office Word Documents (docx) into one single Office Word document

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple Word DOCX Together
    api_response = api_instance.merge_document_docx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_docx_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_html**
> object merge_document_html(input_file1, input_file2)

Merge Two HTML (HTM) Files Together

Combine two HTML (.HTM) files into a single text document, preserving the order of the input documents in the combined document by stacking them vertically.  The title will be taken from the first document.

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two HTML (HTM) Files Together
    api_response = api_instance.merge_document_html(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_html_multi**
> str merge_document_html_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple HTML (HTM) Files Together

Combine multiple HTML (.HTM) files into a single text document, preserving the order of the input documents in the combined document by stacking them vertically.  The title will be taken from the first document.

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple HTML (HTM) Files Together
    api_response = api_instance.merge_document_html_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_html_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_pdf**
> str merge_document_pdf(input_file1, input_file2)

Merge Two PDF Files Together

Combine two PDF files (pdf) into a single PDF document, preserving the order of the input documents in the combined document

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two PDF Files Together
    api_response = api_instance.merge_document_pdf(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_pdf_multi**
> str merge_document_pdf_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple PDF Files Together

Combine multiple PDF files (pdf) into a single PDF document, preserving the order of the input documents in the combined document

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple PDF Files Together
    api_response = api_instance.merge_document_pdf_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_pdf_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_png**
> str merge_document_png(input_file1, input_file2)

Merge Two PNG Files Together

Combine two PNG files into a single PNG document, preserving the order of the input documents in the combined document by stacking them vertically

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two PNG Files Together
    api_response = api_instance.merge_document_png(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_png_multi**
> str merge_document_png_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple PNG Files Together

Combine multiple PNG files into a single PNG document, preserving the order of the input documents in the combined document by stacking them vertically

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple PNG Files Together
    api_response = api_instance.merge_document_png_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_png_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_pptx**
> str merge_document_pptx(input_file1, input_file2)

Merge Two PowerPoint PPTX Together

Combine two Office PowerPoint presentations (pptx) into one single Office PowerPoint presentation

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two PowerPoint PPTX Together
    api_response = api_instance.merge_document_pptx(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_pptx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_pptx_multi**
> str merge_document_pptx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple PowerPoint PPTX Together

Combine multiple Office PowerPoint presentations (pptx) into one single Office PowerPoint presentation

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple PowerPoint PPTX Together
    api_response = api_instance.merge_document_pptx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_pptx_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_txt**
> object merge_document_txt(input_file1, input_file2)

Merge Two Text (TXT) Files Together

Combine two Text (.TXT) files into a single text document, preserving the order of the input documents in the combined document by stacking them vertically.

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two Text (TXT) Files Together
    api_response = api_instance.merge_document_txt(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_txt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_txt_multi**
> str merge_document_txt_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple Text (TXT) Files Together

Combine multiple Text (.TXT) files into a single text document, preserving the order of the input documents in the combined document by stacking them vertically.

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple Text (TXT) Files Together
    api_response = api_instance.merge_document_txt_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_txt_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_xlsx**
> str merge_document_xlsx(input_file1, input_file2)

Merge Two Excel XLSX Together

Combine two Office Excel spreadsheets (xlsx) into a single Office Excel spreadsheet

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on (more than 2 can be supplied).

try:
    # Merge Two Excel XLSX Together
    api_response = api_instance.merge_document_xlsx(input_file1, input_file2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_xlsx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on (more than 2 can be supplied). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_document_xlsx_multi**
> str merge_document_xlsx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Merge Multple Excel XLSX Together

Combine multiple Office Excel spreadsheets (xlsx) into a single Office Excel spreadsheet

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
api_instance = cloudmersive_convert_api_client.MergeDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on.
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Merge Multple Excel XLSX Together
    api_response = api_instance.merge_document_xlsx_multi(input_file1, input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergeDocumentApi->merge_document_xlsx_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | 
 **input_file3** | **file**| Third input file to perform the operation on. | [optional] 
 **input_file4** | **file**| Fourth input file to perform the operation on. | [optional] 
 **input_file5** | **file**| Fifth input file to perform the operation on. | [optional] 
 **input_file6** | **file**| Sixth input file to perform the operation on. | [optional] 
 **input_file7** | **file**| Seventh input file to perform the operation on. | [optional] 
 **input_file8** | **file**| Eighth input file to perform the operation on. | [optional] 
 **input_file9** | **file**| Ninth input file to perform the operation on. | [optional] 
 **input_file10** | **file**| Tenth input file to perform the operation on. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

