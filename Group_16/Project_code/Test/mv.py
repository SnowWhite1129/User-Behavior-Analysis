import os


for i in range(1, 7):
    dir = 'Test_' + str(i)
    for j in range(1, 7):
        sub_dir = dir + "/" + dir + '_' + str(j)
        sub_file = sub_dir + "/wireshark2.json"
        os.system('mv ' + sub_file + ' ' + sub_dir + '/Wireshark.json')
        