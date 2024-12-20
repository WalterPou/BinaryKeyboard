class BinarySystem:
    def ConvertTo8Bit(self,binary):
        if len(binary)%8!=0:
            raise ValueError('Invalid 8 Bit')
        bytes=int(binary,2).to_bytes(len(binary)//8,byteorder='big')
        character=bytes.decode('ascii')
        return character
    
    def ConvertWholeTo8Bit(self,query):
        binaries=query.split(' ')
        string=''
        for binary in binaries:
            value=self.ConvertTo8Bit(binary)
            string+=value
        return string

    def ConvertFrom6Bit(self,binary):
        string=binary
        paddingLen=6-len(string)
        if paddingLen>0:
            for i in range(paddingLen):
                string+='0'
        print(string)
        decVal=0
        for i, bit in enumerate(reversed(string)):
            decVal+=int(bit)*2**i
        return decVal

    def ConvertWholeFrom6Bit(self,query):
        binaries=query.split(' ')
        string=''
        for binary in binaries:
            value=self.ConvertFrom6Bit(binary)
            string+=f'{value} '
        return string
    
    def Convert8BitTo6BitWhole(self,whole):
        BinaryBit8Temp=whole.split(' ')
        ''.join(BinaryBit8Temp)
        BinaryBit8=''
        for obj in BinaryBit8Temp:
            BinaryBit8+=obj
        BinaryBit6Chunk=[BinaryBit8[i:i+6] for i in range(0,len(BinaryBit8),6)]
        ''.join(BinaryBit6Chunk)
        print(BinaryBit6Chunk)
        BinaryBit6=''
        for obj in BinaryBit6Chunk:
            BinaryBit6+=f'{obj} '
        print(BinaryBit6)
        results=self.ConvertWholeFrom6Bit(BinaryBit6)
        return results
    
string="01101000 01100101 01101100 01101100 01101111"
results=BinarySystem().Convert8BitTo6BitWhole(string)
print(results)