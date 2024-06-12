# Chunks From A List in python

def chunks(lst:list, n:int):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

sample: list[str] = ['a','b','c','d','e']
print(sample)
print(list(chunks(sample,3)))