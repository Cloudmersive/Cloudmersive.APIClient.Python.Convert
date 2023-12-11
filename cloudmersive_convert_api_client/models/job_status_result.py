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


class JobStatusResult(object):
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
        'async_job_status': 'str',
        'async_job_id': 'str',
        'pptx_result': 'SplitPptxPresentationResult',
        'error_message': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'async_job_status': 'AsyncJobStatus',
        'async_job_id': 'AsyncJobID',
        'pptx_result': 'PptxResult',
        'error_message': 'ErrorMessage'
    }

    def __init__(self, successful=None, async_job_status=None, async_job_id=None, pptx_result=None, error_message=None):  # noqa: E501
        """JobStatusResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._async_job_status = None
        self._async_job_id = None
        self._pptx_result = None
        self._error_message = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if async_job_status is not None:
            self.async_job_status = async_job_status
        if async_job_id is not None:
            self.async_job_id = async_job_id
        if pptx_result is not None:
            self.pptx_result = pptx_result
        if error_message is not None:
            self.error_message = error_message

    @property
    def successful(self):
        """Gets the successful of this JobStatusResult.  # noqa: E501

        True if the operation to check the status of the job was successful, false otherwise  # noqa: E501

        :return: The successful of this JobStatusResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this JobStatusResult.

        True if the operation to check the status of the job was successful, false otherwise  # noqa: E501

        :param successful: The successful of this JobStatusResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def async_job_status(self):
        """Gets the async_job_status of this JobStatusResult.  # noqa: E501

        Returns the job status of the Async Job, if applicable.  Possible states are STARTED and COMPLETED  # noqa: E501

        :return: The async_job_status of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._async_job_status

    @async_job_status.setter
    def async_job_status(self, async_job_status):
        """Sets the async_job_status of this JobStatusResult.

        Returns the job status of the Async Job, if applicable.  Possible states are STARTED and COMPLETED  # noqa: E501

        :param async_job_status: The async_job_status of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._async_job_status = async_job_status

    @property
    def async_job_id(self):
        """Gets the async_job_id of this JobStatusResult.  # noqa: E501

        When the job exceeds 25 pages, an Async Job ID is returned.  Use the CheckPdfOcrJobStatus API to check on the status of this job using the AsyncJobID and get the result when it finishes  # noqa: E501

        :return: The async_job_id of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        """Sets the async_job_id of this JobStatusResult.

        When the job exceeds 25 pages, an Async Job ID is returned.  Use the CheckPdfOcrJobStatus API to check on the status of this job using the AsyncJobID and get the result when it finishes  # noqa: E501

        :param async_job_id: The async_job_id of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._async_job_id = async_job_id

    @property
    def pptx_result(self):
        """Gets the pptx_result of this JobStatusResult.  # noqa: E501

        PowerPoint split result (if applicable)  # noqa: E501

        :return: The pptx_result of this JobStatusResult.  # noqa: E501
        :rtype: SplitPptxPresentationResult
        """
        return self._pptx_result

    @pptx_result.setter
    def pptx_result(self, pptx_result):
        """Sets the pptx_result of this JobStatusResult.

        PowerPoint split result (if applicable)  # noqa: E501

        :param pptx_result: The pptx_result of this JobStatusResult.  # noqa: E501
        :type: SplitPptxPresentationResult
        """

        self._pptx_result = pptx_result

    @property
    def error_message(self):
        """Gets the error_message of this JobStatusResult.  # noqa: E501

        Error message (if any)  # noqa: E501

        :return: The error_message of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this JobStatusResult.

        Error message (if any)  # noqa: E501

        :param error_message: The error_message of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(JobStatusResult, dict):
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
        if not isinstance(other, JobStatusResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
