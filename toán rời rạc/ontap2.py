def kiemtranuocsoi(nhietdo):
    print("Kiểm tra:", nhietdo)
    if nhietdo < 0 or nhietdo > 120:
        print("Nhiệt độ bất thường!")
    elif nhietdo <= 50:
        print("Xử lý nước lạnh")
        print("Nước chưa sôi")
    elif 70 <= nhietdo <= 100:
        print("Nước nóng nhưng chưa sôi")
        print("Nước chưa sôi")
    elif nhietdo == 100:
        print("Nước vừa sôi")
    elif nhietdo > 100:
        print("Nước đang sôi mạnh")
    else:
        print("Nước ấm")
        print("Nước chưa sôi")
kiemtranuocsoi(45)
kiemtranuocsoi(85)
kiemtranuocsoi(100)
kiemtranuocsoi(105)
kiemtranuocsoi(-10)
kiemtranuocsoi(130)
