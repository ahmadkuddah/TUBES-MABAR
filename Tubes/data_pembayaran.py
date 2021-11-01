tagihan=''
def tagihan_(ID):
    global tagihan
    if 0 <= ID < 10000:
        tagihan='50000'

    elif 10000 <= ID < 20000:
        tagihan='75000'
  
    elif 20000 <= ID < 30000:
        tagihan='100000'
  
    elif 30000 <= ID < 40000:
        tagihan='150000'
  
    elif 40000 <= ID < 50000:
        tagihan='250000'
  
    elif 50000 <= ID < 60000:
        tagihan='500000'
   
    elif 60000 <= ID < 70000:
        tagihan='750000'

    elif 70000 <= ID < 80000:
        tagihan='1000000'

    elif 80000 <= ID < 90000:
        tagihan='1500000'

    elif 90000 <= ID < 99999:
        tagihan='2000000'

    return
