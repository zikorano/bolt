from urllib.request import url2pathname
import os

def playlistRelative(sourceFilePath: "str") -> "list[str]":
    newFilelines = []
    sourceFile = open(sourceFilePath, "rb")
    fileLines = sourceFile.readlines()
    
    for line in fileLines:
        decodedLine = line.decode("UTF-8")
        if not decodedLine.startswith("#"):
            newFilelines.append(url2pathname(decodedLine))
    
    sourceFile.close()
    return newFilelines

def playlistAbsolute(sourceFilePath: "str", rpPlLines: "list[str]"):
    sourceFilePath = os.path.abspath(sourceFilePath)

    pathUnion = rpPlLines[0].split("/")[0]
    pathHead = sourceFilePath.split(pathUnion)[0]

    rpPlLines = [(pathHead + rpLine).replace("\n", "") for rpLine in rpPlLines]
    return rpPlLines

def convertPlaylistFile(sourceFilePath: "str"):
    relativePL = playlistRelative(sourceFilePath)
    absolutePL = playlistAbsolute(sourceFilePath, relativePL)
    outputPath = sourceFilePath.replace(".m3u8", ".m3u")
    outputFile = open(outputPath, "w")

    outputFile.write("".join(absolutePL))
    outputFile.close()
