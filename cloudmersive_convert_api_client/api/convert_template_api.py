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


class ConvertTemplateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def convert_template_apply_docx_template(self, input_file, **kwargs):  # noqa: E501
        """Apply Word DOCX template  # noqa: E501

        Apply operations to fill in a Word DOCX template by replacing target template/placeholder strings in the DOCX with values, generating a final Word DOCX result.  For example, you could create a Word Document invoice containing strings such as \"{FirstName}\" and \"{LastName}\" and then replace these values with \"John\" and \"Smith\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_template_apply_docx_template(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :param object template_definition: Template definition for the document, including what values to replace
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_template_apply_docx_template_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_template_apply_docx_template_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def convert_template_apply_docx_template_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Apply Word DOCX template  # noqa: E501

        Apply operations to fill in a Word DOCX template by replacing target template/placeholder strings in the DOCX with values, generating a final Word DOCX result.  For example, you could create a Word Document invoice containing strings such as \"{FirstName}\" and \"{LastName}\" and then replace these values with \"John\" and \"Smith\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_template_apply_docx_template_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :param object template_definition: Template definition for the document, including what values to replace
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file', 'template_definition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_template_apply_docx_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `convert_template_apply_docx_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'template_definition' in params:
            header_params['templateDefinition'] = params['template_definition']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/template/docx/apply', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_template_apply_html_template(self, value, **kwargs):  # noqa: E501
        """Apply HTML template  # noqa: E501

        Apply operations to fill in an HTML template, generating a final HTML result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_template_apply_html_template(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HtmlTemplateApplicationRequest value: Operations to apply to template (required)
        :return: HtmlTemplateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.convert_template_apply_html_template_with_http_info(value, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_template_apply_html_template_with_http_info(value, **kwargs)  # noqa: E501
            return data

    def convert_template_apply_html_template_with_http_info(self, value, **kwargs):  # noqa: E501
        """Apply HTML template  # noqa: E501

        Apply operations to fill in an HTML template, generating a final HTML result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.convert_template_apply_html_template_with_http_info(value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HtmlTemplateApplicationRequest value: Operations to apply to template (required)
        :return: HtmlTemplateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_template_apply_html_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `convert_template_apply_html_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'value' in params:
            body_params = params['value']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/template/html/apply', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HtmlTemplateApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
