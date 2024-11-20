import time
import matplotlib.pyplot as plt

def fibonacci(n):    
    if n <= 0:
        raise ValueError("Số phải là số nguyên dương.")    
    sequence = [0, 1]
    
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2]) 
           
    return sequence[:n] if n > 1 else sequence[:1]

def fibonacci_program():   
    password = "DH23HM"
    max_attempts = 3    
    for attempt in range(max_attempts):
        matkhau = input(f"Lần thử {attempt + 1}/{max_attempts} - Nhập mật khẩu để vào chương trình: ")
                
        if matkhau.strip() == password:
            print("Đăng nhập thành công!")  
                      
            for i in iter(int, 1):  
                try:
                    n_input = input("Nhập số phần tử Fibonacci cần tính (hoặc 'end_Fibo' để thoát): ")                    
                    if n_input.strip().lower() == "end_fibo":
                        print("Đang thoát chương trình...")
                        break 
                    
                    n = int(n_input)
                    if n <= 0:
                        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
                        continue
                    
                    sequence = fibonacci(n)
                    print(f"Chuỗi Fibonacci ({n} phần tử): {sequence}")
                    plot_fibonacci(sequence)                                       
                    continue_input = input("Bạn có muốn thoát chương trình không? Nhập 'end_Fibo' để thoát hoặc nhấn Enter để tiếp tục: ").strip().lower()
                    time.sleep(3) 
                     
                    if continue_input == "end_fibo":
                        print("Đang thoát chương trình...")
                        break     
                               
                except ValueError:
                    print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên dương.")           
            return         
       
        else:
            print("Sai mật khẩu.")
            if attempt < max_attempts - 1:
                print("Vui lòng thử lại.")   
    print("Bạn đã nhập sai quá nhiều lần. Thoát chương trình...")

def plot_fibonacci(sequence):
    if not sequence:
        print("Chuỗi rỗng, không thể vẽ biểu đồ.")
        return
    
    try:
        # Biểu đồ Line chart
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(sequence, marker='o', linestyle='-', color='b')
        plt.title("Biểu đồ Fibonacci - Line Chart")
        plt.xlabel("Chỉ số")
        plt.ylabel("Giá trị")
        
        # Biểu đồ Pie chart
        plt.subplot(1, 2, 2)
        plt.pie(sequence, labels=range(1, len(sequence) + 1), autopct='%1.1f%%', startangle=140)
        plt.title("Biểu đồ chuỗi Fibonacci - Pie Chart")
        
        # Hiển thị biểu đồ
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        print(f"Lỗi khi hiển thị biểu đồ: {e}")
        print("Lưu biểu đồ dưới dạng hình ảnh 'fibonacci_plot.png'.")
        plt.savefig("fibonacci_plot.png")

fibonacci_program()
