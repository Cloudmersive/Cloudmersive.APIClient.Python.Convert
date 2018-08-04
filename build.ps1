#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli.jar generate -i https://api.cloudmersive.com/swagger/api/convert -l python -c packageconfig.json

# Bug fix

$newcontent = (Get-Content ./core/replace.py -Raw)
Write-Host $newcontent
(Get-Content ./cloudmersive_convert_api_client/api_client.py).replace('if response_type:', $newcontent) | Set-Content ./cloudmersive_convert_api_client/api_client.py
(Get-Content ./cloudmersive_convert_api_client/rest.py).replace((Get-Content ./core/rest_match.py -Raw), (Get-Content ./core/rest_replace.py -Raw)) | Set-Content ./cloudmersive_convert_api_client/rest.py