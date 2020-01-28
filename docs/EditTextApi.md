# cloudmersive_convert_api_client.EditTextApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_text_base64_decode**](EditTextApi.md#edit_text_base64_decode) | **POST** /convert/edit/text/encoding/base64/decode | Base 64 decode, convert base 64 string to binary content
[**edit_text_base64_detect**](EditTextApi.md#edit_text_base64_detect) | **POST** /convert/edit/text/encoding/base64/detect | Detect, check if text string is base 64 encoded
[**edit_text_base64_encode**](EditTextApi.md#edit_text_base64_encode) | **POST** /convert/edit/text/encoding/base64/encode | Base 64 encode, convert binary or file data to a text string
[**edit_text_change_line_endings**](EditTextApi.md#edit_text_change_line_endings) | **POST** /convert/edit/text/line-endings/change | Set, change line endings of a text file
[**edit_text_detect_line_endings**](EditTextApi.md#edit_text_detect_line_endings) | **POST** /convert/edit/text/line-endings/detect | Detect line endings of a text file
[**edit_text_find_regex**](EditTextApi.md#edit_text_find_regex) | **POST** /convert/edit/text/find/regex | Find a regular expression regex in text input
[**edit_text_find_simple**](EditTextApi.md#edit_text_find_simple) | **POST** /convert/edit/text/find/string | Find a string in text input
[**edit_text_remove_all_whitespace**](EditTextApi.md#edit_text_remove_all_whitespace) | **POST** /convert/edit/text/remove/whitespace/all | Remove whitespace from text string
[**edit_text_remove_html**](EditTextApi.md#edit_text_remove_html) | **POST** /convert/edit/text/remove/html | Remove HTML from text string
[**edit_text_replace_regex**](EditTextApi.md#edit_text_replace_regex) | **POST** /convert/edit/text/replace/regex | Replace a string in text with a regex regular expression string
[**edit_text_replace_simple**](EditTextApi.md#edit_text_replace_simple) | **POST** /convert/edit/text/replace/string | Replace a string in text with another string value
[**edit_text_text_encoding_detect**](EditTextApi.md#edit_text_text_encoding_detect) | **POST** /convert/edit/text/encoding/detect | Detect text encoding of file
[**edit_text_trim_whitespace**](EditTextApi.md#edit_text_trim_whitespace) | **POST** /convert/edit/text/remove/whitespace/trim | Trim leading and trailing whitespace from text string


# **edit_text_base64_decode**
> Base64DecodeResponse edit_text_base64_decode(request)

Base 64 decode, convert base 64 string to binary content

Decodes / converts base 64 UTF-8 text string to binary content

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.Base64DecodeRequest() # Base64DecodeRequest | Input request

try:
    # Base 64 decode, convert base 64 string to binary content
    api_response = api_instance.edit_text_base64_decode(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_base64_decode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Base64DecodeRequest**](Base64DecodeRequest.md)| Input request | 

### Return type

[**Base64DecodeResponse**](Base64DecodeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_base64_detect**
> Base64DetectResponse edit_text_base64_detect(request)

Detect, check if text string is base 64 encoded

Checks, detects if input string is base 64 encoded

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.Base64DetectRequest() # Base64DetectRequest | Input request

try:
    # Detect, check if text string is base 64 encoded
    api_response = api_instance.edit_text_base64_detect(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_base64_detect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Base64DetectRequest**](Base64DetectRequest.md)| Input request | 

### Return type

[**Base64DetectResponse**](Base64DetectResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_base64_encode**
> Base64EncodeResponse edit_text_base64_encode(request)

Base 64 encode, convert binary or file data to a text string

Encodes / converts binary or file data to a text string

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.Base64EncodeRequest() # Base64EncodeRequest | Input request

try:
    # Base 64 encode, convert binary or file data to a text string
    api_response = api_instance.edit_text_base64_encode(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_base64_encode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Base64EncodeRequest**](Base64EncodeRequest.md)| Input request | 

### Return type

[**Base64EncodeResponse**](Base64EncodeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_change_line_endings**
> ChangeLineEndingResponse edit_text_change_line_endings(line_ending_type, input_file)

Set, change line endings of a text file

Sets the line ending type of a text file; set to Windows, Unix or Mac.

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
line_ending_type = 'line_ending_type_example' # str | Required; 'Windows' will use carriage return and line feed, 'Unix' will use newline, and 'Mac' will use carriage return
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Set, change line endings of a text file
    api_response = api_instance.edit_text_change_line_endings(line_ending_type, input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_change_line_endings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_ending_type** | **str**| Required; &#39;Windows&#39; will use carriage return and line feed, &#39;Unix&#39; will use newline, and &#39;Mac&#39; will use carriage return | 
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**ChangeLineEndingResponse**](ChangeLineEndingResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_detect_line_endings**
> DetectLineEndingsResponse edit_text_detect_line_endings(input_file)

Detect line endings of a text file

Detect line ending type (Windows, Unix or Mac) of an input file.

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Detect line endings of a text file
    api_response = api_instance.edit_text_detect_line_endings(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_detect_line_endings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**DetectLineEndingsResponse**](DetectLineEndingsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_find_regex**
> FindStringRegexResponse edit_text_find_regex(request)

Find a regular expression regex in text input

Find all occurrences of the input regular expression in the input content, and returns the matches

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.FindStringRegexRequest() # FindStringRegexRequest | Input request

try:
    # Find a regular expression regex in text input
    api_response = api_instance.edit_text_find_regex(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_find_regex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FindStringRegexRequest**](FindStringRegexRequest.md)| Input request | 

### Return type

[**FindStringRegexResponse**](FindStringRegexResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_find_simple**
> FindStringSimpleResponse edit_text_find_simple(request)

Find a string in text input

Finds all occurrences of the input string in the input content, and returns the matches

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.FindStringSimpleRequest() # FindStringSimpleRequest | Input request

try:
    # Find a string in text input
    api_response = api_instance.edit_text_find_simple(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_find_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FindStringSimpleRequest**](FindStringSimpleRequest.md)| Input request | 

### Return type

[**FindStringSimpleResponse**](FindStringSimpleResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_remove_all_whitespace**
> RemoveWhitespaceFromTextResponse edit_text_remove_all_whitespace(request)

Remove whitespace from text string

Removes all whitespace from text, leaving behind only non-whitespace characters.  Whitespace includes newlines, spaces and other whitespace characters.

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.RemoveWhitespaceFromTextRequest() # RemoveWhitespaceFromTextRequest | Input request

try:
    # Remove whitespace from text string
    api_response = api_instance.edit_text_remove_all_whitespace(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_remove_all_whitespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RemoveWhitespaceFromTextRequest**](RemoveWhitespaceFromTextRequest.md)| Input request | 

### Return type

[**RemoveWhitespaceFromTextResponse**](RemoveWhitespaceFromTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_remove_html**
> RemoveHtmlFromTextResponse edit_text_remove_html(request)

Remove HTML from text string

Removes HTML from text, leaving behind only text.  Formatted text will become plain text.  Important for protecting against HTML and Cross-Site-Scripting attacks.

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.RemoveHtmlFromTextRequest() # RemoveHtmlFromTextRequest | Input request

try:
    # Remove HTML from text string
    api_response = api_instance.edit_text_remove_html(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_remove_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RemoveHtmlFromTextRequest**](RemoveHtmlFromTextRequest.md)| Input request | 

### Return type

[**RemoveHtmlFromTextResponse**](RemoveHtmlFromTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_replace_regex**
> ReplaceStringRegexResponse edit_text_replace_regex(request)

Replace a string in text with a regex regular expression string

Replaces all occurrences of the input regular expression regex string in the input content, and returns the result

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.ReplaceStringRegexRequest() # ReplaceStringRegexRequest | Input request

try:
    # Replace a string in text with a regex regular expression string
    api_response = api_instance.edit_text_replace_regex(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_replace_regex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ReplaceStringRegexRequest**](ReplaceStringRegexRequest.md)| Input request | 

### Return type

[**ReplaceStringRegexResponse**](ReplaceStringRegexResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_replace_simple**
> ReplaceStringSimpleResponse edit_text_replace_simple(request)

Replace a string in text with another string value

Replaces all occurrences of the input string in the input content, and returns the result

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.ReplaceStringSimpleRequest() # ReplaceStringSimpleRequest | Input request

try:
    # Replace a string in text with another string value
    api_response = api_instance.edit_text_replace_simple(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_replace_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ReplaceStringSimpleRequest**](ReplaceStringSimpleRequest.md)| Input request | 

### Return type

[**ReplaceStringSimpleResponse**](ReplaceStringSimpleResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_text_encoding_detect**
> TextEncodingDetectResponse edit_text_text_encoding_detect(input_file)

Detect text encoding of file

Checks text encoding of file

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Detect text encoding of file
    api_response = api_instance.edit_text_text_encoding_detect(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_text_encoding_detect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**TextEncodingDetectResponse**](TextEncodingDetectResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_text_trim_whitespace**
> RemoveWhitespaceFromTextResponse edit_text_trim_whitespace(request)

Trim leading and trailing whitespace from text string

Trim leading and trailing whitespace from text, leaving behind a trimmed string.  Whitespace includes newlines, spaces and other whitespace characters.

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
api_instance = cloudmersive_convert_api_client.EditTextApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.RemoveWhitespaceFromTextRequest() # RemoveWhitespaceFromTextRequest | Input request

try:
    # Trim leading and trailing whitespace from text string
    api_response = api_instance.edit_text_trim_whitespace(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditTextApi->edit_text_trim_whitespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RemoveWhitespaceFromTextRequest**](RemoveWhitespaceFromTextRequest.md)| Input request | 

### Return type

[**RemoveWhitespaceFromTextResponse**](RemoveWhitespaceFromTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

