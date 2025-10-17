def analizaBitke(bitka):
    napad, obramba = 0,0
    for i in range(len(bitka[0])):
        if bitka[0][i] > bitka[1][i]:
            napad += 1
        if bitka[0][i] < bitka[1][i]:
            obramba += 1
    return [napad, obramba]

def zloziPapir(planet):
    planet_id = 0
    planeti = [["zemlja", "mars", "jupiter",],[384400000,225000000000, 778000000000]]
    for i, planet_išče in enumerate(planeti[0]):
        if planet_išče == planet:
            planet_id = i
            break
    debelina_lista = 0.0001
    št_pregibov = 0
    #print(f"Planet_id: {planet_id}")
    #print(f"planeti[1][planet_id]: {planeti[1][planet_id]}")
    while debelina_lista < planeti[1][planet_id]:
        #print(št_pregibov, debelina_lista)
        debelina_lista = debelina_lista * 2
        št_pregibov += 1
    return planet_id, [planet, planeti[1][planet_id],št_pregibov]

        
#print(analizaBitke([[1,2,3],[1,3,2]])) #[1,1]
#print(analizaBitke([[2,3,6,8,2,4,6],[2,3,5,6,7,5,4]])) #[3,2]
#print(zloziPapir("mars"))
#print(zloziPapir("zemlja"))
