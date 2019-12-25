# GetDocxTableRowRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_bytes** | **str** | Optional: Bytes of the input file to operate on | [optional] 
**input_file_url** | **str** | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
**table_path** | **str** | Path to the table to retrievew the row from | [optional] 
**table_row_row_index** | **int** | 0-based index of the row to retrieve (e.g. 0, 1, 2, ...) in the table | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

