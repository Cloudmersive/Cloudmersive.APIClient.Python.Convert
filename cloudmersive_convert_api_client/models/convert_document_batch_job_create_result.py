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


class ConvertDocumentBatchJobCreateResult(object):
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
        'successful': 'bool',
        'async_job_id': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'async_job_id': 'AsyncJobID'
    }

    def __init__(self, successful=None, async_job_id=None):  # noqa: E501
        """ConvertDocumentBatchJobCreateResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._async_job_id = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if async_job_id is not None:
            self.async_job_id = async_job_id

    @property
    def successful(self):
        """Gets the successful of this ConvertDocumentBatchJobCreateResult.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this ConvertDocumentBatchJobCreateResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ConvertDocumentBatchJobCreateResult.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this ConvertDocumentBatchJobCreateResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def async_job_id(self):
        """Gets the async_job_id of this ConvertDocumentBatchJobCreateResult.  # noqa: E501

        When creating a job, an Async Job ID is returned.  Use the GetAsyncJobStatus API to check on the status of this job using the AsyncJobID and get the result when it finishes  # noqa: E501

        :return: The async_job_id of this ConvertDocumentBatchJobCreateResult.  # noqa: E501
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        """Sets the async_job_id of this ConvertDocumentBatchJobCreateResult.

        When creating a job, an Async Job ID is returned.  Use the GetAsyncJobStatus API to check on the status of this job using the AsyncJobID and get the result when it finishes  # noqa: E501

        :param async_job_id: The async_job_id of this ConvertDocumentBatchJobCreateResult.  # noqa: E501
        :type: str
        """

        self._async_job_id = async_job_id

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
        if issubclass(ConvertDocumentBatchJobCreateResult, dict):
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
        if not isinstance(other, ConvertDocumentBatchJobCreateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
