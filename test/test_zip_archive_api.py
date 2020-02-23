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
from cloudmersive_convert_api_client.api.zip_archive_api import ZipArchiveApi  # noqa: E501
from cloudmersive_convert_api_client.rest import ApiException


class TestZipArchiveApi(unittest.TestCase):
    """ZipArchiveApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_convert_api_client.api.zip_archive_api.ZipArchiveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_zip_archive_zip_create(self):
        """Test case for zip_archive_zip_create

        Compress files to create a new zip archive  # noqa: E501
        """
        pass

    def test_zip_archive_zip_create_advanced(self):
        """Test case for zip_archive_zip_create_advanced

        Compress files and folders to create a new zip archive with advanced options  # noqa: E501
        """
        pass

    def test_zip_archive_zip_extract(self):
        """Test case for zip_archive_zip_extract

        Extract, decompress files and folders from a zip archive  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()