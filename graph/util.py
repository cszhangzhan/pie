def count_feature(history_matrix, filter_list):
    counter = 0
    for feature_list in history_matrix:
        match = True
        for t in filter_list:
            index = t[0]
            value = t[1]
            if feature_list[index] != value:
                match = False
                break
        if match:
            counter += 1
    return counter 

if __name__ == '__main__':
    f = open('history.data')
    lines = f.readlines()
    history_matrix = []
    for line in lines:
        line = line.strip('\n')
        feature_list = [int(feature) for feature in line.split(' ')]
        history_matrix.append(feature_list)
    filter_list = []
    filter_list.append([0, 1])
    filter_list.append([3, 2])
    print count_feature(history_matrix, filter_list)
