# cloudmersive_convert_api_client
Convert API lets you effortlessly convert file formats and types.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.1.4
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_convert_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_convert_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
cloudmersive_convert_api_client.configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# cloudmersive_convert_api_client.configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDataApi()
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # CSV to JSON conversion
    api_response = api_instance.convert_data_csv_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_csv_to_json: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConvertDataApi* | [**convert_data_csv_to_json**](docs/ConvertDataApi.md#convert_data_csv_to_json) | **POST** /convert/csv/to/json | CSV to JSON conversion
*ConvertDataApi* | [**convert_data_xml_to_json**](docs/ConvertDataApi.md#convert_data_xml_to_json) | **POST** /convert/xml/to/json | XML to JSON conversion
*ConvertDocumentApi* | [**convert_document_autodetect_to_pdf**](docs/ConvertDocumentApi.md#convert_document_autodetect_to_pdf) | **POST** /convert/autodetect/to/pdf | Convert Document to PDF
*ConvertDocumentApi* | [**convert_document_docx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_docx_to_pdf) | **POST** /convert/docx/to/pdf | Word DOCX to PDF
*ConvertDocumentApi* | [**convert_document_pptx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_pptx_to_pdf) | **POST** /convert/pptx/to/pdf | PowerPoint PPTX to PDF
*ConvertDocumentApi* | [**convert_document_xlsx_to_csv**](docs/ConvertDocumentApi.md#convert_document_xlsx_to_csv) | **POST** /convert/xlsx/to/csv | Excel XLSX to CSV
*ConvertDocumentApi* | [**convert_document_xlsx_to_pdf**](docs/ConvertDocumentApi.md#convert_document_xlsx_to_pdf) | **POST** /convert/xlsx/to/pdf | Excel XLSX to PDF
*ConvertImageApi* | [**convert_image_image_format_convert**](docs/ConvertImageApi.md#convert_image_image_format_convert) | **POST** /convert/image/{format1}/to/{format2} | Image format conversion
*ConvertTemplateApi* | [**convert_template_apply_html_template**](docs/ConvertTemplateApi.md#convert_template_apply_html_template) | **POST** /convert/template/html/apply | Apply HTML template
*ConvertWebApi* | [**convert_web_html_to_pdf**](docs/ConvertWebApi.md#convert_web_html_to_pdf) | **POST** /convert/web/html/to/pdf | Convert HTML string to PDF
*ConvertWebApi* | [**convert_web_url_to_pdf**](docs/ConvertWebApi.md#convert_web_url_to_pdf) | **POST** /convert/web/url/to/pdf | Convert a URL to PDF
*ConvertWebApi* | [**convert_web_url_to_screenshot**](docs/ConvertWebApi.md#convert_web_url_to_screenshot) | **POST** /convert/web/url/to/screenshot | Take screenshot of URL


## Documentation For Models

 - [HtmlTemplateApplicationRequest](docs/HtmlTemplateApplicationRequest.md)
 - [HtmlTemplateApplicationResponse](docs/HtmlTemplateApplicationResponse.md)
 - [HtmlTemplateOperation](docs/HtmlTemplateOperation.md)
 - [HtmlToPdfRequest](docs/HtmlToPdfRequest.md)
 - [ScreenshotRequest](docs/ScreenshotRequest.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



