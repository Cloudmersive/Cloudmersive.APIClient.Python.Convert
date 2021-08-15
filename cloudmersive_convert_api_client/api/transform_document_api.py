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


class TransformDocumentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transform_document_docx_replace(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in Word DOCX document, return result  # noqa: E501

        Replace all instances of a string in an Office Word Document (docx)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_replace(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transform_document_docx_replace_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
        else:
            (data) = self.transform_document_docx_replace_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
            return data

    def transform_document_docx_replace_with_http_info(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in Word DOCX document, return result  # noqa: E501

        Replace all instances of a string in an Office Word Document (docx)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_replace_with_http_info(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_string', 'replace_string', 'input_file', 'input_file_url', 'match_case']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transform_document_docx_replace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_string' is set
        if ('match_string' not in params or
                params['match_string'] is None):
            raise ValueError("Missing the required parameter `match_string` when calling `transform_document_docx_replace`")  # noqa: E501
        # verify the required parameter 'replace_string' is set
        if ('replace_string' not in params or
                params['replace_string'] is None):
            raise ValueError("Missing the required parameter `replace_string` when calling `transform_document_docx_replace`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'input_file_url' in params:
            header_params['inputFileUrl'] = params['input_file_url']  # noqa: E501
        if 'match_string' in params:
            header_params['matchString'] = params['match_string']  # noqa: E501
        if 'replace_string' in params:
            header_params['replaceString'] = params['replace_string']  # noqa: E501
        if 'match_case' in params:
            header_params['matchCase'] = params['match_case']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/transform/docx/replace-all', 'POST',
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

    def transform_document_docx_replace_edit_session(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in Word DOCX document, return edit session  # noqa: E501

        Replace all instances of a string in an Office Word Document (docx).  Returns an edit session URL so that you can chain together multiple edit operations without having to send the entire document contents back and forth multiple times.  Call the Finish Editing API to retrieve the final document once editing is complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_replace_edit_session(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: DocumentTransformEditSession
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transform_document_docx_replace_edit_session_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
        else:
            (data) = self.transform_document_docx_replace_edit_session_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
            return data

    def transform_document_docx_replace_edit_session_with_http_info(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in Word DOCX document, return edit session  # noqa: E501

        Replace all instances of a string in an Office Word Document (docx).  Returns an edit session URL so that you can chain together multiple edit operations without having to send the entire document contents back and forth multiple times.  Call the Finish Editing API to retrieve the final document once editing is complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_replace_edit_session_with_http_info(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: DocumentTransformEditSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_string', 'replace_string', 'input_file', 'input_file_url', 'match_case']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transform_document_docx_replace_edit_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_string' is set
        if ('match_string' not in params or
                params['match_string'] is None):
            raise ValueError("Missing the required parameter `match_string` when calling `transform_document_docx_replace_edit_session`")  # noqa: E501
        # verify the required parameter 'replace_string' is set
        if ('replace_string' not in params or
                params['replace_string'] is None):
            raise ValueError("Missing the required parameter `replace_string` when calling `transform_document_docx_replace_edit_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'input_file_url' in params:
            header_params['inputFileUrl'] = params['input_file_url']  # noqa: E501
        if 'match_string' in params:
            header_params['matchString'] = params['match_string']  # noqa: E501
        if 'replace_string' in params:
            header_params['replaceString'] = params['replace_string']  # noqa: E501
        if 'match_case' in params:
            header_params['matchCase'] = params['match_case']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/transform/docx/replace-all/edit-session', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentTransformEditSession',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transform_document_docx_table_fill_in(self, request, **kwargs):  # noqa: E501
        """Fill in data in a table in a Word DOCX document, return result  # noqa: E501

        Replace placeholder rows ina  table in an Office Word Document (docx) using one or more templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_table_fill_in(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DocxTableTableFillRequest request: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transform_document_docx_table_fill_in_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.transform_document_docx_table_fill_in_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def transform_document_docx_table_fill_in_with_http_info(self, request, **kwargs):  # noqa: E501
        """Fill in data in a table in a Word DOCX document, return result  # noqa: E501

        Replace placeholder rows ina  table in an Office Word Document (docx) using one or more templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_table_fill_in_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DocxTableTableFillRequest request: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transform_document_docx_table_fill_in" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `transform_document_docx_table_fill_in`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/transform/docx/table/fill/data', 'POST',
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

    def transform_document_docx_table_fill_in_edit_session(self, request, **kwargs):  # noqa: E501
        """Fill in data in a table in a Word DOCX document, return edit session  # noqa: E501

        Replace placeholder rows ina  table in an Office Word Document (docx) using one or more templates.  Returns an edit session URL so that you can chain together multiple edit operations without having to send the entire document contents back and forth multiple times.  Call the Finish Editing API to retrieve the final document once editing is complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_table_fill_in_edit_session(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DocxTableTableFillRequest request: (required)
        :return: DocumentTransformEditSession
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transform_document_docx_table_fill_in_edit_session_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.transform_document_docx_table_fill_in_edit_session_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def transform_document_docx_table_fill_in_edit_session_with_http_info(self, request, **kwargs):  # noqa: E501
        """Fill in data in a table in a Word DOCX document, return edit session  # noqa: E501

        Replace placeholder rows ina  table in an Office Word Document (docx) using one or more templates.  Returns an edit session URL so that you can chain together multiple edit operations without having to send the entire document contents back and forth multiple times.  Call the Finish Editing API to retrieve the final document once editing is complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_docx_table_fill_in_edit_session_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DocxTableTableFillRequest request: (required)
        :return: DocumentTransformEditSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transform_document_docx_table_fill_in_edit_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `transform_document_docx_table_fill_in_edit_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/transform/docx/table/fill/data/edit-session', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentTransformEditSession',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transform_document_pptx_replace(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in PowerPoint PPTX presentation, return result  # noqa: E501

        Replace all instances of a string in an Office PowerPoint Document (pptx)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_pptx_replace(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transform_document_pptx_replace_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
        else:
            (data) = self.transform_document_pptx_replace_with_http_info(match_string, replace_string, **kwargs)  # noqa: E501
            return data

    def transform_document_pptx_replace_with_http_info(self, match_string, replace_string, **kwargs):  # noqa: E501
        """Replace string in PowerPoint PPTX presentation, return result  # noqa: E501

        Replace all instances of a string in an Office PowerPoint Document (pptx)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transform_document_pptx_replace_with_http_info(match_string, replace_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_string: String to search for and match against, to be replaced (required)
        :param str replace_string: String to replace the matched values with (required)
        :param file input_file: Optional: Input file to perform the operation on.
        :param str input_file_url: Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API (part of EditDocumentApi) to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).
        :param bool match_case: Optional: True if the case should be matched, false for case insensitive match. Default is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_string', 'replace_string', 'input_file', 'input_file_url', 'match_case']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transform_document_pptx_replace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_string' is set
        if ('match_string' not in params or
                params['match_string'] is None):
            raise ValueError("Missing the required parameter `match_string` when calling `transform_document_pptx_replace`")  # noqa: E501
        # verify the required parameter 'replace_string' is set
        if ('replace_string' not in params or
                params['replace_string'] is None):
            raise ValueError("Missing the required parameter `replace_string` when calling `transform_document_pptx_replace`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'input_file_url' in params:
            header_params['inputFileUrl'] = params['input_file_url']  # noqa: E501
        if 'match_string' in params:
            header_params['matchString'] = params['match_string']  # noqa: E501
        if 'replace_string' in params:
            header_params['replaceString'] = params['replace_string']  # noqa: E501
        if 'match_case' in params:
            header_params['matchCase'] = params['match_case']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/convert/transform/pptx/replace-all', 'POST',
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
