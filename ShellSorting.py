"""
Shell Sorting
    sorting in several times by sequence
    "Knutt sequence" => 
        d(0) = 1
        d(i)=3*d(i-1)+1
"""
from InsertSorting import sort


def get_seq(item_len):
    i = 1
    seq = []
    while i<item_len:
        seq.append(i)
        i = 3*i+1
    return seq[::-1]

def shellSort(item):
    print("===shell started===\n")
    for i in get_seq(len(item)):
        step = i-1 if i>1 else i
        print("\n\n=step is",i)
        sort(item, step)

if __name__ == "__main__":
    shellSort([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])