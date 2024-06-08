def towerOfHanoi(n,from_rod,to_rod,aux_rod):
    if(n==1):
        print(f'Disk {n} moved from Disk {from_rod} to Disk {to_rod}')
    else:
        towerOfHanoi(n-1,from_rod,aux_rod,to_rod)
        print(f'Disk {n} moved from Disk {from_rod} to Disk {to_rod}')
        towerOfHanoi(n-1,aux_rod,to_rod,from_rod)
        

towerOfHanoi(3,'a','c','b')
