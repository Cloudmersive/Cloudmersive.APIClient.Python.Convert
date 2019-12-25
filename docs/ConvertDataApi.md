# cloudmersive_convert_api_client.ConvertDataApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_data_csv_to_json**](ConvertDataApi.md#convert_data_csv_to_json) | **POST** /convert/csv/to/json | Convert CSV to JSON conversion
[**convert_data_json_to_xml**](ConvertDataApi.md#convert_data_json_to_xml) | **POST** /convert/json/to/xml | Convert JSON to XML conversion
[**convert_data_xls_to_json**](ConvertDataApi.md#convert_data_xls_to_json) | **POST** /convert/xls/to/json | Convert Excel (97-2003) XLS to JSON conversion
[**convert_data_xlsx_to_json**](ConvertDataApi.md#convert_data_xlsx_to_json) | **POST** /convert/xlsx/to/json | Convert Excel XLSX to JSON conversion
[**convert_data_xml_edit_add_attribute_with_x_path**](ConvertDataApi.md#convert_data_xml_edit_add_attribute_with_x_path) | **POST** /convert/xml/edit/xpath/add-attribute | Adds an attribute to all XML nodes matching XPath expression
[**convert_data_xml_edit_add_child_with_x_path**](ConvertDataApi.md#convert_data_xml_edit_add_child_with_x_path) | **POST** /convert/xml/edit/xpath/add-child | Adds an XML node as a child to XML nodes matching XPath expression
[**convert_data_xml_edit_remove_all_child_nodes_with_x_path**](ConvertDataApi.md#convert_data_xml_edit_remove_all_child_nodes_with_x_path) | **POST** /convert/xml/edit/xpath/remove-all-children | Removes, deletes all children of nodes matching XPath expression, but does not remove the nodes
[**convert_data_xml_edit_replace_with_x_path**](ConvertDataApi.md#convert_data_xml_edit_replace_with_x_path) | **POST** /convert/xml/edit/xpath/replace | Replaces XML nodes matching XPath expression with new node
[**convert_data_xml_edit_set_value_with_x_path**](ConvertDataApi.md#convert_data_xml_edit_set_value_with_x_path) | **POST** /convert/xml/edit/xpath/set-value | Sets the value contents of XML nodes matching XPath expression
[**convert_data_xml_filter_with_x_path**](ConvertDataApi.md#convert_data_xml_filter_with_x_path) | **POST** /convert/xml/select/xpath | Filter, select XML nodes using XPath expression, get results
[**convert_data_xml_remove_with_x_path**](ConvertDataApi.md#convert_data_xml_remove_with_x_path) | **POST** /convert/xml/edit/xpath/remove | Remove, delete XML nodes and items matching XPath expression
[**convert_data_xml_to_json**](ConvertDataApi.md#convert_data_xml_to_json) | **POST** /convert/xml/to/json | Convert XML to JSON conversion
[**convert_data_xml_transform_with_xslt_to_xml**](ConvertDataApi.md#convert_data_xml_transform_with_xslt_to_xml) | **POST** /convert/xml/transform/xslt/to/xml | Transform XML document file with XSLT into a new XML document


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
> str convert_data_json_to_xml(json_object)

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

**str**

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

# **convert_data_xml_edit_add_attribute_with_x_path**
> XmlAddAttributeWithXPathResult convert_data_xml_edit_add_attribute_with_x_path(input_file, x_path_expression, xml_attribute_name, xml_attribute_value)

Adds an attribute to all XML nodes matching XPath expression

Return the reuslts of editing an XML document by adding an attribute to all of the nodes that match an input XPath expression.

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
xml_attribute_name = 'xml_attribute_name_example' # str | Name of the XML attribute to add
xml_attribute_value = 'xml_attribute_value_example' # str | Value of the XML attribute to add

try:
    # Adds an attribute to all XML nodes matching XPath expression
    api_response = api_instance.convert_data_xml_edit_add_attribute_with_x_path(input_file, x_path_expression, xml_attribute_name, xml_attribute_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_edit_add_attribute_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **xml_attribute_name** | **str**| Name of the XML attribute to add | 
 **xml_attribute_value** | **str**| Value of the XML attribute to add | 

### Return type

[**XmlAddAttributeWithXPathResult**](XmlAddAttributeWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_edit_add_child_with_x_path**
> XmlAddChildWithXPathResult convert_data_xml_edit_add_child_with_x_path(input_file, x_path_expression, xml_node_to_add)

Adds an XML node as a child to XML nodes matching XPath expression

Return the reuslts of editing an XML document by adding an XML node as a child to all of the nodes that match an input XPath expression.

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
xml_node_to_add = 'xml_node_to_add_example' # str | XML Node to add as a child

try:
    # Adds an XML node as a child to XML nodes matching XPath expression
    api_response = api_instance.convert_data_xml_edit_add_child_with_x_path(input_file, x_path_expression, xml_node_to_add)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_edit_add_child_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **xml_node_to_add** | **str**| XML Node to add as a child | 

### Return type

[**XmlAddChildWithXPathResult**](XmlAddChildWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_edit_remove_all_child_nodes_with_x_path**
> XmlRemoveAllChildrenWithXPathResult convert_data_xml_edit_remove_all_child_nodes_with_x_path(input_file, x_path_expression)

Removes, deletes all children of nodes matching XPath expression, but does not remove the nodes

Return the reuslts of editing an XML document by removing all child nodes of the nodes that match an input XPath expression.

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression

try:
    # Removes, deletes all children of nodes matching XPath expression, but does not remove the nodes
    api_response = api_instance.convert_data_xml_edit_remove_all_child_nodes_with_x_path(input_file, x_path_expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_edit_remove_all_child_nodes_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **x_path_expression** | **str**| Valid XML XPath query expression | 

### Return type

[**XmlRemoveAllChildrenWithXPathResult**](XmlRemoveAllChildrenWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_edit_replace_with_x_path**
> XmlReplaceWithXPathResult convert_data_xml_edit_replace_with_x_path(input_file, x_path_expression, xml_node_replacement)

Replaces XML nodes matching XPath expression with new node

Return the reuslts of editing an XML document by replacing all of the nodes that match an input XPath expression with a new XML node expression.

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
xml_node_replacement = 'xml_node_replacement_example' # str | XML Node replacement content

try:
    # Replaces XML nodes matching XPath expression with new node
    api_response = api_instance.convert_data_xml_edit_replace_with_x_path(input_file, x_path_expression, xml_node_replacement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_edit_replace_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **xml_node_replacement** | **str**| XML Node replacement content | 

### Return type

[**XmlReplaceWithXPathResult**](XmlReplaceWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_edit_set_value_with_x_path**
> XmlSetValueWithXPathResult convert_data_xml_edit_set_value_with_x_path(input_file, x_path_expression, xml_value)

Sets the value contents of XML nodes matching XPath expression

Return the reuslts of editing an XML document by setting the contents of all of the nodes that match an input XPath expression.  Supports elements and attributes.

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
xml_value = 'xml_value_example' # str | XML Value to set into the matching XML nodes

try:
    # Sets the value contents of XML nodes matching XPath expression
    api_response = api_instance.convert_data_xml_edit_set_value_with_x_path(input_file, x_path_expression, xml_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_edit_set_value_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **xml_value** | **str**| XML Value to set into the matching XML nodes | 

### Return type

[**XmlSetValueWithXPathResult**](XmlSetValueWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_filter_with_x_path**
> XmlFIlterWithXPathResult convert_data_xml_filter_with_x_path(x_path_expression, input_file)

Filter, select XML nodes using XPath expression, get results

Return the reuslts of filtering, selecting an XML document with an XPath expression

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
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Filter, select XML nodes using XPath expression, get results
    api_response = api_instance.convert_data_xml_filter_with_x_path(x_path_expression, input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_filter_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**XmlFIlterWithXPathResult**](XmlFIlterWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_data_xml_remove_with_x_path**
> XmlRemoveWithXPathResult convert_data_xml_remove_with_x_path(x_path_expression, input_file)

Remove, delete XML nodes and items matching XPath expression

Return the reuslts of editing an XML document by removing all of the nodes that match an input XPath expression

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
x_path_expression = 'x_path_expression_example' # str | Valid XML XPath query expression
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Remove, delete XML nodes and items matching XPath expression
    api_response = api_instance.convert_data_xml_remove_with_x_path(x_path_expression, input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_remove_with_x_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_path_expression** | **str**| Valid XML XPath query expression | 
 **input_file** | **file**| Input file to perform the operation on. | 

### Return type

[**XmlRemoveWithXPathResult**](XmlRemoveWithXPathResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

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

# **convert_data_xml_transform_with_xslt_to_xml**
> str convert_data_xml_transform_with_xslt_to_xml(input_file, transform_file)

Transform XML document file with XSLT into a new XML document

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
input_file = '/path/to/file.txt' # file | Input XML file to perform the operation on.
transform_file = '/path/to/file.txt' # file | Input XSLT file to use to transform the input XML file.

try:
    # Transform XML document file with XSLT into a new XML document
    api_response = api_instance.convert_data_xml_transform_with_xslt_to_xml(input_file, transform_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_xml_transform_with_xslt_to_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input XML file to perform the operation on. | 
 **transform_file** | **file**| Input XSLT file to use to transform the input XML file. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

