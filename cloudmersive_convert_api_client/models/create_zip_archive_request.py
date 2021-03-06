# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateZipArchiveRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'files_in_zip': 'list[ZipFile]',
        'directories_in_zip': 'list[ZipDirectory]'
    }

    attribute_map = {
        'files_in_zip': 'FilesInZip',
        'directories_in_zip': 'DirectoriesInZip'
    }

    def __init__(self, files_in_zip=None, directories_in_zip=None):  # noqa: E501
        """CreateZipArchiveRequest - a model defined in Swagger"""  # noqa: E501

        self._files_in_zip = None
        self._directories_in_zip = None
        self.discriminator = None

        if files_in_zip is not None:
            self.files_in_zip = files_in_zip
        if directories_in_zip is not None:
            self.directories_in_zip = directories_in_zip

    @property
    def files_in_zip(self):
        """Gets the files_in_zip of this CreateZipArchiveRequest.  # noqa: E501

        Top-level files in the root directory fo the zip file  # noqa: E501

        :return: The files_in_zip of this CreateZipArchiveRequest.  # noqa: E501
        :rtype: list[ZipFile]
        """
        return self._files_in_zip

    @files_in_zip.setter
    def files_in_zip(self, files_in_zip):
        """Sets the files_in_zip of this CreateZipArchiveRequest.

        Top-level files in the root directory fo the zip file  # noqa: E501

        :param files_in_zip: The files_in_zip of this CreateZipArchiveRequest.  # noqa: E501
        :type: list[ZipFile]
        """

        self._files_in_zip = files_in_zip

    @property
    def directories_in_zip(self):
        """Gets the directories_in_zip of this CreateZipArchiveRequest.  # noqa: E501

        Top-level directories in the root directory of the zip; directories can contain sub-directories and files  # noqa: E501

        :return: The directories_in_zip of this CreateZipArchiveRequest.  # noqa: E501
        :rtype: list[ZipDirectory]
        """
        return self._directories_in_zip

    @directories_in_zip.setter
    def directories_in_zip(self, directories_in_zip):
        """Sets the directories_in_zip of this CreateZipArchiveRequest.

        Top-level directories in the root directory of the zip; directories can contain sub-directories and files  # noqa: E501

        :param directories_in_zip: The directories_in_zip of this CreateZipArchiveRequest.  # noqa: E501
        :type: list[ZipDirectory]
        """

        self._directories_in_zip = directories_in_zip

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateZipArchiveRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateZipArchiveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
