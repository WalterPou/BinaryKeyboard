$filePath=read-host "File"
$content=Get-Content -Path $filePath
$chunks=@()
for($i=0;$i -lt $content.Length;$i+=8){$r=$content.Length-$i;$c=[System.Math]::Min(8,$r);$chunks+=$content.Substring($i,$c)}
$chunks=$chunks -join ' '
$command=($chunks.Split(' ')|ForEach-Object{[char]([convert]::ToInt32($_,2))})-join ''
write-host $command
$command | Out-File "temp.py" -Encoding utf8
clear
python3 temp.py
Remove-Item "temp.py"
