# Generate data for TRUONGHOC1

import random
from mysql.connector import connect
from mysql.connector import Error
import time

# Connect to database `TRUONGHOC1`
try:
    passwd = input("Enter mySQL password: ")
    connection = connect(
        host='localhost', 
        user='root',  
        password=passwd,
        database="truonghoc1"
    ) 
    if connection.is_connected():
        cursor = connection.cursor()
        print("Connected to database (`TRUONGHOC1`).\n")
        
except Error as e:
    print("Error while connecting to MySQL. ", e)
    exit()

# Store the start time of this program
start_time = time.time()

### PREPARE DATA TO RANDOM INFORMATION ###

# Constants 
MIN_MATR = 1785001              # The minimum number of MATR
MAX_MATR = 1785100              # The maximum number of MATR
MIN_MAHS = 70000001             # The minimum number of MAHS
MAX_MAHS = 71000000             # The maximum number of MAHS
MIN_CCCD = 123456789123         # The minimum number of CCCD
MAX_CCCD = 987654321987         # The maximum number of CCCD
MIN_BIRTHDAY = "2000-01-01"     # The minimum time of birthday 
MAX_BIRTHDAY = "2007-12-31"     # The maximum time of birthday
TIME_FORMAT = '%Y-%m-%d'        # The format of date

# The set of unique CCCD numbers
# The values of the set are between MIN_CCCD and MAX_CCCD
# The size of set is the number of student  
set_of_cccd = random.sample(range(MIN_CCCD, MAX_CCCD + 1), MAX_MAHS - MIN_MAHS + 1)

# The list of last name
last_name = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Đặng", "Đỗ", "Ngô", "Hồ", "Dương", "Đinh", "Ái", "An", "Anh", "Ao", "Ánh", "Ân", "Âu", "Âu Dương", "Ấu", "Bá", "Bạc", "Bạch", "Bàn", "Bàng", "Bành", "Bảo", "Bế", "Bì", "Biện", "Bình", "Bồ", "Chriêng", "Ca", "Cà", "Cái", "Cai", "Cam", "Cảnh", "Cao", "Cáp", "Cát", "Cầm", "Cấn", "Chế", "Chiêm", "Chu", "Chắng", "Chung", "Chúng", "Chương", "Chử", "Cồ", "Cổ", "Công", "Cống", "Cung", "Cù", "Cự", "Dã", "Danh", "Diêm", "Diệp", "Doãn", "Du", "Duy", "Dư", "Đan", "Đàm", "Đào", "Đăng", "Đắc", "Đầu", "Đậu", "Đèo", "Điêu", "Điền", "Điều", "Đinh", "Đình", "Đoái", "Đoàn", "Đoạn", "Đôn", "Đống", "Đồ", "Đồng", "Đổng", "Đới", "Đương", "Đường", "Đức", "Giả", "Giao", "Giang", "Giàng", "Giản", "Giảng", "Giáp", "Hưng", "Hầu", "Hà", "Hạ", "Hàn", "Hàng", "Hán", "Hề", "Hi", "Hình", "Hoa", "Hoà", "Hoài", "Hoàng Phủ", "Hồng", "Hùng", "Hứa", "Hướng", "Kinh", "Kiểu", "Kha", "Khà", "Khai", "Khâu", "Khiếu", "Khoa", "Khổng", "Khuất", "Khúc", "Khương", "Khưu", "Kiều", "Kim", "Ly", "Lý", "La", "Lã", "Lành", "Lãnh", "Lạc", "Lại", "Lăng", "Lâm", "Lầu", "Lèng", "Lều", "Liên", "Liệp", "Liêu", "Liễu", "Linh", "Loan", "Lò", "Lô", "Lỗ", "Lộ", "Lộc", "Luyện", "Lục", "Lù", "Lư", "Lương", "Lường", "Lưu", "Ma", "Mai", "Man", "Mang", "Mã", "Mạc", "Mạch", "Mạnh", "Mâu", "Mầu", "Mẫn", "Minh", "Mộc", "Mông", "Mùa", "Mục", "Miêu", "Niê", "Ngạc", "Ngân", "Nghiêm", "Nghị", "Ngọ", "Ngọc", "Ngôn", "Ngũ", "Ngụy", "Nhan", "Nhâm", "Nhữ", "Ninh", "Nông", "Ong", "Ô", "Ông", "Phi", "Phí", "Phó", "Phong", "Phù", "Phú", "Phùng", "Phương", "Quản", "Quán", "Quang", "Quàng", "Quảng", "Quách", "Quế", "Quốc", "Quyền", "Sái", "Sâm", "Sầm", "Sơn", "Sử", "Sùng", "Sỳ", "Tán", "Tào", "Tạ", "Tăng", "Tấn", "Tất", "Tề", "Thang", "Thanh", "Thái", "Thành", "Thào", "Thạch", "Thân", "Thẩm", "Thập", "Thế", "Thi", "Thiều", "Thiệu", "Thịnh", "Thiềm", "Thoa", "Thôi", "Thóng", "Thục", "Tiêu", "Tiết", "Tiếp", "Tinh", "Tòng", "Tô", "Tôn", "Tôn Nữ", "Tôn Thất", "Tông", "Tống", "Trang", "Tráng", "Trác", "Trà", "Trâu", "Tri", "Trì", "Triệu", "Trình", "Trịnh", "Trung", "Trưng", "Tuấn", "Từ", "Tưởng", "Tướng", "Ty", "Uông", "Uân", "Ung", "Ưng", "Ứng", "Vàng", "Vâng", "Vạn", "Văn", "Văng", "Vi", "Vĩnh", "Viêm", "Viên", "Việt", "Vòng", "Vừ", "Vương", "Vưu", "Vu", "Xa", "Xung", "Y", "Yên"]

# The list of first name
first_name = ["Huy", "Khang", "Bảo", "Minh", "Phúc", "Anh", "Khoa", "Phát", "Đạt", "Khôi", "Long", "Nam", "Duy", "Quân", "Kiệt", "Thịnh", "Tuấn", "Hưng", "Hoàng", "Hiếu", "Nhân", "Trí", "Tài", "Phong", "Nguyên", "An", "Phú", "Thành", "Đức", "Dũng", "Lộc", "Khánh", "Vinh", "Tiến", "Nghĩa", "Thiện", "Hào", "Hải", "Đăng", "Quang", "Lâm", "Nhật", "Trung", "Thắng", "Tú", "Hùng", "Tâm", "Sang", "Sơn", "Thái", "Cường", "Vũ", "Toàn", "Ân", "Thuận", "Bình", "Trường", "Danh", "Kiên", "Phước", "Thiên", "Tân", "Việt", "Khải", "Tín", "Dương", "Tùng", "Quý", "Hậu", "Trọng", "Triết", "Luân", "Phương", "Quốc", "Thông", "Khiêm", "Hòa", "Thanh", "Tường", "Kha", "Vỹ", "Bách", "Khanh", "Mạnh", "Lợi", "Đại", "Hiệp", "Đông", "Nhựt", "Giang", "Kỳ", "Phi", "Tấn", "Văn", "Vương", "Công", "Hiển", "Linh", "Ngọc", "Vĩ", "Anh", "Vy", "Ngọc", "Nhi", "Hân", "Thư", "Linh", "Như", "Ngân", "Phương", "Thảo", "My", "Trân", "Quỳnh", "Nghi", "Trang", "Trâm", "An", "Thy", "Châu", "Trúc", "Uyên", "Yến", "Ý", "Tiên", "Mai", "Hà", "Vân", "Nguyên", "Hương", "Quyên", "Duyên", "Kim", "Trinh", "Thanh", "Tuyền", "Hằng", "Dương", "Chi", "Giang", "Tâm", "Lam", "Tú", "Ánh", "Hiền", "Khánh", "Minh", "Huyền", "Thùy", "Vi", "Ly", "Dung", "Nhung", "Phúc", "Lan", "Phụng", "Ân", "Thi", "Khanh", "Kỳ", "Nga", "Tường", "Thúy", "Mỹ", "Hoa", "Tuyết", "Lâm", "Thủy", "Đan", "Hạnh", "Xuân", "Oanh", "Mẫn", "Khuê", "Diệp", "Thương", "Nhiên", "Băng", "Hồng", "Bình", "Loan", "Thơ", "Phượng", "Mi", "Nhã", "Nguyệt", "Bích", "Đào", "Diễm", "Kiều", "Hiếu", "Di", "Liên", "Trà", "Tuệ", "Thắm", "Diệu", "Quân", "Nhàn", "Doanh"]

# The list of school's name
school = ["Trường THPT Nguyễn Trường Tộ", "Trường THPT Lưu Trung Kiên", "Trường THPT Trần Nguyên Hãn", "Trường THPT Đinh Tiên Hoàng", "Trường THPT Chuyên Lê Quý Đôn", "Trường THPT Nguyễn Huệ", "Trường THPT Lê Hồng Phong", "Trường THPT Nguyễn Thị Minh Khai", "Trường THPT Châu Thành", "Trường THPT Nguyễn Bỉnh Khiêm", "Trường THPT DL Chu Văn An", "Trường THPT Xuyên Mộc", "Trường THPT Phước Bửu", "Trường THPT Hòa Bình", "Trường THPT Hoà Hội", "Trường THPT Bưng Riềng", "Trường THPT Trần Văn Quan", "Trường THPT Long Hải - Phước tỉnh", "Trường THPT Trần Quang Khải", "Trường THPT Dương Bạch Mai", "Trường THPT Minh Đạm", "Trường THPT Hắc Dịch", "Trường THPT Trần Hưng Đạo", "Trường THPT Nguyễn Du", "Trường THPT Nguyễn Trãi", "Trường THPT Ngô Quyền", "Trường THPT Trần Phú", "Trường THPT Nguyễn Văn Cừ", "Trường THPT Võ Thị Sáu", "Trường THPT Nguyễn Huệ", "Trường THPT Dân tộc nội trú tỉnh", "Trường THPT Chuyên Lương Văn Chánh", "Trường THPT Ngô Gia Tự", "Trường THPT Nguyễn Trãi", "Trường THPT Nguyễn Trường Tộ", "Trường THPT DL Nguyễn Bỉnh Khiêm", "Trường THPT Lê Lợi", "Trường THPT Nguyễn Thái Bình", "Trường THPT Phan Đình Phùng", "Trường THPT Lê Thành Phương", "Trường THPT Trần Phú", "Trường THPT Phan Bội Châu", "Trường THPT Nguyễn Du", "Trường THPT Tôn Đức Thắng", "Trường THPT Lê Trung Kiên", "Trường THPT Nguyễn Công Trứ", "Trường THPT DL Lê Thánh Tôn", "Trường THPT Nguyễn Văn Linh", "Trường THPT Trần Quốc Tuấn", "Trường THPT Trần Bình Trọng", "Trường THPT Trần Suyền", "Trường THPT Lê Hồng Phong", "Trường THPT Phạm Văn Đồng", "Trường THPT Nguyễn Thị Minh Khai", "Trường THPT Trần Phú", "Trường THPT Chuyên Vĩnh Phúc", "Trường THPT Liên Bảo", "Trường THPT Vĩnh Yên", "Trường THPT DTNT Tỉnh", "Trường THPT Nguyễn Thái Học", "Trường THPT Tam Dương", "Trường THPT Trần Hưng Đạo", "Trường THPT Tam Dương 2", "Trường THPT Ngô Gia Tự", "Trường THPT Liễn Sơn", "Trường THPT Trần Nguyên Hãn", "Trường THPT Triệu Thái", "Trường THPT Thái Hoà", "Trường THPT Văn Quán", "Trường THPT Lê Xoay", "Trường THPT Nguyễn Viết Xuân", "Trường THPT Đội Cấn", "Trường THPT Vĩnh Tường", "Trường THPT Nguyễn Thị Giang", "Trường THPT Hồ Xuân Hương", "Trường THPT Yên Lạc", "Trường THPT Yên Lạc 2", "Trường THPT Phạm Công Bình", "Trường THPT Đồng Đậu", "Trường THPT Ngô Quyền", "Trường THPT Tân Phong", "Trường THPT Lê Thánh Tôn", "Trường THPT Nguyễn Văn Linh", "Trường THPT Lương Văn Can", "Trường THPT Ngô Gia Tự", "Trường THPT Tạ Quang Bửu", "Trường THPT Võ Văn Kiệt", "Trường THPT Năng khiếu TDTT Nguyễn Thị Định", "Trường THPT Phước Long", "Trường THPT Long Trường", "Trường THPT Nguyễn Huệ", "Trường THPT Nguyễn Văn Tăng", "Trường THPT Nguyễn An Ninh", "Trường THPT Nguyễn Khuyến", "Trường THPT Nguyễn Du", "Trường THPT Sương Nguyệt Anh", "Trường THPT Diên Hồng", "Trường THPT Nguyễn Hiền", "Trường THPT Nam Kỳ Khởi Nghĩa", "Trường THPT Trần Quang Khải"]

# The list of province
province = ["Tỉnh Bà Rịa-Vũng Tàu", "Tỉnh Hòa Bình", "Tỉnh Ninh Thuận"]

# The list of district
district = []

# Create a list of district for each province
for i in range (len(province)):
    district.append([])
    
# Append the districts or cities of Ba Ria-Vung Tau province
district[0].append("Thành phố Vũng Tàu")
district[0].append("Thành phố Bà Rịa")
district[0].append("Thị xã Phú Mỹ")
district[0].append("Huyện Châu Đức")
district[0].append("Huyện Côn Đảo")
district[0].append("Huyện Đất Đỏ")
district[0].append("Huyện Long Điền")
district[0].append("Huyện Xuyên Mộc")

# Append the districts or cities of Hoa Binh province
district[1].append("Thành phố Hòa Bình")
district[1].append("Huyện Lương Sơn")
district[1].append("Huyện Cao Phong")
district[1].append("Huyện Đà Bắc")
district[1].append("Huyện Kim Bôi")
district[1].append("Huyện Kỳ Sơn")
district[1].append("Huyện Lạc Sơn")
district[1].append("Huyện Lạc Thủy")
district[1].append("Huyện Mai Châu")
district[1].append("Huyện Tân Lạc")
district[1].append("Huyện Yên Thủy")

# Append the districts or cities of Ninh Thuan province
district[2].append("Thị xã Phan Rang - Tháp Chàm")
district[2].append("Huyện Ninh Sơn")
district[2].append("Huyện Ninh Hải")
district[2].append("Huyện Ninh Phước")

# The list of school's address
address_of_school = []

# The list of the school of students
school_of_student = []

# The list of student's birthday
birthday_of_student = []

# Create a new last name
# Return a string
def new_last_name():
    return last_name[random.randrange(0, len(last_name))]
    
# Create a new first name
# A first name is combined by two first names in the list of those
# Return a string
def new_first_name():
    return first_name[random.randrange(0, len(first_name))] + " " + first_name[random.randrange(0, len(first_name))]

# Create a new address
# A address includes information about the district and the province 
# Return a string
def new_address():
    new_province = random.randrange(0, len(province))
    new_district = random.randrange(0, len(district[new_province]))
    return district[new_province][new_district] + ", " + province[new_province]

# Get CCCD of the index-th student from the created set of CCCD 
# Return a string
def new_cccd(index):
    return str(set_of_cccd[index])

# Random a birthday between MIN_BIRTHDAY and MAX_BIRTHDAY
# Return a string which has TIME_FORMAT : YYYY-MM-DD
def new_birthday():
    stime = time.mktime(time.strptime(MIN_BIRTHDAY, TIME_FORMAT))
    etime = time.mktime(time.strptime(MAX_BIRTHDAY, TIME_FORMAT))
    ptime = stime + random.random() * (etime - stime)
    return time.strftime(TIME_FORMAT, time.localtime(ptime))

# Get a rank of the specific score
# Return a string which is the rank of this score
def get_rank(score):
    if score >= 9:
        return "Xuất sắc"
    elif score >= 8:
        return "Giỏi"
    elif score >= 6.5:
        return "Khá"
    elif score >= 5:
        return "Trung Bình"
    else: 
        return "Yếu"
           
# Get the result of the specific score
# Return a string which is the result of this score (this rank)
def get_result(score):
    rank = get_rank(score)
    return "Hoàn thành" if rank != "Yếu" else "Chưa hoàn thành"

# Generate data for table `TRUONG`
def generate_data_for_table_TRUONG():
    
    # This program generates 100 instances for table `TRUONG`
    
    print(f"Create {MAX_MATR - MIN_MATR + 1} instances...")
    
    for i in range(0, MAX_MATR - MIN_MATR + 1):
        address_of_school.append(new_address())
        new_instance = f"INSERT INTO `TRUONG` VALUES ('{str(i + MIN_MATR)}', '{school[i]}', '{address_of_school[i]}')"
        cursor.execute(new_instance)   

    print(f"Completed creating {MAX_MATR - MIN_MATR + 1} instances.")
    

# Generate data for table `HS`
def generate_data_for_table_HS():
    
    # This program generates 1.000.000 instances for table `HS`
    
    print(f"Create {MAX_MAHS - MIN_MAHS + 1} instances...")
    
    for i in range (0, MAX_MAHS - MIN_MAHS + 1):
        school_of_student.append(random.randrange(0, len(school)))
        birthday_of_student.append(new_birthday())
        new_instance = f"INSERT INTO `HS` VALUES ('{str(i + MIN_MAHS)}', '{new_last_name()}', '{new_first_name()}', '{new_cccd(i)}', '{birthday_of_student[i]}', '{address_of_school[school_of_student[i]]}')"
        cursor.execute(new_instance)
            
    print(f"Completed creating {MAX_MAHS - MIN_MAHS + 1} instances.")

# Generate data for table `HOC`
def generate_data_for_table_HOC():
    
    print("Create the instances for the table `HOC`...")
    
    count_instance_hoc = 0
    
    for i in range (0, MAX_MAHS - MIN_MAHS + 1):
        
        birthday = int(birthday_of_student[i][:4])
        
        school_year = 3
        
        if birthday == 2007:
            school_year = 1
        elif birthday == 2008:
            school_year = 2
        
        for j in range (school_year):
            score = round(random.uniform(4, 10), 2)
            new_instance = f"INSERT INTO `HOC` VALUES ('{str(MIN_MATR + school_of_student[i])}', '{str(MIN_MAHS + i)}', '{str(birthday + j + 15) + '-' + str(birthday + j + 16)}', {score}, '{get_rank(score)}', '{get_result(score)}')"
            cursor.execute(new_instance)
            count_instance_hoc += 1
        
    print(f"Completed creating {count_instance_hoc} instances.")

# Start to generate data

print("Start to generate table TRUONG...")
generate_data_for_table_TRUONG()
print("Completed generating table TRUONG!!!\n")

print("Start to generate table HS...")
generate_data_for_table_HS()
print("Completed generating table HS!!!\n")

print("Start to generate table HOC...")
generate_data_for_table_HOC()
print("Completed generating table HOC!!!\n")

connection.commit()

print("Done.")

# Store the end time of this program
end_time = time.time()

# Calculate execution time in minutes

execution_time = (end_time - start_time) / 60

print(f"Execution time is {execution_time} minutes.")