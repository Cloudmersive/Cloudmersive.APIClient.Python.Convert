﻿Remove-Item –path ./cloudmersive_convert_api_client –recurse
& java -jar swagger-codegen-cli-2.4.14.jar generate -i https://api.cloudmersive.com/swagger/api/convert -l python -c packageconfig.json

# Bug fix

$newcontent = (Get-Content ./core/replace.py -Raw)
Write-Host $newcontent
(Get-Content ./cloudmersive_convert_api_client/api_client.py).replace('if response_type:', $newcontent) | Set-Content ./cloudmersive_convert_api_client/api_client.py
(Get-Content ./cloudmersive_convert_api_client/rest.py).replace((Get-Content ./core/rest_match.py -Raw), (Get-Content ./core/rest_replace.py -Raw)) | Set-Content ./cloudmersive_convert_api_client/rest.py



$extrasetup = (Get-Content ./extrasetup.py) -join "`n"
Write-Host $extrasetup
(Get-Content ./setup.py).replace('# http://pypi.python.org/pypi/setuptools', $extrasetup) | Set-Content ./setup.py
(Get-Content ./setup.py).replace('"""\', "long_description,`n    long_description_content_type='text/markdown'") | Set-Content ./setup.py
(Get-Content ./setup.py).replace('Convert API lets you effortlessly convert file formats and types.  # noqa: E501', '') | Set-Content ./setup.py
(Get-Content ./setup.py).replace('    """', '') | Set-Content ./setup.py
(Get-Content ./README.md).replace('This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:', 'This Python package provides a native API client for [Cloudmersive Document Conversion](https://www.cloudmersive.com/convert-api)') | Set-Content ./README.md
Write-Host "Done."