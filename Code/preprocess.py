import xmltodict


def processXML(path):
    with open(path + "/Sysmon.xml") as fd:
        doc = xmltodict.parse(fd.read())
        return doc["Events"]["Event"][0]["System"]["Execution"]['@ProcessID']


if __name__ == '__main__':
    processXML('./Example_Test/Test_1')
