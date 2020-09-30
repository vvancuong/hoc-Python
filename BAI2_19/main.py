import modules.maytinh as m
def main():
    try:
        a, b = map(float, input("Nhap vao 2 só a,b : ").split(","))
        # tnhs phép chia tại đây
        print(m.chia(a, b))
        
    except:
        print("a,b phai la so thuc")
    finally:
        print("Ket thuc chuong trinh")



if __name__ == '__main__':
    main()
