from argparse import ArgumentParser
from Code import preprocess
import os

parser = ArgumentParser(description="python3 main.py <FILE_PATH>")
parser.add_argument("path", help="input")
args = parser.parse_args()

computer = []

for i in range(1, 7):
    computer.append(preprocess.processXML('./Logs/Train/Person_' + str(i) + "/Sysmon.xml"))

test = os.listdir('./Example_Test')
num = 1
for testcase in test:
    name = preprocess.processXML('./Example_Test/' + testcase + '/Sysmon.xml')
    for i in range(6):
        if name == computer[i]:
            print('testcase ' + str(num) + ':' + 'person' + str(i))
            num += 1
            break
