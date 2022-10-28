if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i_lista = [ x for x in range(0,x+1)]
    j_lista = [ y for y in range(0,y+1)]
    k_lista = [ z for z in range(0,z+1)]
    
    allproduct = [[x,y,z] 
            for x in i_lista
            for y in j_lista
            for z in k_lista
            if sum([x,y,z]) != n]