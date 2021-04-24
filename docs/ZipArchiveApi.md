# cloudmersive_convert_api_client.ZipArchiveApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zip_archive_zip_create**](ZipArchiveApi.md#zip_archive_zip_create) | **POST** /convert/archive/zip/create | Compress files to create a new zip archive
[**zip_archive_zip_create_advanced**](ZipArchiveApi.md#zip_archive_zip_create_advanced) | **POST** /convert/archive/zip/create/advanced | Compress files and folders to create a new zip archive with advanced options
[**zip_archive_zip_create_encrypted**](ZipArchiveApi.md#zip_archive_zip_create_encrypted) | **POST** /convert/archive/zip/create/encrypted | Compress files to create a new, encrypted and password-protected zip archive
[**zip_archive_zip_create_quarantine**](ZipArchiveApi.md#zip_archive_zip_create_quarantine) | **POST** /convert/archive/zip/create/quarantine | Create an encrypted zip file to quarantine a dangerous file
[**zip_archive_zip_decrypt**](ZipArchiveApi.md#zip_archive_zip_decrypt) | **POST** /convert/archive/zip/decrypt | Decrypt and remove password protection on a zip file
[**zip_archive_zip_encrypt_advanced**](ZipArchiveApi.md#zip_archive_zip_encrypt_advanced) | **POST** /convert/archive/zip/encrypt/advanced | Encrypt and password protect a zip file
[**zip_archive_zip_extract**](ZipArchiveApi.md#zip_archive_zip_extract) | **POST** /convert/archive/zip/extract | Extract, decompress files and folders from a zip archive


# **zip_archive_zip_create**
> str zip_archive_zip_create(input_file1, input_file2=input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

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
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on. (optional)
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Compress files to create a new zip archive
    api_response = api_instance.zip_archive_zip_create(input_file1, input_file2=input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file1** | **file**| First input file to perform the operation on. | 
 **input_file2** | **file**| Second input file to perform the operation on. | [optional] 
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

# **zip_archive_zip_create_encrypted**
> str zip_archive_zip_create_encrypted(password, input_file1, encryption_algorithm=encryption_algorithm, input_file2=input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)

Compress files to create a new, encrypted and password-protected zip archive

Create a new zip archive by compressing input files, and also applies encryption and password protection to the zip.

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
password = 'password_example' # str | Password to place on the Zip file; the longer the password, the more secure
input_file1 = '/path/to/file.txt' # file | First input file to perform the operation on.
encryption_algorithm = 'encryption_algorithm_example' # str | Encryption algorithm to use; possible values are AES-256 (recommended), AES-128, and PK-Zip (not recommended; legacy, weak encryption algorithm). Default is AES-256. (optional)
input_file2 = '/path/to/file.txt' # file | Second input file to perform the operation on. (optional)
input_file3 = '/path/to/file.txt' # file | Third input file to perform the operation on. (optional)
input_file4 = '/path/to/file.txt' # file | Fourth input file to perform the operation on. (optional)
input_file5 = '/path/to/file.txt' # file | Fifth input file to perform the operation on. (optional)
input_file6 = '/path/to/file.txt' # file | Sixth input file to perform the operation on. (optional)
input_file7 = '/path/to/file.txt' # file | Seventh input file to perform the operation on. (optional)
input_file8 = '/path/to/file.txt' # file | Eighth input file to perform the operation on. (optional)
input_file9 = '/path/to/file.txt' # file | Ninth input file to perform the operation on. (optional)
input_file10 = '/path/to/file.txt' # file | Tenth input file to perform the operation on. (optional)

try:
    # Compress files to create a new, encrypted and password-protected zip archive
    api_response = api_instance.zip_archive_zip_create_encrypted(password, input_file1, encryption_algorithm=encryption_algorithm, input_file2=input_file2, input_file3=input_file3, input_file4=input_file4, input_file5=input_file5, input_file6=input_file6, input_file7=input_file7, input_file8=input_file8, input_file9=input_file9, input_file10=input_file10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_create_encrypted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| Password to place on the Zip file; the longer the password, the more secure | 
 **input_file1** | **file**| First input file to perform the operation on. | 
 **encryption_algorithm** | **str**| Encryption algorithm to use; possible values are AES-256 (recommended), AES-128, and PK-Zip (not recommended; legacy, weak encryption algorithm). Default is AES-256. | [optional] 
 **input_file2** | **file**| Second input file to perform the operation on. | [optional] 
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

# **zip_archive_zip_create_quarantine**
> object zip_archive_zip_create_quarantine()

Create an encrypted zip file to quarantine a dangerous file

Create a new zip archive by compressing input files, and also applies encryption and password protection to the zip, for the purposes of quarantining the underlyikng file.

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
    # Create an encrypted zip file to quarantine a dangerous file
    api_response = api_instance.zip_archive_zip_create_quarantine()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_create_quarantine: %s\n" % e)
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

# **zip_archive_zip_decrypt**
> object zip_archive_zip_decrypt(input_file, zip_password)

Decrypt and remove password protection on a zip file

Decrypts and removes password protection from an encrypted zip file with the specified password

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
zip_password = 'zip_password_example' # str | Required; Password for the input archive

try:
    # Decrypt and remove password protection on a zip file
    api_response = api_instance.zip_archive_zip_decrypt(input_file, zip_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **zip_password** | **str**| Required; Password for the input archive | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zip_archive_zip_encrypt_advanced**
> object zip_archive_zip_encrypt_advanced(encryption_request)

Encrypt and password protect a zip file

Encrypts and password protects an existing zip file with the specified password and encryption algorithm

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
encryption_request = cloudmersive_convert_api_client.ZipEncryptionAdvancedRequest() # ZipEncryptionAdvancedRequest | Encryption request

try:
    # Encrypt and password protect a zip file
    api_response = api_instance.zip_archive_zip_encrypt_advanced(encryption_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipArchiveApi->zip_archive_zip_encrypt_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encryption_request** | [**ZipEncryptionAdvancedRequest**](ZipEncryptionAdvancedRequest.md)| Encryption request | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

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

