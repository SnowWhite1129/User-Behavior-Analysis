from argparse import ArgumentParser
import preprocess, model
import os

parser = ArgumentParser(description="python3 [-t] main.py <TEST_PATH>\n"
                                    "Example: python3 --train main.py ./Example_Test/")
parser.add_argument("-t", action='store_true', help="Train model")
parser.add_argument("path", help="Test Path")
args = parser.parse_args()

if args.t == True:
    processID = model.train()
else:
    processID = ['2480', '2844', '2944', '2848', '3008', '1036']

test = os.listdir(args.path)
num = 1
for testcase in test:
    name = preprocess.processXML(args.path + testcase)
    for i in range(1, 7):
        if name == processID[i-1]:
            print('testcase ' + str(num) + ': ' + 'person' + str(i))
            num += 1
            break
