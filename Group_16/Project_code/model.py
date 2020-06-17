import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def findID(train, test):
    for i in range(1, 7):
        if name == processSecurityID[i-1]:
            return i
    return 0


def predict(train, test):
    n = 0
    index = 0
    for i in range(len(train)):
        weightsum = 0
        for j in range(len(test)):
            tmp = train[i].get(test[j], 0)
            weightsum += tmp
        if weightsum >= n:
            n = weightsum
            index = i
    return index


def trainDNS(name):
    query = []
    for i in range(1, 7):
        query.append(preprocess.processJSON('./Train/Person_' + str(i), name))
    vectorizer = TfidfVectorizer(token_pattern='\S+')
    DNS = vectorizer.fit_transform(query).toarray()
    feature = vectorizer.get_feature_names()
    with open('train.tfidf', 'w') as fd:
        for i in range(len(DNS)):
            for j in range(len(feature)):
                fd.write(feature[j] + ' ' + str(DNS[i][j]) + '\n')
            fd.write('Person\n')
    return DNS


def trainID(name):
    processID = []
    for i in range(1, 7):
        processID.append(preprocess.processXML('./Train/Person_' + str(i), name))
    return processID


if __name__ == '__main__':
    print(trainDNS('Wireshark'))
#    print(trainID('Sysmon'))
#    print(trainID('Security'))
    pass

