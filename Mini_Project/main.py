import modules.maytinh as m
# print("Hello")


def main():
    print("---Chọn phép tính---")
    print("---[1]: phép cộng")
    print("---[2]: phép trừ")
    print("---[3]: phép nhân")
    print("---[4]: phép chia")
    print("---[5]: thoát chương trình")

    a = input("nhập a = ")
    b = input("nhập b = ")

    while(1 == 1):
        n = input("nhập lựa chọn :")
        
        if (n == "1"):
            m.cong(a, b)
        if (n == "2"):
            m.tru(a, b)
        if (n == "3"):
            m.nhan(a, b)
        if (n == "4"):
            m.chia(a, b)
        if (n == "5"):
            print("Thoát chương trình")
            break
            


if __name__ == '__main__':
    main()

