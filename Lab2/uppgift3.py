def avbetalningsplan(skuld, räntesats, belopp):
    print("Årlig avbetalning: " +str(belopp))
    print("Räntesats: " + str(räntesats*100))
    print("Ingående skuld: " + str(skuld))
    year=1
    ränta=räntesats*skuld
    while(belopp<(skuld+ränta)):
        

        print("-- År " +str(year)+" --")
        skuld=skuld+ränta-belopp
        print("Återstående skuld: " + str(skuld))
        print("Amorterat belopp: " + str(belopp-ränta))
        print("Ränta: " + str(ränta))
        year=year+1
        ränta=räntesats*skuld
    
    
    
    print("-- År " +str(year)+" --")
    ränta=räntesats*skuld
    print("Återstående skuld: 0")
    print("Amorterat belopp: " + str(skuld))
    print("Ränta: " + str(ränta))
    
avbetalningsplan(100,0.05,25)
