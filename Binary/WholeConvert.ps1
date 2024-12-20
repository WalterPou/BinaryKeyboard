class BinarySystem {
	[string]ConvertToAscii([string]$binary) {
		$output=($binary.Split(' ')|ForEach-Object {[Char]([Convert]::ToInt32($_,2))}) -join ''
		return $output
	}

	[string]BitFromQuery([string]$query) {
		$chunks=@()
		for ($i=0;$i -lt $query.Length;$i+=8){$rLen=$query.Length-$i;$cLen=[System.Math]::Min(8,$rLen);$chunks+=$query.Substring($i,$cLen)}
		$chunks=$chunks -join ' '
		return $this.ConvertToAscii($chunks)
	}
}

$BinarySystem=[BinarySystem]::new()
$userInput=read-host "TargetFile: "
$out=read-host "OutFile: "
$content=Get-Content -Path $userInput -Raw
$results=$BinarySystem.BitFromQuery($content)
write-host "Decoded File: $($out)"
New-Item $out
$results > $out
