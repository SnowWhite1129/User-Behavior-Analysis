import xmltodict


def processXML(path):
    with open(path + "/Sysmon.xml") as fd:
        doc = xmltodict.parse(fd.read())
        return doc["Events"]["Event"]["System"]["Computer"]