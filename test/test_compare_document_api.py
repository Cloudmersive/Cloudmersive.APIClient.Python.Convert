# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.api.compare_document_api import CompareDocumentApi  # noqa: E501
from cloudmersive_convert_api_client.rest import ApiException


class TestCompareDocumentApi(unittest.TestCase):
    """CompareDocumentApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_convert_api_client.api.compare_document_api.CompareDocumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_compare_document_docx(self):
        """Test case for compare_document_docx

        Compare Two Word DOCX  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()