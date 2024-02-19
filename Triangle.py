import tkinter as tk

def calculate_triangle_type():
  # รับค่าความยาวด้านจาก Entry widget
  side_a = float(entry_side1.get())
  side_b = float(entry_side2.get())
  side_c = float(entry_side3.get())

  # คำนวณประเภทสามเหลี่ยม
  triangle_type = " Not a triangle"
  if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a == side_b and side_b == side_c:
      triangle_type = " Equilateral triangle"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
      triangle_type = " Isosceles triangle"
    else:
      triangle_type = " Scalene triangle"

  # แสดงผลลัพธ์ใน Entry widget
  entry_result.delete(0, tk.END)
  entry_result.insert(40, triangle_type)


# กำหนดขนาดหน้าต่างและสีพื้นหลัง
root = tk.Tk()
root.geometry("490x320")
root.configure(bg='#D6D7EC')

# กำหนดชื่อโปรแกรม
root.title("Triangle")

# สร้าง Label สำหรับข้อความ "Enter the length of sides"
label_title = tk.Label(text="Enter the length of sides", font=("Arial", 20), bg='#D6D7EC')
label_title.pack(pady=20)
label_title.place(x=20,y=20)

# สร้าง Label สำหรับ "Side 1"
label_side1 = tk.Label(text="Side 1", font=("Arial", 20), bg='#D6D7EC')
label_side1.place(x=20, y=60)

# สร้าง Entry widget สำหรับรับค่า Side 1
entry_side1 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side1.place(x=160, y=65)

#---------------------------------------------------------------------------------#

# สร้าง Label สำหรับ "Side 2"
label_side2 = tk.Label(text="Side 2", font=("Arial", 20), bg='#D6D7EC')
label_side2.place(x=20, y=100)

# สร้าง Entry widget สำหรับรับค่า Side 2
entry_side2 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side2.place(x=160, y=105)

#---------------------------------------------------------------------------------#

# สร้าง Label สำหรับ "Side 3"
label_side3 = tk.Label(text="Side 3", font=("Arial", 20), bg='#D6D7EC')
label_side3.place(x=20, y=140)

# สร้าง Entry widget สำหรับรับค่า Side 3
entry_side3 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side3.place(x=160, y=145)

#---------------------------------------------------------------------------------#

# สร้าง Label สำหรับแสดงผลลัพธ์
label_result = tk.Label(text="Result", font=("Arial", 20), bg='#D6D7EC')
label_result.place(x=265, y=200)

# สร้างปุ่มสำหรับคำนวณ
button_calculate = tk.Button(text="Enter", font=("Arial", 17), bg='#CDCC03', command = calculate_triangle_type)
button_calculate.place(x=20, y=250)

# สร้าง Entry widget สำหรับแสดงชนิดของสามเหลี่ยม
entry_result = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_result.place(x=160, y=260)

# รันโปรแกรม
root.mainloop()
