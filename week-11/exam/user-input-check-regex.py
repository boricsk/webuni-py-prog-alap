import re
import base64
import urllib.parse
from math import log
from collections import Counter
from rich import print as rprint


def checkUserInput(string: str):
    encodedStringList = []
    print('')
    rprint(f'[bold][yellow]Start investigation of "{string}"[/bold][/yellow]')
    if isUrldecode(string):
        stringList = decodeUrl(string).split()
        rprint(f'URL coding found')
    else:
        stringList = string.split()
        print(f'URL coding not found')
    
    for item in stringList:
        if shannon(item) > 6:
            rprint(f'Compressed or encrypted data found in [purple]{item}Shannon entropy is : {shannon(item)}[/purple]')
        else:
            #rprint(f'Compressed or encrypted data not found in [purple]{item}[/purple]')
            pass
            
        if isBase64(item):
            encodeLevel, encodedData = encodingLevelBase64(item)
            rprint(f'Base64 data found, decode results : [purple]{encodeLevel}[/purple] times encoding detected. Encoded data : [purple]{encodedData}[/purple]')
            encodedStringList.append(encodedData)
        else:
            #print(f'No Base64 data found in {item}')
            encodedStringList.append(item)
    
    stringToCheck = ' '.join([item for item in encodedStringList])
    
    if bool(re.search(r"(\s*([\0\b\'\"\n\r\t\%\_\\]*\s*(((select\s*.+\s*from\s*.+)|(insert\s*.+\s*into\s*.+)|(update\s*.+\s*set\s*.+)|(delete\s*.+\s*from\s*.+)|(drop\s*.+)|(truncate\s*.+)|(alter\s*.+)|(exec\s*.+)|(\s*(all|any|not|and|between|in|like|or|some|contains|containsall|containskey)\s*.+[\=\>\<=\!\~]+.+)|(let\s+.+[\=]\s*.*)|(begin\s*.*\s*end)|(\s*[\*]+\s*.*\s*[\*]+)|(\s*(\-\-)\s*.*\s+)|(\s*(contains|containsall|containskey)\s+.*)))(\s*[\;]\s*)*)+)", stringToCheck)):
        rprint(f'[bold]SQLi injection command found in :[/bold] [red]{string}[/red]')
        
    else:
        rprint('[bold][green]User Input OK[/bold][/green]')
        
            
def shannon(string):
    counts = Counter(string)
    frequencies = ((i / len(string)) for i in counts.values())
    return - sum(f * log(f, 2) for f in frequencies)

def isBase64(data): # ellenőrzi a base64 kódolt szöveget
    if re.search(r"(?:^(?:[A-Za-z0-9+\/]{4}\n?)*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)$)", data):
        #print(f'Data in base 64 check : {data}')
        return True
    else:
        return False

def isUrldecode(data):
    if re.search(r"%([A-Fa-f0-9])*", data):
        return True
    else:
        return False

def decodeUrl(urlString):
    return urllib.parse.unquote(urlString)

def encodingLevelBase64(data): # A kódolás szintjét határozza meg, ha többször van kódolva a szöveg
    encodingLevel = 0
    while isBase64(data):
        dataTemp = str(base64.b64decode(bytes(data,'utf-8')))
        data = ''.join(dataTemp[2:len(dataTemp)-1])
        encodingLevel += 1
    return encodingLevel, data

checkUserInput('This is a text VjJ0V2EySXlUa2hVYWxaU1ltdEtjVnBXVmt0aU1VNVdZVVpPYVZJeFdrcFdWbEYzVUZFOVBRPT0=')
checkUserInput('This is a second text TElLRSDigJglcGFzc3dvcmQl4oCZOlNFTEVDVCBESVNUSU5DVCByZWxuYW1lIEZST00gcGdfY2xhc3MgQywgcGdfbmFtZXNwYWNlIE4sIHBnX2F0dHJpYnV0ZSBBLCBwZ190eXBlIFQgV0hFUkUgKEMucmVsa2luZD3igJlyJykgQU5EIChOLm9pZD1DLnJlbG5hbWVzcGFjZSkgQU5EIChBLmF0dHJlbGlkPUMub2lkKSBBTkQgKEEuYXR0dHlwaWQ9VC5vaWQpIEFORCAoQS5hdHRudW0+MCkgQU5EIChOT1QgQS5hdHRpc2Ryb3BwZWQpIEFORCAoTi5uc3BuYW1lIElMSUtFIOKAmHB1YmxpY+KAmSkgQU5EIGF0dG5hbWUgTElLRSDigJglcGFzc3dvcmQl4oCZOw==')
checkUserInput('This is a text \'or 1=1 --')
checkUserInput('This is a text \'or 1=1 #')
checkUserInput('This is a text SELECT CONCAT("A","B","C")')
checkUserInput('This is a text SELECT name FROM someotherdb..sysobjects WHERE xtype = "U"')
checkUserInput('This is a text SELECT name FROM master..syslogins WHERE bulkadmin = 1;')
checkUserInput('This is a second text TElLRSDigJglcGFzc3dvcmQl4oCZOlNFTEVDVCBESVNUSU5DVCByZWxuYW1lIEZST00gcGdfY2xhc3MgQywgcGdfbmFtZXNwYWNlIE4sIHBnX2F0dHJpYnV0ZSBBLCBwZ190eXBlIFQgV0hFUkUgKEMucmVsa2luZD3igJlyJykgQU5EIChOLm9pZD1DLnJlbG5hbWVzcGFjZSkgQU5EIChBLmF0dHJlbGlkPUMub2lkKSBBTkQgKEEuYXR0dHlwaWQ9VC5vaWQpIEFORCAoQS5hdHRudW0%2BMCkgQU5EIChOT1QgQS5hdHRpc2Ryb3BwZWQpIEFORCAoTi5uc3BuYW1lIElMSUtFIOKAmHB1YmxpY%2BKAmSkgQU5EIGF0dG5hbWUgTElLRSDigJglcGFzc3dvcmQl4oCZOw%3D%3D')
checkUserInput('This is a regular user input')
checkUserInput('This is a regular user input nev="Jozsi" and if(left(zip,4)=2021,sleep(5),1)=1#')
