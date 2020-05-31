import preprocess
def train():
    processID = []
    for i in range(1, 7):
        processID.append(preprocess.processXML('./Train/Person_' + str(i)))
    return processID


if __name__ == '__main__':
    print(train())

