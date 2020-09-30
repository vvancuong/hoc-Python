# kiểm tra, thực thi module
import extra.about as ab
import modules.module1 as m1
import modules.module2 as m2

#print("HELO")

while(1 == 1):
    n = input("nhap lua chon:")
    print("ma  n:", n)
    if (n == "1"):
        m1.inChuoiVietHoa()
    if (n == "2"):
        m1.inThuTrongTuan()
    if (n == "3"):
        m2.soLonNhat()
    if (n == "4"):
        m2.dangChuSo()
    if (n == "0"):
        print("thoat")
        break
