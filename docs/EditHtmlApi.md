# cloudmersive_convert_api_client.EditHtmlApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_html_html_append_header_tag**](EditHtmlApi.md#edit_html_html_append_header_tag) | **POST** /convert/edit/html/head/append/tag | Append an HTML tag to the HEAD section of an HTML Document
[**edit_html_html_append_heading**](EditHtmlApi.md#edit_html_html_append_heading) | **POST** /convert/edit/html/append/heading | Append a Heading to an HTML Document
[**edit_html_html_append_image_from_url**](EditHtmlApi.md#edit_html_html_append_image_from_url) | **POST** /convert/edit/html/append/image/from-url | Append an Image to an HTML Document from a URL
[**edit_html_html_append_image_inline**](EditHtmlApi.md#edit_html_html_append_image_inline) | **POST** /convert/edit/html/append/image/inline | Append a Base64 Inline Image to an HTML Document
[**edit_html_html_append_paragraph**](EditHtmlApi.md#edit_html_html_append_paragraph) | **POST** /convert/edit/html/append/paragraph | Append a Paragraph to an HTML Document
[**edit_html_html_create_blank_document**](EditHtmlApi.md#edit_html_html_create_blank_document) | **POST** /convert/edit/html/create/blank | Create a Blank HTML Document
[**edit_html_html_get_language**](EditHtmlApi.md#edit_html_html_get_language) | **POST** /convert/edit/html/head/get/language | Gets the language for the HTML document
[**edit_html_html_get_links**](EditHtmlApi.md#edit_html_html_get_links) | **POST** /convert/edit/html/extract/links | Extract resolved link URLs from HTML File
[**edit_html_html_get_rel_canonical**](EditHtmlApi.md#edit_html_html_get_rel_canonical) | **POST** /convert/edit/html/head/get/rel-canonical-url | Gets the rel canonical URL for the HTML document
[**edit_html_html_get_sitemap**](EditHtmlApi.md#edit_html_html_get_sitemap) | **POST** /convert/edit/html/head/get/sitemap-url | Gets the sitemap URL for the HTML document
[**edit_html_html_set_language**](EditHtmlApi.md#edit_html_html_set_language) | **POST** /convert/edit/html/head/set/language | Sets the language for the HTML document
[**edit_html_html_set_rel_canonical**](EditHtmlApi.md#edit_html_html_set_rel_canonical) | **POST** /convert/edit/html/head/set/rel-canonical-url | Sets the rel canonical URL for the HTML document
[**edit_html_html_set_sitemap_url**](EditHtmlApi.md#edit_html_html_set_sitemap_url) | **POST** /convert/edit/html/head/set/sitemap-url | Sets the sitemap URL for the HTML document


# **edit_html_html_append_header_tag**
> str edit_html_html_append_header_tag(html_tag, input_file=input_file, input_file_url=input_file_url)

Append an HTML tag to the HEAD section of an HTML Document

Appends an HTML tag to the HEAD section of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
html_tag = 'html_tag_example' # str | The HTML tag to append.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Append an HTML tag to the HEAD section of an HTML Document
    api_response = api_instance.edit_html_html_append_header_tag(html_tag, input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_append_header_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **html_tag** | **str**| The HTML tag to append. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_append_heading**
> str edit_html_html_append_heading(heading_text, input_file=input_file, input_file_url=input_file_url, heading_size=heading_size, css_style=css_style)

Append a Heading to an HTML Document

Appends a heading to the end of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
heading_text = 'heading_text_example' # str | The text content to be used in the header.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)
heading_size = 56 # int | Optional: The heading size number. Default is 1. Accepts values between 1 and 6. (optional)
css_style = 'css_style_example' # str | Optional: The CSS style for the heading. (optional)

try:
    # Append a Heading to an HTML Document
    api_response = api_instance.edit_html_html_append_heading(heading_text, input_file=input_file, input_file_url=input_file_url, heading_size=heading_size, css_style=css_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_append_heading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heading_text** | **str**| The text content to be used in the header. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 
 **heading_size** | **int**| Optional: The heading size number. Default is 1. Accepts values between 1 and 6. | [optional] 
 **css_style** | **str**| Optional: The CSS style for the heading. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_append_image_from_url**
> str edit_html_html_append_image_from_url(image_url, input_file=input_file, input_file_url=input_file_url, css_style=css_style)

Append an Image to an HTML Document from a URL

Appends an image to the end of an HTML document using a URL.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
image_url = 'image_url_example' # str | The URL for the image.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)
css_style = 'css_style_example' # str | Optional: CSS style for the image. (optional)

try:
    # Append an Image to an HTML Document from a URL
    api_response = api_instance.edit_html_html_append_image_from_url(image_url, input_file=input_file, input_file_url=input_file_url, css_style=css_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_append_image_from_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The URL for the image. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 
 **css_style** | **str**| Optional: CSS style for the image. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_append_image_inline**
> str edit_html_html_append_image_inline(input_file=input_file, input_file_url=input_file_url, image_file=image_file, image_url=image_url, css_style=css_style, image_extension=image_extension)

Append a Base64 Inline Image to an HTML Document

Appends a base64 inline image to the end of an HTML document from an input file or URL.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)
image_file = '/path/to/file.txt' # file | Optional: Image file to be appended as base64 inline image. (optional)
image_url = 'image_url_example' # str | Optional: Image URL to be appended as base64 inline image. (optional)
css_style = 'css_style_example' # str | Optional: CSS style for the image. (optional)
image_extension = 'image_extension_example' # str | Optional: The extension (JPG, PNG, GIF, etc.) of the image file. Recommended if uploading an imageFile directly, instead of using imageUrl. If no extension can be determined, will default to JPG. (optional)

try:
    # Append a Base64 Inline Image to an HTML Document
    api_response = api_instance.edit_html_html_append_image_inline(input_file=input_file, input_file_url=input_file_url, image_file=image_file, image_url=image_url, css_style=css_style, image_extension=image_extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_append_image_inline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 
 **image_file** | **file**| Optional: Image file to be appended as base64 inline image. | [optional] 
 **image_url** | **str**| Optional: Image URL to be appended as base64 inline image. | [optional] 
 **css_style** | **str**| Optional: CSS style for the image. | [optional] 
 **image_extension** | **str**| Optional: The extension (JPG, PNG, GIF, etc.) of the image file. Recommended if uploading an imageFile directly, instead of using imageUrl. If no extension can be determined, will default to JPG. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_append_paragraph**
> str edit_html_html_append_paragraph(paragraph_text, input_file=input_file, input_file_url=input_file_url, css_style=css_style)

Append a Paragraph to an HTML Document

Appends a paragraph to the end of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
paragraph_text = 'paragraph_text_example' # str | The text content to be used in the paragraph.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)
css_style = 'css_style_example' # str | Optional: The CSS style for the paragraph. (optional)

try:
    # Append a Paragraph to an HTML Document
    api_response = api_instance.edit_html_html_append_paragraph(paragraph_text, input_file=input_file, input_file_url=input_file_url, css_style=css_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_append_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paragraph_text** | **str**| The text content to be used in the paragraph. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 
 **css_style** | **str**| Optional: The CSS style for the paragraph. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_create_blank_document**
> str edit_html_html_create_blank_document(title=title, css_url=css_url, css_inline=css_inline, javascript_url=javascript_url, javascript_inline=javascript_inline)

Create a Blank HTML Document

Returns a blank HTML Document format file.  The file is blank, with no contents by default.  Use the optional input parameters to add various starting elements.  Use additional editing commands such as Append Header, Append Paragraph or Append Image from URL to populate the document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
title = 'title_example' # str | Optional: The title of the HTML document (optional)
css_url = 'css_url_example' # str | Optional: A CSS style URL to be added to the document. (optional)
css_inline = 'css_inline_example' # str | Optional: An inline CSS style to be added to the document. (optional)
javascript_url = 'javascript_url_example' # str | Optional: Javascript URL to be added to the document. (optional)
javascript_inline = 'javascript_inline_example' # str | Optional: Inline Javascript to be added to the document. (optional)

try:
    # Create a Blank HTML Document
    api_response = api_instance.edit_html_html_create_blank_document(title=title, css_url=css_url, css_inline=css_inline, javascript_url=javascript_url, javascript_inline=javascript_inline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_create_blank_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Optional: The title of the HTML document | [optional] 
 **css_url** | **str**| Optional: A CSS style URL to be added to the document. | [optional] 
 **css_inline** | **str**| Optional: An inline CSS style to be added to the document. | [optional] 
 **javascript_url** | **str**| Optional: Javascript URL to be added to the document. | [optional] 
 **javascript_inline** | **str**| Optional: Inline Javascript to be added to the document. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_get_language**
> HtmlGetLanguageResult edit_html_html_get_language(input_file=input_file, input_file_url=input_file_url)

Gets the language for the HTML document

Retrieves the language code (e.g. \"en\" or \"de\") of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Gets the language for the HTML document
    api_response = api_instance.edit_html_html_get_language(input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_get_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

[**HtmlGetLanguageResult**](HtmlGetLanguageResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_get_links**
> HtmlGetLinksResponse edit_html_html_get_links(input_file=input_file, input_file_url=input_file_url, base_url=base_url)

Extract resolved link URLs from HTML File

Extracts the resolved link URLs, fully-qualified if possible, from an input HTML file.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)
base_url = 'base_url_example' # str | Optional: Base URL of the page, such as https://mydomain.com (optional)

try:
    # Extract resolved link URLs from HTML File
    api_response = api_instance.edit_html_html_get_links(input_file=input_file, input_file_url=input_file_url, base_url=base_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_get_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 
 **base_url** | **str**| Optional: Base URL of the page, such as https://mydomain.com | [optional] 

### Return type

[**HtmlGetLinksResponse**](HtmlGetLinksResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_get_rel_canonical**
> HtmlGetRelCanonicalUrlResult edit_html_html_get_rel_canonical(input_file=input_file, input_file_url=input_file_url)

Gets the rel canonical URL for the HTML document

Gets the rel canonical URL of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Gets the rel canonical URL for the HTML document
    api_response = api_instance.edit_html_html_get_rel_canonical(input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_get_rel_canonical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

[**HtmlGetRelCanonicalUrlResult**](HtmlGetRelCanonicalUrlResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_get_sitemap**
> HtmlGetSitemapUrlResult edit_html_html_get_sitemap(input_file=input_file, input_file_url=input_file_url)

Gets the sitemap URL for the HTML document

Gets the sitemap link URL of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Gets the sitemap URL for the HTML document
    api_response = api_instance.edit_html_html_get_sitemap(input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_get_sitemap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

[**HtmlGetSitemapUrlResult**](HtmlGetSitemapUrlResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_set_language**
> str edit_html_html_set_language(language_code, input_file=input_file, input_file_url=input_file_url)

Sets the language for the HTML document

Sets the language code of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
language_code = 'language_code_example' # str | The HTML langauge code to set.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Sets the language for the HTML document
    api_response = api_instance.edit_html_html_set_language(language_code, input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_set_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| The HTML langauge code to set. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_set_rel_canonical**
> str edit_html_html_set_rel_canonical(canonical_url, input_file=input_file, input_file_url=input_file_url)

Sets the rel canonical URL for the HTML document

Sets the rel canonical URL of an HTML document.  This is useful for telling search engines and other indexers which pages are duplicates of eachother; any pages with the rel=canonical tag will be treated as duplicates of the canonical URL.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
canonical_url = 'canonical_url_example' # str | The HTML canonical URL to set.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Sets the rel canonical URL for the HTML document
    api_response = api_instance.edit_html_html_set_rel_canonical(canonical_url, input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_set_rel_canonical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canonical_url** | **str**| The HTML canonical URL to set. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_html_html_set_sitemap_url**
> str edit_html_html_set_sitemap_url(sitemap_url, input_file=input_file, input_file_url=input_file_url)

Sets the sitemap URL for the HTML document

Sets the sitemap URL of an HTML document.

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
api_instance = cloudmersive_convert_api_client.EditHtmlApi(cloudmersive_convert_api_client.ApiClient(configuration))
sitemap_url = 'sitemap_url_example' # str | The HTML sitemap URL to set.
input_file = '/path/to/file.txt' # file | Optional: Input file to perform the operation on. (optional)
input_file_url = 'input_file_url_example' # str | Optional: URL of a file to operate on as input. (optional)

try:
    # Sets the sitemap URL for the HTML document
    api_response = api_instance.edit_html_html_set_sitemap_url(sitemap_url, input_file=input_file, input_file_url=input_file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditHtmlApi->edit_html_html_set_sitemap_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sitemap_url** | **str**| The HTML sitemap URL to set. | 
 **input_file** | **file**| Optional: Input file to perform the operation on. | [optional] 
 **input_file_url** | **str**| Optional: URL of a file to operate on as input. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

