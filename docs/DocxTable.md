# DocxTable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | The ID of the table | [optional] 
**width** | **str** | The Width of the table, or 0 if not specified | [optional] 
**width_type** | **str** | The Width configuration type of the table | [optional] 
**table_rows** | [**list[DocxTableRow]**](DocxTableRow.md) | Rows in the table; this is where the contents is located | [optional] 
**top_border_type** | **str** | Type for the top border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**top_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**top_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**top_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**bottom_border_type** | **str** | Type for the bottom border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**bottom_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**bottom_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**bottom_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**left_border_type** | **str** | Type for the left border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**left_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**left_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**left_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**right_border_type** | **str** | Type for the right border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**right_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**right_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**right_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**cell_horizontal_border_type** | **str** | Type for the cell horizontal border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**cell_horizontal_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**cell_horizontal_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**cell_horizontal_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**cell_vertical_border_type** | **str** | Type for the cell vertical border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**cell_vertical_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**cell_vertical_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**cell_vertical_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**start_border_type** | **str** | Type for the start border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**start_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**start_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**start_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**end_border_type** | **str** | Type for the end border - can be a Single, DashDotStroked, Dashed, DashSmallGap, DotDash, DotDotDash, Dotted, Double, DoubleWave, Inset, Nil, None, Outset, Thick, ThickThinLargeGap, ThickThinMediumGap, ThickThinSmallGap, ThinThickLargeGap, ThinThickMediumGap, ThinThickSmallGap, ThinThickThinLargeGap, ThinThickThinMediumGap, ThinThickThinSmallGap, ThreeDEmboss, ThreeDEngrave, Triple, Wave | [optional] 
**end_border_size** | **int** | Width of the border in points (1/72nd of an inch) | [optional] 
**end_border_space** | **int** | Spacing around the border in points (1/72nd of an inch) | [optional] 
**end_border_color** | **str** | HTML-style color hex value (do not include a #) | [optional] 
**table_indentation_mode** | **str** | Table indentation type | [optional] 
**table_indentation_width** | **int** | Table indentation width | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


