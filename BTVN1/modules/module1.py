# nhập vào chuỗi ký tự -> in ra chuoix viết Hoa
# nhập vào số 2-8: in ra thứ trong tuần ( thứ Hai)

def inChuoiVietHoa():
    x = str(input("Mời bạn nhập chuỗi ký tự thường : "))
    return x.upper()

def inThuTrongTuan():
    y = int(input("Mời bạn nhập vào số 2 -> 8: "))
    if y < 2 and y > 8:
        print("Mờibạnnhậplại ! ")
    else:
        if y == 2:
            print("Thứ Hai")
        elif y == 3:
            print("Thứ Ba")
        elif y == 4:
            print("Thứ Tư")
        elif y == 5:
            print("Thứ Năm")
        elif y == 6:
            print("Thứ Sáu")
        elif y == 7:
            print("Thứ Bảy")
        print("Chủ Nhật")
    




