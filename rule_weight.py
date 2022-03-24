




def set_weight(list):
    '''

    :param list: a list of float to be saved
    :return:
    '''
    rule_weight = open("rule_weight.txt","w")
    for value in list:
        rule_weight.write(str(value)+"\n")
    rule_weight.close()

def read_weight():
    '''

    :return: the list of floating point saved in rule_weight.txt
    '''
    with open("rule_weight.txt","r") as f:
        weight = [float(line.strip()) for line in f]
        f.close()
        return weight


if __name__ == "__main__":
    set_weight([1,2,3])
    print(read_weight())