#1
def tinh_tien_taxi(x):
    if x <= 1:
        t = 15000
    elif x <= 5:
        t = 15000 + (x - 1) * 13500
    else:
        t = 15000 + 4 * 13500 + (x - 5) * 11000
 
    if x > 120:
        t = t * 0.9
 
    return t
 
x = float(input("Nhap so km đi đuoc x: "))
t = tinh_tien_taxi(x)
print("Tien taxi t phai tra la: ", t)
#2
import math
 
def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b / (2*a)
        return "Phuong trinh co nghiem kep x1 = x2 = " + str(x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return "Phuong trinh co 2 nghiem phan biet x1 = " + str(x1) + " và x2 = " + str(x2)
 
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
ket_qua = giai_phuong_trinh_bac_2(a, b, c)
print(ket_qua)
#4
def kiem_tra_nam_nhuan(t):
    if (t % 4 == 0) and (t % 100 != 0 or t % 400 == 0):
        return "Nam " + str(t) + " là nam nhuan"
    else:
        return "Nam " + str(t) + " khong phai la nam nhuan"
 
t = int(input("Nhap nam t :"))
print(kiem_tra_nam_nhuan(t))
#5
def xep_loai_hoc_sinh(DTB):
    if DTB >= 9.0:
        return "Xuat sac"
    elif DTB >= 8.0:
        return "Gioi"
    elif DTB >= 6.5:
        return "Kha"
    elif DTB >= 5.0:
        return "Trung binh"
    elif DTB >= 3.5:
        return "Yeu"
    else:
        return "Kem"
 
DTB = float(input("Nhap diem trung binh ĐTB: "))
xep_loai = xep_loai_hoc_sinh(DTB)
print("Xep loai hoc sinh: ", xep_loai)
#6
def doi_tien(t):
    t_500 = t // 500000
    t = t % 500000
    t_200 = t // 200000
    t = t % 200000
    t_100 = t // 100000
    t = t % 100000
    t_50 = t // 50000
    return t_500, t_200, t_100, t_50
 
t = int(input("Nhap so tien t: "))
t_500, t_200, t_100, t_50 = doi_tien(t)
print("So tien tuong ung: ", t_500, "to 500.000, ", t_200, "to 200.000, ", t_100, "to 100.000, ", t_50, "tờ 50.000")
