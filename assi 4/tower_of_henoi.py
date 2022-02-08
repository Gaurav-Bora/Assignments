count = 0
def henoi(disc,source,aux,target):
    global count
    if disc ==1:
        count = count + 1
        return
    
    henoi(disc - 1, source, target, aux)
    count = count + 1
    henoi(disc - 1, aux, source, target)
disc=int(input('enter discs: '))
henoi(disc, 'source', 'aux', 'target')
print(count)