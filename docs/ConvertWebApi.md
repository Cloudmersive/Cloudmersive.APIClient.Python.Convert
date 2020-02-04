# cloudmersive_convert_api_client.ConvertWebApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_web_html_to_docx**](ConvertWebApi.md#convert_web_html_to_docx) | **POST** /convert/html/to/docx | Convert HTML to Word DOCX Document
[**convert_web_html_to_pdf**](ConvertWebApi.md#convert_web_html_to_pdf) | **POST** /convert/web/html/to/pdf | Convert HTML string to PDF
[**convert_web_html_to_png**](ConvertWebApi.md#convert_web_html_to_png) | **POST** /convert/web/html/to/png | Convert HTML string to PNG screenshot
[**convert_web_html_to_txt**](ConvertWebApi.md#convert_web_html_to_txt) | **POST** /convert/web/html/to/txt | Convert HTML string to text (txt)
[**convert_web_md_to_html**](ConvertWebApi.md#convert_web_md_to_html) | **POST** /convert/web/md/to/html | Convert Markdown to HTML
[**convert_web_url_to_pdf**](ConvertWebApi.md#convert_web_url_to_pdf) | **POST** /convert/web/url/to/pdf | Convert a URL to PDF
[**convert_web_url_to_screenshot**](ConvertWebApi.md#convert_web_url_to_screenshot) | **POST** /convert/web/url/to/screenshot | Take screenshot of URL
[**convert_web_url_to_txt**](ConvertWebApi.md#convert_web_url_to_txt) | **POST** /convert/web/url/to/txt | Convert website URL page to text (txt)


# **convert_web_html_to_docx**
> str convert_web_html_to_docx(input_request)

Convert HTML to Word DOCX Document

Convert HTML to Office Word Document (DOCX) format

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_request = cloudmersive_convert_api_client.HtmlToOfficeRequest() # HtmlToOfficeRequest | HTL input to convert to DOCX

try:
    # Convert HTML to Word DOCX Document
    api_response = api_instance.convert_web_html_to_docx(input_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_html_to_docx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_request** | [**HtmlToOfficeRequest**](HtmlToOfficeRequest.md)| HTL input to convert to DOCX | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_html_to_pdf**
> str convert_web_html_to_pdf(input)

Convert HTML string to PDF

Fully renders a website and returns a PDF of the HTML.  Javascript, HTML5, CSS and other advanced features are all supported.

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.HtmlToPdfRequest() # HtmlToPdfRequest | HTML to PDF request parameters

try:
    # Convert HTML string to PDF
    api_response = api_instance.convert_web_html_to_pdf(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_html_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**HtmlToPdfRequest**](HtmlToPdfRequest.md)| HTML to PDF request parameters | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_html_to_png**
> object convert_web_html_to_png(input)

Convert HTML string to PNG screenshot

Fully renders a website and returns a PNG (screenshot) of the HTML.  Javascript, HTML5, CSS and other advanced features are all supported.

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.HtmlToPngRequest() # HtmlToPngRequest | HTML to PNG request parameters

try:
    # Convert HTML string to PNG screenshot
    api_response = api_instance.convert_web_html_to_png(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_html_to_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**HtmlToPngRequest**](HtmlToPngRequest.md)| HTML to PNG request parameters | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_html_to_txt**
> HtmlToTextResponse convert_web_html_to_txt(input)

Convert HTML string to text (txt)

Converts an HTML string input into text (txt); extracts text from HTML

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.HtmlToTextRequest() # HtmlToTextRequest | HTML to Text request parameters

try:
    # Convert HTML string to text (txt)
    api_response = api_instance.convert_web_html_to_txt(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_html_to_txt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**HtmlToTextRequest**](HtmlToTextRequest.md)| HTML to Text request parameters | 

### Return type

[**HtmlToTextResponse**](HtmlToTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_md_to_html**
> HtmlMdResult convert_web_md_to_html(input_file)

Convert Markdown to HTML

Convert a markdown file (.md) to HTML

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Convert Markdown to HTML
    api_response = api_instance.convert_web_md_to_html(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_md_to_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**HtmlMdResult**](HtmlMdResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_url_to_pdf**
> str convert_web_url_to_pdf(input)

Convert a URL to PDF

Fully renders a website and returns a PDF of the full page.  Javascript, HTML5, CSS and other advanced features are all supported.

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.UrlToPdfRequest() # UrlToPdfRequest | URL to PDF request parameters

try:
    # Convert a URL to PDF
    api_response = api_instance.convert_web_url_to_pdf(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_url_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**UrlToPdfRequest**](UrlToPdfRequest.md)| URL to PDF request parameters | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_url_to_screenshot**
> str convert_web_url_to_screenshot(input)

Take screenshot of URL

Fully renders a website and returns a PNG screenshot of the full page image.  Javascript, HTML5, CSS and other advanced features are all supported.

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.ScreenshotRequest() # ScreenshotRequest | Screenshot request parameters

try:
    # Take screenshot of URL
    api_response = api_instance.convert_web_url_to_screenshot(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_url_to_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ScreenshotRequest**](ScreenshotRequest.md)| Screenshot request parameters | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_web_url_to_txt**
> UrlToTextResponse convert_web_url_to_txt(input)

Convert website URL page to text (txt)

Converts a website URL page into text (txt); extracts text from HTML

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
api_instance = cloudmersive_convert_api_client.ConvertWebApi(cloudmersive_convert_api_client.ApiClient(configuration))
input = cloudmersive_convert_api_client.UrlToTextRequest() # UrlToTextRequest | HTML to Text request parameters

try:
    # Convert website URL page to text (txt)
    api_response = api_instance.convert_web_url_to_txt(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertWebApi->convert_web_url_to_txt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**UrlToTextRequest**](UrlToTextRequest.md)| HTML to Text request parameters | 

### Return type

[**UrlToTextResponse**](UrlToTextResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

