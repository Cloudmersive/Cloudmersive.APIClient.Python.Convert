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


class ZipEncryptionAdvancedRequest(object):
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
        'input_file_contents': 'str',
        'password': 'str',
        'encryption_algorithm': 'str'
    }

    attribute_map = {
        'input_file_contents': 'InputFileContents',
        'password': 'Password',
        'encryption_algorithm': 'EncryptionAlgorithm'
    }

    def __init__(self, input_file_contents=None, password=None, encryption_algorithm=None):  # noqa: E501
        """ZipEncryptionAdvancedRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_contents = None
        self._password = None
        self._encryption_algorithm = None
        self.discriminator = None

        if input_file_contents is not None:
            self.input_file_contents = input_file_contents
        if password is not None:
            self.password = password
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm

    @property
    def input_file_contents(self):
        """Gets the input_file_contents of this ZipEncryptionAdvancedRequest.  # noqa: E501

        Input Zip File archive contents in bytes  # noqa: E501

        :return: The input_file_contents of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_contents

    @input_file_contents.setter
    def input_file_contents(self, input_file_contents):
        """Sets the input_file_contents of this ZipEncryptionAdvancedRequest.

        Input Zip File archive contents in bytes  # noqa: E501

        :param input_file_contents: The input_file_contents of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :type: str
        """
        if input_file_contents is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_contents):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_contents`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_contents = input_file_contents

    @property
    def password(self):
        """Gets the password of this ZipEncryptionAdvancedRequest.  # noqa: E501

        Password to place on the Zip file; the longer the password, the more secure  # noqa: E501

        :return: The password of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ZipEncryptionAdvancedRequest.

        Password to place on the Zip file; the longer the password, the more secure  # noqa: E501

        :param password: The password of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this ZipEncryptionAdvancedRequest.  # noqa: E501

        Encryption algorithm to use; possible values are AES-256 (recommended), AES-128, and PK-Zip (not recommended; legacy, weak encryption algorithm).  Default is AES-256.  # noqa: E501

        :return: The encryption_algorithm of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this ZipEncryptionAdvancedRequest.

        Encryption algorithm to use; possible values are AES-256 (recommended), AES-128, and PK-Zip (not recommended; legacy, weak encryption algorithm).  Default is AES-256.  # noqa: E501

        :param encryption_algorithm: The encryption_algorithm of this ZipEncryptionAdvancedRequest.  # noqa: E501
        :type: str
        """

        self._encryption_algorithm = encryption_algorithm

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
        if issubclass(ZipEncryptionAdvancedRequest, dict):
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
        if not isinstance(other, ZipEncryptionAdvancedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
