def main():
    # sử dụng hàm open()
    # cú pháp open('path','tham số')
    f = open("result.txt", 'a+')
    # a+: tao ra file neu không có 
    f.write("Thử ghi thêm nội dung mới")
    f.close()

if __name__ == '__main__':
    main()