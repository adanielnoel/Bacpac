from main import dataset


scores = dataset['score']
sorter = range(len(scores))


def sort(a, b):
    """ Sort lists a and b according to a in increasing order"""
    a, b = [list(x) for x in zip(*sorted(zip(a, b), key=lambda pair: pair[0]))]
    return b


def update_dict(dict, removed_index):
    """ Mutates dict object and deletes row"""
    dict.drop(dataset.index[removed_index], inplace=True)
    return dict