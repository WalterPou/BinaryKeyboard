class MainProgram {
	[string]CharConvert([string]$let) {
		$byte=[System.Convert]::ToString([int][char]$let,2).PadLeft(8,'0')
		return $byte
	}

	[string]BytesChunk([string]$str) {
		$bytes=@()
		for ($i=0;$i -lt $str.Length;$i+=8) {
			$r=$str.Length-$i
			$c=[System.Math]::Min(8,$r)
			$bytes+=$str.Substring($i,$c)
		}
		$bytes=$bytes -join ' '
		return $bytes
	}

	[string]BinaryConvert([string]$binaries) {
		$bytes=$this.BytesChunk($binaries)
		$outString=($bytes.Split(' ')|foreach-object {[char]([System.Convert]::ToInt32($_,2))})-join ''
		return $outString
	}

	[string]StringConvert([string]$str) {
		$array=$str.ToCharArray()
		$outBin=-join($array|foreach-object {$this.CharConvert($_)})
		return $outBin
	}
}

$utils=[MainProgram]::new()

while ($true) {
	$userInput=read-host ">"
	if (!$userInput) {write-host "No Command."}
	if ($userInput -eq "?") {
		write-host "chc -- Character To Byte"
		write-host "byc -- Bytes To Byte Chunks"
		write-host "bic -- Binary To String"
		write-host "stc -- String To Binary"
	}
	if ($userInput -eq "chc") {
		try {
			$let=read-host "Char"
			write-host $utils.CharConvert($let)
		}
		catch {
			write-host "Invalid Input! Must be a single ascii character." -foreground red
		}
	}
	if ($userInput -eq "byc") {
		try {
			$bytes=read-host "Bytes"
			write-host $utils.BytesChunk($bytes)
		}
		catch {
			write-host "Invalid Input! Must be a valid bytes string." -foreground red
		}
	}
	if ($userInput -eq "bic") {
		try {
			$bytes=read-host "Bytes String"
			write-host $utils.BinaryConvert($bytes)
		}
		catch {
			write-host "Invalid Input! Must be a valid bytes string." -foreground red
		}
	}
	if ($userInput -eq "stc") {
		try {
			$text=read-host "String"
			write-host $utils.StringConvert($text)
		}
		catch {
			write-host "Invalid Input! Must be a valid string type. (ASCII)" -foreground red
		}
	}
}
