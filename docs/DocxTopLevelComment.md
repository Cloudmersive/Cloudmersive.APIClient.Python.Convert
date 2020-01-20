# DocxTopLevelComment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to the comment in the document | [optional] 
**author** | **str** | Author name of the comment | [optional] 
**author_initials** | **str** | Initials of the author of the comment | [optional] 
**comment_text** | **str** | Text content of the comment | [optional] 
**comment_date** | **datetime** | Date timestamp of the comment | [optional] 
**reply_child_comments** | [**list[DocxComment]**](DocxComment.md) | Child comments, that are replies to this one | [optional] 
**done** | **bool** | True if this comment is marked as Done in Word, otherwise it is false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


