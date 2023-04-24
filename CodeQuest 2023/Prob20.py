cases = int(input())



for caseNum in range(cases):
    bar_amount = int(input())
    packages, standard, first, priority, mail_id, zipcode = 0,0,0,0,0,0
    for code in range(bar_amount):
        barcode = input()
        if len(barcode) == 48:
            
