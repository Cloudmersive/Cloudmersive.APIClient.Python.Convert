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


class DocumentArrayInput(object):
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
        'documents': 'list[DocumentItem]'
    }

    attribute_map = {
        'documents': 'Documents'
    }

    def __init__(self, documents=None):  # noqa: E501
        """DocumentArrayInput - a model defined in Swagger"""  # noqa: E501

        self._documents = None
        self.discriminator = None

        if documents is not None:
            self.documents = documents

    @property
    def documents(self):
        """Gets the documents of this DocumentArrayInput.  # noqa: E501

        Array of document objects  # noqa: E501

        :return: The documents of this DocumentArrayInput.  # noqa: E501
        :rtype: list[DocumentItem]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this DocumentArrayInput.

        Array of document objects  # noqa: E501

        :param documents: The documents of this DocumentArrayInput.  # noqa: E501
        :type: list[DocumentItem]
        """

        self._documents = documents

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
        if issubclass(DocumentArrayInput, dict):
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
        if not isinstance(other, DocumentArrayInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
