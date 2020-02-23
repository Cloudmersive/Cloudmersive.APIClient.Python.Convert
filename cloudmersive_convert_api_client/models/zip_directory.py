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

from cloudmersive_convert_api_client.models.zip_directory import ZipDirectory  # noqa: F401,E501
from cloudmersive_convert_api_client.models.zip_file import ZipFile  # noqa: F401,E501


class ZipDirectory(object):
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
        'directory_name': 'str',
        'directories_in_directory': 'list[ZipDirectory]',
        'files_in_directory': 'list[ZipFile]'
    }

    attribute_map = {
        'directory_name': 'DirectoryName',
        'directories_in_directory': 'DirectoriesInDirectory',
        'files_in_directory': 'FilesInDirectory'
    }

    def __init__(self, directory_name=None, directories_in_directory=None, files_in_directory=None):  # noqa: E501
        """ZipDirectory - a model defined in Swagger"""  # noqa: E501

        self._directory_name = None
        self._directories_in_directory = None
        self._files_in_directory = None
        self.discriminator = None

        if directory_name is not None:
            self.directory_name = directory_name
        if directories_in_directory is not None:
            self.directories_in_directory = directories_in_directory
        if files_in_directory is not None:
            self.files_in_directory = files_in_directory

    @property
    def directory_name(self):
        """Gets the directory_name of this ZipDirectory.  # noqa: E501

        Name of this directory  # noqa: E501

        :return: The directory_name of this ZipDirectory.  # noqa: E501
        :rtype: str
        """
        return self._directory_name

    @directory_name.setter
    def directory_name(self, directory_name):
        """Sets the directory_name of this ZipDirectory.

        Name of this directory  # noqa: E501

        :param directory_name: The directory_name of this ZipDirectory.  # noqa: E501
        :type: str
        """

        self._directory_name = directory_name

    @property
    def directories_in_directory(self):
        """Gets the directories_in_directory of this ZipDirectory.  # noqa: E501

        Child directories contained directly in this directory  # noqa: E501

        :return: The directories_in_directory of this ZipDirectory.  # noqa: E501
        :rtype: list[ZipDirectory]
        """
        return self._directories_in_directory

    @directories_in_directory.setter
    def directories_in_directory(self, directories_in_directory):
        """Sets the directories_in_directory of this ZipDirectory.

        Child directories contained directly in this directory  # noqa: E501

        :param directories_in_directory: The directories_in_directory of this ZipDirectory.  # noqa: E501
        :type: list[ZipDirectory]
        """

        self._directories_in_directory = directories_in_directory

    @property
    def files_in_directory(self):
        """Gets the files_in_directory of this ZipDirectory.  # noqa: E501

        Child files contained directly in this directory  # noqa: E501

        :return: The files_in_directory of this ZipDirectory.  # noqa: E501
        :rtype: list[ZipFile]
        """
        return self._files_in_directory

    @files_in_directory.setter
    def files_in_directory(self, files_in_directory):
        """Sets the files_in_directory of this ZipDirectory.

        Child files contained directly in this directory  # noqa: E501

        :param files_in_directory: The files_in_directory of this ZipDirectory.  # noqa: E501
        :type: list[ZipFile]
        """

        self._files_in_directory = files_in_directory

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
        if issubclass(ZipDirectory, dict):
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
        if not isinstance(other, ZipDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other