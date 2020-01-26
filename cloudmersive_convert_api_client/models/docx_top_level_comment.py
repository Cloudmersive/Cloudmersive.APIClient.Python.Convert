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

from cloudmersive_convert_api_client.models.docx_comment import DocxComment  # noqa: F401,E501


class DocxTopLevelComment(object):
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
        'path': 'str',
        'author': 'str',
        'author_initials': 'str',
        'comment_text': 'str',
        'comment_date': 'datetime',
        'reply_child_comments': 'list[DocxComment]',
        'done': 'bool'
    }

    attribute_map = {
        'path': 'Path',
        'author': 'Author',
        'author_initials': 'AuthorInitials',
        'comment_text': 'CommentText',
        'comment_date': 'CommentDate',
        'reply_child_comments': 'ReplyChildComments',
        'done': 'Done'
    }

    def __init__(self, path=None, author=None, author_initials=None, comment_text=None, comment_date=None, reply_child_comments=None, done=None):  # noqa: E501
        """DocxTopLevelComment - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._author = None
        self._author_initials = None
        self._comment_text = None
        self._comment_date = None
        self._reply_child_comments = None
        self._done = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if author is not None:
            self.author = author
        if author_initials is not None:
            self.author_initials = author_initials
        if comment_text is not None:
            self.comment_text = comment_text
        if comment_date is not None:
            self.comment_date = comment_date
        if reply_child_comments is not None:
            self.reply_child_comments = reply_child_comments
        if done is not None:
            self.done = done

    @property
    def path(self):
        """Gets the path of this DocxTopLevelComment.  # noqa: E501

        Path to the comment in the document  # noqa: E501

        :return: The path of this DocxTopLevelComment.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DocxTopLevelComment.

        Path to the comment in the document  # noqa: E501

        :param path: The path of this DocxTopLevelComment.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def author(self):
        """Gets the author of this DocxTopLevelComment.  # noqa: E501

        Author name of the comment  # noqa: E501

        :return: The author of this DocxTopLevelComment.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DocxTopLevelComment.

        Author name of the comment  # noqa: E501

        :param author: The author of this DocxTopLevelComment.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def author_initials(self):
        """Gets the author_initials of this DocxTopLevelComment.  # noqa: E501

        Initials of the author of the comment  # noqa: E501

        :return: The author_initials of this DocxTopLevelComment.  # noqa: E501
        :rtype: str
        """
        return self._author_initials

    @author_initials.setter
    def author_initials(self, author_initials):
        """Sets the author_initials of this DocxTopLevelComment.

        Initials of the author of the comment  # noqa: E501

        :param author_initials: The author_initials of this DocxTopLevelComment.  # noqa: E501
        :type: str
        """

        self._author_initials = author_initials

    @property
    def comment_text(self):
        """Gets the comment_text of this DocxTopLevelComment.  # noqa: E501

        Text content of the comment  # noqa: E501

        :return: The comment_text of this DocxTopLevelComment.  # noqa: E501
        :rtype: str
        """
        return self._comment_text

    @comment_text.setter
    def comment_text(self, comment_text):
        """Sets the comment_text of this DocxTopLevelComment.

        Text content of the comment  # noqa: E501

        :param comment_text: The comment_text of this DocxTopLevelComment.  # noqa: E501
        :type: str
        """

        self._comment_text = comment_text

    @property
    def comment_date(self):
        """Gets the comment_date of this DocxTopLevelComment.  # noqa: E501

        Date timestamp of the comment  # noqa: E501

        :return: The comment_date of this DocxTopLevelComment.  # noqa: E501
        :rtype: datetime
        """
        return self._comment_date

    @comment_date.setter
    def comment_date(self, comment_date):
        """Sets the comment_date of this DocxTopLevelComment.

        Date timestamp of the comment  # noqa: E501

        :param comment_date: The comment_date of this DocxTopLevelComment.  # noqa: E501
        :type: datetime
        """

        self._comment_date = comment_date

    @property
    def reply_child_comments(self):
        """Gets the reply_child_comments of this DocxTopLevelComment.  # noqa: E501

        Child comments, that are replies to this one  # noqa: E501

        :return: The reply_child_comments of this DocxTopLevelComment.  # noqa: E501
        :rtype: list[DocxComment]
        """
        return self._reply_child_comments

    @reply_child_comments.setter
    def reply_child_comments(self, reply_child_comments):
        """Sets the reply_child_comments of this DocxTopLevelComment.

        Child comments, that are replies to this one  # noqa: E501

        :param reply_child_comments: The reply_child_comments of this DocxTopLevelComment.  # noqa: E501
        :type: list[DocxComment]
        """

        self._reply_child_comments = reply_child_comments

    @property
    def done(self):
        """Gets the done of this DocxTopLevelComment.  # noqa: E501

        True if this comment is marked as Done in Word, otherwise it is false  # noqa: E501

        :return: The done of this DocxTopLevelComment.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this DocxTopLevelComment.

        True if this comment is marked as Done in Word, otherwise it is false  # noqa: E501

        :param done: The done of this DocxTopLevelComment.  # noqa: E501
        :type: bool
        """

        self._done = done

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
        if issubclass(DocxTopLevelComment, dict):
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
        if not isinstance(other, DocxTopLevelComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other