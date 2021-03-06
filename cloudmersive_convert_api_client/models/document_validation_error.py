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


class DocumentValidationError(object):
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
        'description': 'str',
        'path': 'str',
        'uri': 'str',
        'is_error': 'bool'
    }

    attribute_map = {
        'description': 'Description',
        'path': 'Path',
        'uri': 'Uri',
        'is_error': 'IsError'
    }

    def __init__(self, description=None, path=None, uri=None, is_error=None):  # noqa: E501
        """DocumentValidationError - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._path = None
        self._uri = None
        self._is_error = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if path is not None:
            self.path = path
        if uri is not None:
            self.uri = uri
        if is_error is not None:
            self.is_error = is_error

    @property
    def description(self):
        """Gets the description of this DocumentValidationError.  # noqa: E501

        Description of the error  # noqa: E501

        :return: The description of this DocumentValidationError.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentValidationError.

        Description of the error  # noqa: E501

        :param description: The description of this DocumentValidationError.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """Gets the path of this DocumentValidationError.  # noqa: E501

        XPath to the error  # noqa: E501

        :return: The path of this DocumentValidationError.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DocumentValidationError.

        XPath to the error  # noqa: E501

        :param path: The path of this DocumentValidationError.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def uri(self):
        """Gets the uri of this DocumentValidationError.  # noqa: E501

        URI of the part in question  # noqa: E501

        :return: The uri of this DocumentValidationError.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DocumentValidationError.

        URI of the part in question  # noqa: E501

        :param uri: The uri of this DocumentValidationError.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def is_error(self):
        """Gets the is_error of this DocumentValidationError.  # noqa: E501

        True if this is an error, false otherwise  # noqa: E501

        :return: The is_error of this DocumentValidationError.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this DocumentValidationError.

        True if this is an error, false otherwise  # noqa: E501

        :param is_error: The is_error of this DocumentValidationError.  # noqa: E501
        :type: bool
        """

        self._is_error = is_error

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
        if issubclass(DocumentValidationError, dict):
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
        if not isinstance(other, DocumentValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
