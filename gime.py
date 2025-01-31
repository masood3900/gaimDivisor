import tkinter as tk
import pygame
import random

# مقداردهی اولیه pygame برای پخش صدا
pygame.mixer.init()

# تابع پخش موسیقی پس‌زمینه
def play_music(file_name, loop=-1):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(loop)

# تابع توقف موسیقی
def stop_music():
    pygame.mixer.music.stop()

# تابع پخش صدای درست یا نادرست
def play_sound(file_name):
    sound = pygame.mixer.Sound(file_name)
    sound.play()

# تابع بررسی پاسخ و تغییر رنگ دکمه‌ها
def check_number(selected_number, correct_number, button):
    global score
    if selected_number == correct_number:
        play_sound("correct.mp3")
        button.config(bg="green")
        score += 1
        result_label.config(text="✅ آفرین! درست گفتی!", fg="green")
    else:
        play_sound("wrong.mp3")
        button.config(bg="red")
        score -= 1
        result_label.config(text="❌ متاسفم، اشتباه گفتی!", fg="red")
    update_score()

# تابع برای به‌روزرسانی امتیاز
def update_score():
    score_label.config(text=f"امتیاز: {score}")

# تابع برای به‌روزرسانی زمان باقی‌مانده
def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"زمان باقی‌مانده: {time_left}s")
        # ادامه به‌روزرسانی پس از 1 ثانیه
        root.after(1000, update_timer)
    else:
        end_game()  # پایان بازی زمانی که زمان تمام شد

# تابع پایان بازی
def end_game():
    result_label.config(text=f"⏰ بازی تمام شد! امتیاز شما: {score}", fg="blue")
    stop_music()  # توقف موسیقی پس‌زمینه

# تابع شروع بازی
def start_game():
    global time_left, correct_number
    time_left = 30  # تنظیم زمان 30 ثانیه
    correct_number = random.randint(1,7)
    stop_music()  # توقف موسیقی معرفی
    intro_window.destroy()  # بستن صفحه معرفی
    main_game()  # اجرای بازی

# تابع اجرای بازی
def main_game():
    global result_label, score, time_left, correct_number, timer_label

    global root
    root = tk.Tk()
    root.title("بازی ریاضی کودکان")
    root.geometry("400x400")
    root.configure(bg="#ffecb3")  # پس‌زمینه نرم کودکانه

    # نمایش عدد بخش‌پذیر
    divisor_label = tk.Label(root, text=f"عدد بخش‌پذیر: {correct_number}", font=("Vazirmatn", 14), bg="#ffecb3")
    divisor_label.pack(pady=10)

    score = 0  # امتیاز شروع بازی
    time_left = 30  # زمان 30 ثانیه

    # فریم برای نمایش امتیاز و زمان
    top_frame = tk.Frame(root, bg="#ffecb3")
    top_frame.pack(pady=10)

    # نمایش امتیاز
    score_label = tk.Label(top_frame, text=f"امتیاز: {score}", font=("Vazirmatn", 12), bg="#ffecb3")
    score_label.pack(side="left", padx=20)

    # نمایش زمان باقی‌مانده
    timer_label = tk.Label(top_frame, text=f"زمان باقی‌مانده: {time_left}s", font=("Vazirmatn", 12), bg="#ffecb3")
    timer_label.pack(side="left", padx=20)

    # فریم برای نگه داشتن دکمه‌ها
    button_frame = tk.Frame(root, bg="#ffecb3")
    button_frame.pack(pady=10)

    # ایجاد لیست عددهای تصادفی
    numbers = random.sample(range(1, 11), 4)  # 4 عدد تصادفی بین 1 تا 10
    if correct_number not in numbers:
        numbers[random.randint(0, 3)] = correct_number  # اطمینان از وجود عدد درست

    buttons = []  # لیست برای ذخیره دکمه‌ها

    for num in numbers:
        btn = tk.Button(button_frame, text=str(num), font=("Vazirmatn", 14), width=5, height=2, bg="#ffcc80")
        btn.config(command=lambda n=num, b=btn: check_number(n, correct_number, b))  # ارسال دکمه درست
        btn.pack(side="left", padx=5)
        buttons.append(btn)  # ذخیره دکمه‌ها

    result_label = tk.Label(root, text="", font=("Vazirmatn", 12), bg="#ffecb3")
    result_label.pack(pady=10)

    # شروع تایمر
    root.after(1000, update_timer)

    btn_exit = tk.Button(root, text="❌ خروج", command=root.quit, font=("Vazirmatn", 12), bg="red", fg="white")
    btn_exit.pack(pady=20)

    root.mainloop()

# --- صفحه معرفی ---
intro_window = tk.Tk()
intro_window.title("معرفی بازی")
intro_window.geometry("470x450")
intro_window.configure(bg="#ffccff")  # پس‌زمینه صورتی کودکانه

# پخش موسیقی پس‌زمینه
play_music("intro.mp3")

title_label = tk.Label(intro_window, text="🎉 به بازی ریاضی ابتدایی قسمت بخش پذیری خوش آمدید! 🎉", font=("Vazirmatn", 14), fg="blue", bg="#ffccff")
title_label.pack(pady=20)

info_label = tk.Label(intro_window, text="🔹  عدد درست را انتخاب کن!\n🔹 امتیاز بگیر و لذت ببر!", font=("Vazirmatn", 12), bg="#ffccff")
info_label.pack(pady=20)
info_label = tk.Label(intro_window, text="تهیه کننده : حکیمه شریفی راد\nدبستان شهید بهشتی منطقه 17 تهران  ", font=("Vazirmatn", 12), bg="#ffccff")
info_label.pack(pady=20)
start_button = tk.Button(intro_window, text="🎮 شروع بازی", command=start_game, font=("Vazirmatn", 14), bg="green", fg="white")
start_button.pack(pady=20)
info_label = tk.Label(intro_window, text="ایجاد شده با زبان شیرین پایتون", font=("Vazirmatn", 12), bg="#ffccff")
info_label.pack(pady=20)


intro_window.mainloop()