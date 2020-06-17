from argparse import ArgumentParser
import preprocess, model
import os


def operation(processID, name):
    ID = preprocess.processXML(args.path + '/' + testcase, name)
    result = model.findID(processID, ID)
    return result


parser = ArgumentParser(description="python3 [-t] main.py <TEST_PATH>\n"
                                    "Example: python3 --train main.py ./Example_Test/")
parser.add_argument("-t", action='store_true', help="Train model")
parser.add_argument("path", help="Test Path")
args = parser.parse_args()

if args.t == True:
    print('=====Train=====')
    processSysmonID = model.trainID('Sysmon')
    processSecurityID = model.trainID('Security')
    print('=====Train=====')
else:
    processSysmonID = ['2480', '2844', '2944', '2848', '3008', '1036']
    processSecurityID = ['{9e1903ff-2cdb-0000-0b05-199edb2cd601}', '{3591cc69-2cda-0001-b1cc-9135da2cd601}', '{46ce64eb-2cda-0001-3665-ce46da2cd601}', '{a21559d7-2cda-0001-275a-15a2da2cd601}', '{e0e75f9b-2cda-0001-ec5f-e7e0da2cd601}', '{7eccaef9-2cd8-0000-01b0-cc7ed82cd601}']

processDNS = preprocess.processTFIDF()
test = sorted(os.listdir(args.path))
print('=====Test=====')
for testcase in test:
    user = operation(processSysmonID, 'Sysmon')
    if user == 0:
        user = operation(processSecurityID, 'Security')
        if user == 0:
            user = preprocess.processJSON(args.path + '/' + testcase, 'Wireshark')
            if not user:
                user = 1
            else:
                user = user.split()
                user = sorted(set(user), key = name.index)
                user = model.predict(processDNS, user) + 1
    print(testcase + ': ' + 'person ' + str(user))

print('=====Test=====')

