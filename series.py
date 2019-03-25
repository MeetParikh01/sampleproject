def read_series (filename):
    f=open(filename, mode='rt', encoding='utf-8')
    series=[]
    for line in f:
        a=int(line.strip())
        series.append(a)
    f.close()
    return series

def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    f=open(filename, mode='wt', encoding='utf-8')
    print(str(islice(sequence(), num+1)))
    f.writelines("{0}\n".format(r) for r in islice(sequence(), num+1))
    f.close()

def main(filename):
    series = read_series(filename)
    print(series)
