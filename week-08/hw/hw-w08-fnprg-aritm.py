def vegrehajt(muvelet):
    szam1, muvelet, szam2 = muvelet.split()
    muveleti_jel = {
        '+': lambda sz1, sz2 : int(sz1) + int(sz2),
        '-': lambda sz1, sz2 : int(sz1) - int(sz2),
        '*': lambda sz1, sz2 : int(sz1) * int(sz2),
        '/': lambda sz1, sz2 : int(sz1) // int(sz2),
        '%': lambda sz1, sz2 : int(sz1) % int(sz2),
    }
    return muveleti_jel[muvelet](szam1, szam2)
    
print(vegrehajt('103 + 206'))
print(vegrehajt('103 - 206'))
print(vegrehajt('103 * 206'))
print(vegrehajt('103 / 206'))
print(vegrehajt('103 % 206'))
