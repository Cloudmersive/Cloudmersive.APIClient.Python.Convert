# cloudmersive_convert_api_client.EditPdfApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_pdf_delete_pages**](EditPdfApi.md#edit_pdf_delete_pages) | **POST** /convert/edit/pdf/pages/delete | Remove / delete pages from a PDF document
[**edit_pdf_encrypt**](EditPdfApi.md#edit_pdf_encrypt) | **POST** /convert/edit/pdf/encrypt | Encrypt and password-protect a PDF
[**edit_pdf_get_form_fields**](EditPdfApi.md#edit_pdf_get_form_fields) | **POST** /convert/edit/pdf/form/get-fields | Gets PDF Form fields and values
[**edit_pdf_get_metadata**](EditPdfApi.md#edit_pdf_get_metadata) | **POST** /convert/edit/pdf/get-metadata | Get PDF document metadata
[**edit_pdf_insert_pages**](EditPdfApi.md#edit_pdf_insert_pages) | **POST** /convert/edit/pdf/pages/insert | Insert / copy pages from one PDF document into another
[**edit_pdf_rasterize**](EditPdfApi.md#edit_pdf_rasterize) | **POST** /convert/edit/pdf/rasterize | Rasterize a PDF to an image-based PDF
[**edit_pdf_set_form_fields**](EditPdfApi.md#edit_pdf_set_form_fields) | **POST** /convert/edit/pdf/form/set-fields | Sets ands fills PDF Form field values
[**edit_pdf_set_metadata**](EditPdfApi.md#edit_pdf_set_metadata) | **POST** /convert/edit/pdf/set-metadata | Sets PDF document metadata
[**edit_pdf_set_permissions**](EditPdfApi.md#edit_pdf_set_permissions) | **POST** /convert/edit/pdf/encrypt/set-permissions | Encrypt, password-protect and set restricted permissions on a PDF
[**edit_pdf_watermark_text**](EditPdfApi.md#edit_pdf_watermark_text) | **POST** /convert/edit/pdf/watermark/text | Add a text watermark to a PDF


# **edit_pdf_delete_pages**
> str edit_pdf_delete_pages(input_file, page_start, page_end)

Remove / delete pages from a PDF document

Remove one or more pages from a PDF document

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
page_start = 56 # int | Page number (1 based) to start deleting pages from (inclusive).
page_end = 56 # int | Page number (1 based) to stop deleting pages from (inclusive).

try:
    # Remove / delete pages from a PDF document
    api_response = api_instance.edit_pdf_delete_pages(input_file, page_start, page_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_delete_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **page_start** | **int**| Page number (1 based) to start deleting pages from (inclusive). | 
 **page_end** | **int**| Page number (1 based) to stop deleting pages from (inclusive). | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_encrypt**
> str edit_pdf_encrypt(input_file, user_password=user_password, owner_password=owner_password)

Encrypt and password-protect a PDF

Encrypt a PDF document with a password.  Set an owner password to control owner (editor/creator) permissions, and set a user (reader) password to control the viewer of the PDF.  Set the password fields null to omit the given password.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
user_password = 'user_password_example' # str | Password of a user (reader) of the PDF file (optional)
owner_password = 'owner_password_example' # str | Password of a owner (creator/editor) of the PDF file (optional)

try:
    # Encrypt and password-protect a PDF
    api_response = api_instance.edit_pdf_encrypt(input_file, user_password=user_password, owner_password=owner_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **user_password** | **str**| Password of a user (reader) of the PDF file | [optional] 
 **owner_password** | **str**| Password of a owner (creator/editor) of the PDF file | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_get_form_fields**
> PdfFormFields edit_pdf_get_form_fields(input_file)

Gets PDF Form fields and values

Encrypt a PDF document with a password.  Set an owner password to control owner (editor/creator) permissions, and set a user (reader) password to control the viewer of the PDF.  Set the password fields null to omit the given password.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Gets PDF Form fields and values
    api_response = api_instance.edit_pdf_get_form_fields(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_get_form_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**PdfFormFields**](PdfFormFields.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_get_metadata**
> PdfMetadata edit_pdf_get_metadata(input_file)

Get PDF document metadata

Returns the metadata from the PDF document, including Title, Author, etc.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Get PDF document metadata
    api_response = api_instance.edit_pdf_get_metadata(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**PdfMetadata**](PdfMetadata.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_insert_pages**
> str edit_pdf_insert_pages(source_file, destination_file, page_start_source, page_end_source, page_insert_before_desitnation)

Insert / copy pages from one PDF document into another

Copy one or more pages from one PDF document (source document) and insert them into a second PDF document (destination document).

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
source_file = '/path/to/file.txt' # file | Source PDF file to copy pages from.
destination_file = '/path/to/file.txt' # file | Destination PDF file to copy pages into.
page_start_source = 56 # int | Page number (1 based) to start copying pages from (inclusive) in the Source file.
page_end_source = 56 # int | Page number (1 based) to stop copying pages pages from (inclusive) in the Source file.
page_insert_before_desitnation = 56 # int | Page number (1 based) to insert the pages before in the Destination file.

try:
    # Insert / copy pages from one PDF document into another
    api_response = api_instance.edit_pdf_insert_pages(source_file, destination_file, page_start_source, page_end_source, page_insert_before_desitnation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_insert_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_file** | **file**| Source PDF file to copy pages from. | 
 **destination_file** | **file**| Destination PDF file to copy pages into. | 
 **page_start_source** | **int**| Page number (1 based) to start copying pages from (inclusive) in the Source file. | 
 **page_end_source** | **int**| Page number (1 based) to stop copying pages pages from (inclusive) in the Source file. | 
 **page_insert_before_desitnation** | **int**| Page number (1 based) to insert the pages before in the Destination file. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_rasterize**
> str edit_pdf_rasterize(input_file)

Rasterize a PDF to an image-based PDF

Rasterize a PDF into an image-based PDF.  The output is a PDF where each page is comprised of a high-resolution image, with all text, figures and other components removed.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Rasterize a PDF to an image-based PDF
    api_response = api_instance.edit_pdf_rasterize(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_rasterize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_set_form_fields**
> str edit_pdf_set_form_fields(field_values)

Sets ands fills PDF Form field values

Fill in the form fields in a PDF form with specific values.  Use form/get-fields to enumerate the available fields and their data types in an input form.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
field_values = cloudmersive_convert_api_client.SetPdfFormFieldsRequest() # SetPdfFormFieldsRequest | 

try:
    # Sets ands fills PDF Form field values
    api_response = api_instance.edit_pdf_set_form_fields(field_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_set_form_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_values** | [**SetPdfFormFieldsRequest**](SetPdfFormFieldsRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_set_metadata**
> str edit_pdf_set_metadata(request)

Sets PDF document metadata

Sets (writes) metadata into the input PDF document, including Title, Author, etc.

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
request = cloudmersive_convert_api_client.SetPdfMetadataRequest() # SetPdfMetadataRequest | 

try:
    # Sets PDF document metadata
    api_response = api_instance.edit_pdf_set_metadata(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_set_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetPdfMetadataRequest**](SetPdfMetadataRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_set_permissions**
> str edit_pdf_set_permissions(owner_password, input_file, user_password=user_password, allow_printing=allow_printing, allow_document_assembly=allow_document_assembly, allow_content_extraction=allow_content_extraction, allow_form_filling=allow_form_filling, allow_editing=allow_editing, allow_annotations=allow_annotations, allow_degraded_printing=allow_degraded_printing)

Encrypt, password-protect and set restricted permissions on a PDF

Encrypt a PDF document with a password, and set permissions on the PDF.  Set an owner password to control owner (editor/creator) permissions [required], and set a user (reader) password to control the viewer of the PDF [optional].  Set the reader password to null to omit the password.  Restrict or allow printing, copying content, document assembly, editing (read-only), form filling, modification of annotations, and degraded printing through document Digital Rights Management (DRM).

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
owner_password = 'owner_password_example' # str | Password of a owner (creator/editor) of the PDF file (required)
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
user_password = 'user_password_example' # str | Password of a user (reader) of the PDF file (optional) (optional)
allow_printing = true # bool | Set to false to disable printing through DRM.  Default is true. (optional)
allow_document_assembly = true # bool | Set to false to disable document assembly through DRM.  Default is true. (optional)
allow_content_extraction = true # bool | Set to false to disable copying/extracting content out of the PDF through DRM.  Default is true. (optional)
allow_form_filling = true # bool | Set to false to disable filling out form fields in the PDF through DRM.  Default is true. (optional)
allow_editing = true # bool | Set to false to disable editing in the PDF through DRM (making the PDF read-only).  Default is true. (optional)
allow_annotations = true # bool | Set to false to disable annotations and editing of annotations in the PDF through DRM.  Default is true. (optional)
allow_degraded_printing = true # bool | Set to false to disable degraded printing of the PDF through DRM.  Default is true. (optional)

try:
    # Encrypt, password-protect and set restricted permissions on a PDF
    api_response = api_instance.edit_pdf_set_permissions(owner_password, input_file, user_password=user_password, allow_printing=allow_printing, allow_document_assembly=allow_document_assembly, allow_content_extraction=allow_content_extraction, allow_form_filling=allow_form_filling, allow_editing=allow_editing, allow_annotations=allow_annotations, allow_degraded_printing=allow_degraded_printing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_set_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_password** | **str**| Password of a owner (creator/editor) of the PDF file (required) | 
 **input_file** | **file**| Input file to perform the operation on. | 
 **user_password** | **str**| Password of a user (reader) of the PDF file (optional) | [optional] 
 **allow_printing** | **bool**| Set to false to disable printing through DRM.  Default is true. | [optional] 
 **allow_document_assembly** | **bool**| Set to false to disable document assembly through DRM.  Default is true. | [optional] 
 **allow_content_extraction** | **bool**| Set to false to disable copying/extracting content out of the PDF through DRM.  Default is true. | [optional] 
 **allow_form_filling** | **bool**| Set to false to disable filling out form fields in the PDF through DRM.  Default is true. | [optional] 
 **allow_editing** | **bool**| Set to false to disable editing in the PDF through DRM (making the PDF read-only).  Default is true. | [optional] 
 **allow_annotations** | **bool**| Set to false to disable annotations and editing of annotations in the PDF through DRM.  Default is true. | [optional] 
 **allow_degraded_printing** | **bool**| Set to false to disable degraded printing of the PDF through DRM.  Default is true. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pdf_watermark_text**
> str edit_pdf_watermark_text(watermark_text, input_file, font_name=font_name, font_size=font_size, font_color=font_color, font_transparency=font_transparency)

Add a text watermark to a PDF

Adds a text watermark to a PDF

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
api_instance = cloudmersive_convert_api_client.EditPdfApi(cloudmersive_convert_api_client.ApiClient(configuration))
watermark_text = 'watermark_text_example' # str | Watermark text to add to the PDF (required)
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
font_name = 'font_name_example' # str | Font Family Name for the watermark text; default is Times New Roman (optional)
font_size = 8.14 # float | Font Size in points of the text; default is 150 (optional)
font_color = 'font_color_example' # str | Font color in hexadecimal or HTML color name; default is Red (optional)
font_transparency = 8.14 # float | Font transparency between 0.0 (completely transparent) to 1.0 (fully opaque); default is 0.5 (optional)

try:
    # Add a text watermark to a PDF
    api_response = api_instance.edit_pdf_watermark_text(watermark_text, input_file, font_name=font_name, font_size=font_size, font_color=font_color, font_transparency=font_transparency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditPdfApi->edit_pdf_watermark_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watermark_text** | **str**| Watermark text to add to the PDF (required) | 
 **input_file** | **file**| Input file to perform the operation on. | 
 **font_name** | **str**| Font Family Name for the watermark text; default is Times New Roman | [optional] 
 **font_size** | **float**| Font Size in points of the text; default is 150 | [optional] 
 **font_color** | **str**| Font color in hexadecimal or HTML color name; default is Red | [optional] 
 **font_transparency** | **float**| Font transparency between 0.0 (completely transparent) to 1.0 (fully opaque); default is 0.5 | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

