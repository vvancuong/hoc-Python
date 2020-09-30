from math import sqrt
def main():

    try:
        a, b, c = map(float, input("Nhap vao a, b, c: ").split(","))
        #tinh dien tich tam giac tai day
        # xu ly them: 2 canh bat ky lon hon canh con lai
        if (a + b > c and a + c > b and b + c > a):
            p = (a + b + c) / 2
            s = sqrt(p * (p - a) * (p - b) * (p - c))
            print("Dien tich tam giac: ", s)
        else:
            print("Khong la 3 canh tam giac")
    except:
        print("Du lieu nhap vao phai la so thuc !")
    finally:
        print("Ket thuc chuong trinh")

def test():
    pass

if __name__ == "__main__":
    main()