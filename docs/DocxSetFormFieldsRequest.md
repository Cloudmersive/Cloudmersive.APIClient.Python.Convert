# DocxSetFormFieldsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_bytes** | **str** | Optional: Bytes of the input file to operate on | [optional] 
**input_file_url** | **str** | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
**handlebar_fields_to_fill** | [**list[FillHandlebarFormField]**](FillHandlebarFormField.md) | Handlebar style form fields to fill in; form field that is handlebar style, such as \&quot;{{FieldName}}\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


