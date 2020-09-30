# in ra số lớn nhất
# nhập vào 1 số < 1000 : in ra dạng chứ số ( 300 -> ba trăm)

def soLonNhat():
    z = list(map(int, input("Nhập vào dãy số: ").split(",")))
    max = z[0]
    for i in z:
        if i > max:
            max = i
    print("Số lớn nhất là: ", max)


def dangChuSo(a):
    a= int(input("nhập vào 1 số từ 1-> 1000: "))
    hangtram = a / 100
    hangchuc = ((a / 10) % 10)
    hangdonvi = a % 10
    
    hangtram = {
        1: "Một trăm",
        2: "Hai trăm",
        3: "Ba trăm",
        4: "Bốn trăm",
        5: "Năm trăm",
        6: "Sáu trăm",
        7: "Bảy trăm",
        8: "Tám trăm",
        9:"Chín trăm"
        
    }
    return hangtram.get(a, "nothing")
    

