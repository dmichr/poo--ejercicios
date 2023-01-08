class Empresa:
    def __init__(self,nom="Hospital Universitario",ruc="0405612984001",tel="0992255432",dir="Milagro"):
        self.nombre=nom
        self.ruc=ruc
        self.tel=tel
        self.dir=dir

if __name__ == '__main__':
    emp = Empresa()
    print("_"*25)
    print(emp.nombre)

