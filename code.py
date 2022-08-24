def count_occurances(a):
    '''
    Counts the number of times each letter occurs in the input string. Returns
    a dictionary with names of each nucleotide with the number of off occurances
    for each nucleotide.

        Parameters:
                a (str): a string of nucleotides

        Returns:
                b (dict): dictionary of counts. keys are nucleotides.
    '''
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def count_to_prop(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

counts = count_occurances('ATCTGACGCGCGCCGC')
prop = count_to_prop(counts)
prop
