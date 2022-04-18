class tugas:
    def __init__(self):
        self.a = [3,1]
        self.b = [6,2]
        self.c = [7,4]
        self.d = [2,5]
        print("Titik Yang Diketahui")
        print(f"A : {self.a}")
        print(f"B : {self.b}")
        print(f"C : {self.c}")
        print(f"D : {self.d}")

    def translasi(self):
        print("TRANSLASI")
        self.t = [-4,2]
        print(f"Translasi : {self.t}")
        self.ta = [self.a[0]+self.t[0],self.a[1]+self.t[1]]
        self.tb = [self.b[0]+self.t[0],self.b[1]+self.t[1]]
        self.tc = [self.c[0]+self.t[0],self.c[1]+self.b[1]]
        self.td = [self.d[0]+self.t[0],self.d[1]+self.b[1]]
        print(f"Translasi A {self.a} -> {self.ta}")
        print(f"Translasi B {self.b} -> {self.tb}")
        print(f"Translasi C {self.c} -> {self.tc}")
        print(f"Translasi D {self.d} -> {self.td}")

    def rotasi(self):
        print("ROTASI")
        self.rotate = 65
        self.sc65 = [0.906 , 0.422] #sin 65 = 0.906 dan cos 65 = 0.422
        self.rotasiA1 = (self.ta[0] * self.sc65[1]) - (self.ta[0] * self.sc65[0])
        self.rotasiA2 = (self.ta[1] * self.sc65[1]) + (self.ta[1] * self.sc65[0])
        print("Nilai A setelah rotasi 65 derajat : ", "{:.2f}".format(self.rotasiA1),",","{:.2f}".format(self.rotasiA2))

        self.rotasiB1 = (self.tb[0] * self.sc65[1]) - (self.tb[0] * self.sc65[0])
        self.rotasiB2 = (self.tb[1] * self.sc65[1]) + (self.tb[1] * self.sc65[0])
        print("Nilai B setelah rotasi 65 derajat : ", "{:.2f}".format(self.rotasiB1),",","{:.2f}".format(self.rotasiB2))

        self.rotasiC1 = (self.tc[0] * self.sc65[1]) - (self.tc[0] * self.sc65[0])
        self.rotasiC2 = (self.tc[1] * self.sc65[1]) + (self.tc[1] * self.sc65[0])
        print("Nilai C setelah rotasi 65 derajat : ", "{:.2f}".format(self.rotasiC1),",","{:.2f}".format(self.rotasiC2))

        self.rotasiD1 = (self.td[0] * self.sc65[1]) - (self.td[0] * self.sc65[0])
        self.rotasiD2 = (self.td[1] * self.sc65[1]) + (self.td[1] * self.sc65[0])
        print("Nilai D setelah rotasi 65 derajat : ", "{:.2f}".format(self.rotasiD1),",","{:.2f}".format(self.rotasiD2))

    def Skala(self):
        print("SKALA")
        self.tipus = [6,2]
        self.skala = [2,3]
        self.atipus = [(self.rotasiA1 + self.tipus[0]), self.rotasiA2 + self.tipus[1]] #mencari titik a dari titik pusat 6,2
        self.askala = ['{:.2f}'.format(self.atipus[0] * self.skala[0]),'{:.2f}'.format(self.atipus[1] * self.skala[1])] #mencari skala dari a baru
        print(f"Titik A [{'{:.2f}'.format(self.rotasiA1)}, {'{:.2f}'.format(self.rotasiA2)}] dengan titik pusat {self.tipus} lalu diberi skala {self.skala} -> A {self.askala}")

        self.btipus = [self.rotasiB1 + self.tipus[0], self.rotasiB2 + self.tipus[1]] 
        self.bskala = ['{:.2f}'.format(self.btipus[0] * self.skala[0]),'{:.2f}'.format(self.btipus[1] * self.skala[1])] 
        print(f"Titik B [{'{:.2f}'.format(self.rotasiB1)}, {'{:.2f}'.format(self.rotasiB2)}] dengan titik pusat {self.tipus} lalu diberi skala {self.skala} -> A {self.bskala}")
        
        self.ctipus = [self.rotasiC1 + self.tipus[0], self.rotasiC2 + self.tipus[1]] 
        self.cskala = ['{:.2f}'.format(self.ctipus[0] * self.skala[0]),'{:.2f}'.format(self.ctipus[1] * self.skala[1])] 
        print(f"Titik C [{'{:.2f}'.format(self.rotasiC1)}, {'{:.2f}'.format(self.rotasiC2)}] dengan titik pusat {self.tipus} lalu diberi skala {self.skala} -> A {self.cskala}")

        self.dtipus = [self.rotasiD1 + self.tipus[0], self.rotasiD2 + self.tipus[1]] 
        self.dskala = ['{:.2f}'.format(self.dtipus[0] * self.skala[0]),'{:.2f}'.format(self.dtipus[1] * self.skala[1])] 
        print(f"Titik D [{'{:.2f}'.format(self.rotasiD1)}, {'{:.2f}'.format(self.rotasiD2)}] dengan titik pusat {self.tipus} lalu diberi skala {self.skala} -> A {self.dskala}")
        
t = tugas()
print("")
t.translasi()
print("")
t.rotasi()
print("")
t.Skala()