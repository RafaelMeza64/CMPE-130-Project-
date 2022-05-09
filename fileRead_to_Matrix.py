# File to convert .txt tab delimiter file to 2-D matrix format

import csv
from tkinter import N 
import xml.etree.ElementTree as ET
import os
import re

def changeFormat(fileName, formatType, fortemp = ""):
    
    print("File Reference: \"" + fileName + "\"")
    if (formatType == '-c'):
        txt_to_csv(fileName, fortemp)
    else:
        raise Exception("Selection is not \"-c\"\nProgram Terminated!")

def txt_to_csv(fileName, fortemp):
    print("...Converting .txt to .csv...\n")
    matrix = []
    with open(fileName, newline='') as file:
        fileReader = csv.reader(file, delimiter='\t')
        
        if fortemp != "":
            fileNameWOfileType = fortemp
        else:
            split = fileName.split(".")
            fileNameWOfileType = split[0]

        newFile = open(fileNameWOfileType + ".csv", 'w')
        csvWriter = csv.writer(newFile)
        
        for x in fileReader: 
            matrix.append(x)
            # print(x)
            csvWriter.writerow(x)
        newFile.close()

    count = 0
    # for i in range(len(matrix[0])):
    #     if i == 0:
    #         continue
    #     else:
    #         print("(" + str(i) + ") " + str(matrix[0][i]))
    
    for i in reversed(range(len(matrix[0]))):
        # print(matrix[i][j])
        if matrix[0][i] == "":
            # print(str(0) + " " + str(i))
            count += 1
            del matrix[0][i]
        else:
            break
    
    # print(matrix[1])
    # print(len(matrix[1]))
    # print("Count:", count)

    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])-1, (len(matrix[i])-count)-1, -1):
            # print(len(matrix[i]))
            # print(count)
            # print("Deleting:", i, j, matrix[i][j])
            del matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "":
                matrix[i][j] = '0'

    for i in range(len(matrix)):
        del matrix[i][0]
    
    print("Header: " + str(matrix[0]) + "\n")

    del matrix[0]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
        

    print("Matrix:", matrix)
    temp = ""
    temp += "["
    for i in range(len(matrix)-1):
        temp += (str(matrix[i]) + ", ")
    temp += (str(matrix[len(matrix)-1]) + "]")

    print(temp + "\n")

    # for i in range(len(matrix)):
    #     print("Row Count #" + str(i+1) + ": " + str(len(matrix[i])))

    # print(matrix[22])


    # tempFileName = fileName.split(".")
    # tempFilecsv = tempFileName[0] + ".csv"
    # print(tempFilecsv)
    # print("Row Count: " + str(numRows(tempFilecsv)))
    print("Converted to .csv\n")

def numRows(fileName) -> int:
    rowCount = 0
    validity = re.search(".*\.csv$", fileName)
    # print("Validity:", validity)
    if validity == None:
        raise Exception("Invalid file type. Must be .csv type.")
    else:
        csvFileOpen = open(fileName, 'r')
        csvData = csv.reader(csvFileOpen)

        for row in csvData:
            if len(row) <= 0:
                continue
            else:
                rowCount += 1

    return rowCount
    

############################################
# Main Function

# fileNameChoice = input("Would you like to input a file? Y/N: ")
fileNameChoice = "N"

while(True):
    if (fileNameChoice == 'Y' or fileNameChoice == 'y'):
        fileName = input("Your .txt file name (do not include file type): ")
        fileName = fileName + ".txt"
        break
    elif (fileNameChoice == 'N' or fileNameChoice == 'n'):
        fileName = "Walmart Neighborhood Market Matrix.txt"
        break
    else:
        fileNameChoice = input("Invalid choice. Please pick Y/N: ")

choice = "-c"

changeFormat(fileName, choice)

print("Program Terminated!\n")