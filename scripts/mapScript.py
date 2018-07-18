import subprocess
import os
import csv

modelDir = input("model directory: ")
weightsDir = input("weights directory: ")
bestmAP = 0
bestfilename = ""
for filename in os.listdir(weightsDir):
    tempmAP = os.system("darknet.exe detector map data\\voc.data {} {}\\{}> out.txt".format(modelDir, weightsDir, filename))
    # tempmAP = subprocess.check_output("darknet.exe", "detector", "map", "data\\voc.data", "modelDir", weightsDir + "\\" + filename)
    tempmAP = open("out.txt", "r").read()
    newTemp = float(tempmAP[tempmAP.find("(mAP)"):-1].split(" ")[-3])
    print(newTemp)
    print(type(newTemp))
    print(bestmAP)
    print(type(bestmAP))
    if (newTemp >= bestmAP):
        bestmAP = newTemp
        bestfilename = filename

top = open("bestmAP_" + bestfilename, "w").write("mAP: {} \n filename: {}".format(bestmAP, bestfilename))