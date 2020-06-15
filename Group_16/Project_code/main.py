from argparse import ArgumentParser
import preprocess, model
import os

parser = ArgumentParser(description="python3 [-t] main.py <TEST_PATH>\n"
                                    "Example: python3 --train main.py ./Example_Test/")
parser.add_argument("-t", action='store_true', help="Train model")
parser.add_argument("path", help="Test Path")
args = parser.parse_args()

if args.t == True:
    print('=====Train=====')
    processSysmonID = model.train('Sysmon')
    processSecurityID = model.train('Security')
    print(processSysmonID)
    print(processSecurityID)
    print('=====Train=====')
else:
    processSysmonID = ['2480', '2844', '2944', '2848', '3008', '1036']
    processSecurityID  = ['{9e1903ff-2cdb-0000-0b05-199edb2cd601}', '{3591cc69-2cda-0001-b1cc-9135da2cd601}', '{46ce64eb-2cda-0001-3665-ce46da2cd601}', '{a21559d7-2cda-0001-275a-15a2da2cd601}', '{e0e75f9b-2cda-0001-ec5f-e7e0da2cd601}', '{7eccaef9-2cd8-0000-01b0-cc7ed82cd601}']

test = os.listdir(args.path)
num = 1
print('=====Test=====')
for testcase in test:
    name = preprocess.processXML(args.path + '/' + testcase, 'Sysmon')
    if name == None:
        name = preprocess.processXML(args.path + '/' + testcase, 'Security')
        if name == None:
            print('testcase ' + str(num) + ': ' + 'person ' + str(1))
            num += 1
            continue
        else:
            for i in range(1, 7):
                if name == processSecurityID[i-1]:
                    print('testcase ' + str(num) + ': ' + 'person ' + str(i))
                    num += 1
                    break
    else:
        for i in range(1, 7):
            if name == processSysmonID[i-1]:
                print('testcase ' + str(num) + ': ' + 'person ' + str(i))
                num += 1
                break
print('=====Test=====')

