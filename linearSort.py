"""
linear sort
- input format XYY: X=a..h Y=0..9
"""
from LinkedList import LinkedList, Node


def hash(size, value):
    if len(value)!=3:
        return None
    value = value if isinstance(value, str) else str(value)
    return sum(map(lambda x:ord(x),value)) % size


def parse(s):
    if len(s)!=3:
        return None
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(s[0])
    num = int(s[1]+s[2])
    return letter*99+num


def ksort(dataset):
    size = len(dataset)
    m = []
    for i in range(size):
        m.append(LinkedList())
    for i in dataset:
        id = int(parse(i)//(792/size))
        if id != None:
            m[id].add(Node(i))
    return m
    

def gen_data(num_of_data):
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = 99
    container = []
    for i in range(num_of_data):
        l_id = random.randint(0,len(letters)-1)
        data = letters[l_id]+str(random.randint(0,9))+str(random.randint(0,9))
        container.append(data)
    return container



########### test ##################
if __name__ == "__main__":
    data = gen_data(20)
##    print(data)
    sorted = []
    print([x.get_arr() for x in ksort(data) if len(x)>0])