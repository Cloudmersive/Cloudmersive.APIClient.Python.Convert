# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_convert_api_client.api_client import ApiClient


class ConvertDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def convert_data_csv_to_json(self, input_file, **kwargs):  # noqa: E501
        """Convert CSV to JSON conversion  # noqa: E501

        Convert a CSV file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_csv_to_json(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_data_csv_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_data_csv_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def convert_data_csv_to_json_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Convert CSV to JSON conversion  # noqa: E501

        Convert a CSV file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_csv_to_json_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_data_csv_to_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `convert_data_csv_to_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/csv/to/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_data_xls_to_json(self, input_file, **kwargs):  # noqa: E501
        """Convert Excel (97-2003) XLS to JSON conversion  # noqa: E501

        Convert an Excel (97-2003) XLS file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xls_to_json(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_data_xls_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_data_xls_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def convert_data_xls_to_json_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Convert Excel (97-2003) XLS to JSON conversion  # noqa: E501

        Convert an Excel (97-2003) XLS file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xls_to_json_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_data_xls_to_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `convert_data_xls_to_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/xls/to/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_data_xlsx_to_json(self, input_file, **kwargs):  # noqa: E501
        """Convert Excel XLSX to JSON conversion  # noqa: E501

        Convert an Excel XLSX file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xlsx_to_json(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_data_xlsx_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_data_xlsx_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def convert_data_xlsx_to_json_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Convert Excel XLSX to JSON conversion  # noqa: E501

        Convert an Excel XLSX file to a JSON object array  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xlsx_to_json_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_data_xlsx_to_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `convert_data_xlsx_to_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/xlsx/to/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_data_xml_to_json(self, input_file, **kwargs):  # noqa: E501
        """Convert XML to JSON conversion  # noqa: E501

        Convert an XML string or file into JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xml_to_json(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_data_xml_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_data_xml_to_json_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def convert_data_xml_to_json_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Convert XML to JSON conversion  # noqa: E501

        Convert an XML string or file into JSON  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_data_xml_to_json_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_data_xml_to_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `convert_data_xml_to_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/xml/to/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
