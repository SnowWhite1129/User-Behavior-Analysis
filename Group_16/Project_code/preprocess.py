import xmltodict


def processXML(path, name):
    with open(path + "/" + name +".xml") as fd:
        try:
            doc = xmltodict.parse(fd.read())
            if name == 'Sysmon':
                for i in range(100000):
                    try:
                        data = doc["Events"]["Event"][i]["System"]["Execution"]['@ProcessID']
                    except:
                        continue
                    if data != None:
                        break
            else:
                for i in range(100000):
                    try:
                        data = doc["Events"]["Event"][i]["System"]["Correlation"]['@ActivityID']
                    except:
                        continue
                    if data != None:
                        break
        except:
            data = None
        return data


if __name__ == '__main__':
    processXML('./Example_Test/Test_1')
