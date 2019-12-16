# cloudmersive_convert_api_client.ConvertDataApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_data_csv_to_json**](ConvertDataApi.md#convert_data_csv_to_json) | **POST** /convert/csv/to/json | Convert CSV to JSON conversion
[**convert_data_json_to_xml**](ConvertDataApi.md#convert_data_json_to_xml) | **POST** /convert/json/to/xml | Convert JSON to XML conversion
[**convert_data_xls_to_json**](ConvertDataApi.md#convert_data_xls_to_json) | **POST** /convert/xls/to/json | Convert Excel (97-2003) XLS to JSON conversion
[**convert_data_xlsx_to_json**](ConvertDataApi.md#convert_data_xlsx_to_json) | **POST** /convert/xlsx/to/json | Convert Excel XLSX to JSON conversion
[**convert_data_xml_to_json**](ConvertDataApi.md#convert_data_xml_to_json) | **POST** /convert/xml/to/json | Convert XML to JSON conversion


# **convert_data_csv_to_json**
> object convert_data_csv_to_json(input_file)

Convert CSV to JSON conversion

Convert a CSV file to a JSON object array

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
api_instance = cloudmersive_convert_api_client.ConvertDataApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert CSV to JSON conversion
    api_response = api_instance.convert_data_csv_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_csv_to_json: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_json_to_xml**
> object convert_data_json_to_xml(json_object)

Convert JSON to XML conversion

Convert a JSON object into XML

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
api_instance = cloudmersive_convert_api_client.ConvertDataApi(cloudmersive_convert_api_client.ApiClient(configuration))
json_object = NULL # object | 

try:
    # Convert JSON to XML conversion
    api_response = api_instance.convert_data_json_to_xml(json_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_json_to_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_object** | **object**|  | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xls_to_json**
> object convert_data_xls_to_json(input_file)

Convert Excel (97-2003) XLS to JSON conversion

Convert an Excel (97-2003) XLS file to a JSON object array

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
api_instance = cloudmersive_convert_api_client.ConvertDataApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert Excel (97-2003) XLS to JSON conversion
    api_response = api_instance.convert_data_xls_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xls_to_json: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xlsx_to_json**
> object convert_data_xlsx_to_json(input_file)

Convert Excel XLSX to JSON conversion

Convert an Excel XLSX file to a JSON object array

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
api_instance = cloudmersive_convert_api_client.ConvertDataApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert Excel XLSX to JSON conversion
    api_response = api_instance.convert_data_xlsx_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xlsx_to_json: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_to_json**
> object convert_data_xml_to_json(input_file)

Convert XML to JSON conversion

Convert an XML string or file into JSON

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
api_instance = cloudmersive_convert_api_client.ConvertDataApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert XML to JSON conversion
    api_response = api_instance.convert_data_xml_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_to_json: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

