l = {}
class Royxat():
    
    def __init__(self, foydalanuvchi, familiya, parol):
        self.foydalanuvchi = foydalanuvchi
        self.familiya = familiya
        self.parol = parol
        if f'{self.foydalanuvchi}|{self.familiya}' in list(l.keys()):
            print('Siz allaqachon ro`yxatdan o`tgansiz, iltimos boshqa foydalanuvchi ismini kirting')
            print(l)
        else:
            l[f'{self.foydalanuvchi}|{self.familiya}'] = self.parol
            print("Ro`yxatdan muvaffaqiyatli o`tdingiz")

    def view(self):
        print("Parolni unutdingizmi? Unda")
        foydalanuvchi = input("Ismizni kiriting: ").capitalize()
        familiya = input("Familiyanguzni kiriting: ").capitalize()
        if f'{foydalanuvchi}|{familiya}' in list(l.keys()):
            print(l[f'{foydalanuvchi}|{familiya}'])
        else:
            print("Siz ro`yxatdan o`tmagansiz")

    def signin(self):
        ism = input("Ismni kiriting: ").capitalize()
        familiya = input("Familiyani kiriting: ").capitalize()
        parol = int(input("Parolni kiriting: "))
        if f'{ism}|{familiya}' in list(l.keys()):
            if parol == l[f'{ism}|{familiya}']:
                print("Ishchi oynaga xush kelibsiz")
            else:
                s.view()
        else:
            print("Bunday foydalanuvchi ro'yxatdan o'tmagan")

s = Royxat(foydalanuvchi = 'Maqsadbek', familiya = 'Ibrohimjonov', parol = 123456)
s.signin()

