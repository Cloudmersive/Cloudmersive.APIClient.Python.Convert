# cloudmersive_convert_api_client.ZipArchiveApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zip_archive_zip_create**](ZipArchiveApi.md#zip_archive_zip_create) | **POST** /convert/archive/zip/create | Compress files to create a new zip archive
[**zip_archive_zip_create_advanced**](ZipArchiveApi.md#zip_archive_zip_create_advanced) | **POST** /convert/archive/zip/create/advanced | Compress files and folders to create a new zip archive with advanced options
[**zip_archive_zip_extract**](ZipArchiveApi.md#zip_archive_zip_extract) | **POST** /convert/archive/zip/extract | Extract, decompress files and folders from a zip archive


# **zip_archive_zip_create**
> object zip_archive_zip_create()

Compress files to create a new zip archive

Create a new zip archive by compressing input files.

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
api_instance = cloudmersive_convert_api_client.ZipArchiveApi(cloudmersive_convert_api_client.ApiClient(configuration))

try:
    # Compress files to create a new zip archive
    api_response = api_instance.zip_archive_zip_create()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zip_archive_zip_create_advanced**
> object zip_archive_zip_create_advanced(request)

Compress files and folders to create a new zip archive with advanced options

Create a new zip archive by compressing input files, folders and leverage advanced options to control the structure of the resulting zip archive.

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
api_instance = cloudmersive_convert_api_client.ZipArchiveApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.CreateZipArchiveRequest() # CreateZipArchiveRequest | Input request

try:
    # Compress files and folders to create a new zip archive with advanced options
    api_response = api_instance.zip_archive_zip_create_advanced(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_create_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateZipArchiveRequest**](CreateZipArchiveRequest.md)| Input request | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zip_archive_zip_extract**
> ZipExtractResponse zip_archive_zip_extract(input_file)

Extract, decompress files and folders from a zip archive

Extracts a zip archive by decompressing files, and folders.

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
api_instance = cloudmersive_convert_api_client.ZipArchiveApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Extract, decompress files and folders from a zip archive
    api_response = api_instance.zip_archive_zip_extract(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**ZipExtractResponse**](ZipExtractResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

