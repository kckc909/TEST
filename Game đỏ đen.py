import random


class MainCharacter:
    def __init__(self, n):
        self._name = n
        self._health = 20
        self._evasion = 25
        self._power = 5
        self._resistance = 5

    def information(self):
        print('-'*5 + 'Information of {}'.format(self._name) + '-' * 5)
        print('Health : ', self._health)
        print('Power : ', self._power)
        print('Evasion : ', self._evasion / 100)
        print('Resistance : ', self._resistance)
        print('-' * 39)

    def health(self):
        return self._health

    def evasion(self):
        return self._evasion

    def power(self):
        return self._power

    def resistance(self):
        return self._resistance

    def change_health(self, ind):
        self._health += ind

    # thay đổi giáp khi nhận hiểu ứng
    def change_resistance(self, ind):
        self._resistance += ind
        if self._resistance <= 1:
            self._resistance = 1

    def change_evasion(self, ind):
        self._evasion += ind

    def change_power(self, ind):
        self._power += ind
        if self._power <= 1:
            self._power = 1


class Monster:
    def __init__(self, health, resistance, power):
        self._health = health
        self._power = power
        self._evasion = 25
        self._resistance = resistance

    def information(self):
        print('-'*5 + 'Thông tin quái' + '-'*5)
        print('Health : ', self._health)
        print('Power : ', self._power)
        print('Evasion : ', self._evasion / 100)
        print('Resistance : ', self._resistance)
        print('-'*24)

    def health(self):
        return self._health

    def evasion(self):
        return self._evasion

    def power(self):
        return self._power

    def resistance(self):
        return self._resistance

    def change_health(self, ind):
        self._health += ind

    def change_resistance(self, ind):
        self._resistance += ind

    def change_evasion(self, ind):
        self._evasion += ind

    def change_power(self, ind):
        self._power += ind


def thongbao(ind, s):
    if ind < 0:
        print('Vật phẩm nguyền! Chỉ sổ {} giảm'.format(s))
    else:
        print('Vật phẩm ban ơn! Chỉ số {} tăng'.format(s))


def trumau(tancong, thu):
    a = tancong - thu
    if a <= 0:
        return 1
    else:
        return a


name = str(input('Tên nhân vật: '))
mc = MainCharacter(name)
vanmay = random.randint(1, 6)
mc.information()
print('Vận may của bạn là : ', vanmay)
diem = 0.0
luotboqua = int(vanmay)
cstt = 1
while mc.health() > 0:
    print('\n' + '='*30 + '\n')
    turn = str(input('Roll (R) - Xem chỉ số (S) - Dừng lại (D)')).upper()
    if turn == 'R':
        roll = random.randint(0, 9)
        if vanmay == roll:
            print('Level up!')
            print('Các chỉ số tăng !')
            mc.change_health(2)
            mc.change_power(2)
            mc.change_resistance(1)
            mc.information()
            diem += 1
        elif vanmay < roll:
            print('Bạn gặp phải quái vật!')
            h = random.randint(1 + cstt, 20 + cstt)
            re = random.randint(1 + cstt, 20 + cstt)
            p = random.randint(1 + cstt, 20 + cstt)
            ms = Monster(h, re, p)
            print('          Thông tin quái          ')
            ms.information()
            lua_chon = str(input('Đánh (Đ) hay bỏ chạy (B): ')).upper()
            while lua_chon != 'Đ' and lua_chon != 'B':
                lua_chon = str(input('Đánh (Đ) hay bỏ chạy (B): ')).upper()
            if luotboqua <= 0:
                print('Bạn đã hết lượt bỏ qua, không thể bỏ qua!')
                lua_chon = 'Đ'
            if lua_chon == 'Đ':
                exp = 0
                while ms.health() > 0 and mc.health() > 0:
                    mctancong = random.randint(1, 100)
                    mstancong = random.randint(1, 100)
                    if mctancong > ms.evasion():
                        tc_pt = trumau(mc.power(), ms.resistance())
                        ms.change_health(- tc_pt)
                        print('Bạn đánh quái trừ {} máu! '.format(tc_pt))
                    else:
                        print('Quái né!')
                    if mstancong > mc.evasion():
                        dn = trumau(ms.power(), mc.resistance())
                        mc.change_health(- dn)
                        print('Quái đánh bạn trừ {} máu! '.format(dn))
                    else:
                        print('Bạn né!')
                    exp += 1
                    if exp == 5:
                        mc.change_health(1)
                        mc.change_power(1)
                        mc.change_resistance(0.5)
                if mc.health() <= 0:
                    print('Bạn đã chết! ')
                    break
                print('Bạn đã tiêu diệt quái vật')
                print('Các chỉ số tăng!')
                mc.change_health(1)
                mc.change_power(1)
                mc.change_resistance(0.5)
                mc.information()
                diem += 2
            elif lua_chon == 'B' and luotboqua > 0:
                luotboqua -= 1
                print('Bạn đã bỏ chạy!')
                print('Quái vật đã mạnh lên!')
                print('Bạn còn {} lượt bỏ qua! '.format(luotboqua))
                cstt += 2
            cstt += 1
        elif vanmay > roll:
            print('Bạn tìm được vật phẩm!')
            diem += 1
            lua_chon = str(input('Có sử dụng hay không? (Y or N)\n')).upper()
            if lua_chon == 'Y':
                rd = random.randint(1, 3)
                index = random.randint(-5, 5)
                if rd == 1:
                    mc.change_health(index)
                    thongbao(index, "máu")
                elif rd == 2:
                    mc.change_power(index)
                    thongbao(index, 'sức mạnh')
                elif rd == 3:
                    mc.change_resistance(index)
                    thongbao(index, 'chống chịu')
            elif lua_chon == 'N':
                print('Bạn đã bỏ lại vật phẩm! ')
            mc.information()
    elif turn == "S":
        mc.information()
    elif turn == 'D':
        print('Bạn đã dừng cuộc chơi!')
        break
print('\n' + 39 * '=' + '\n')
print('Nhân vật {} đạt {} điểm!'.format(name, diem))
