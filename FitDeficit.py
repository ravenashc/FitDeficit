import tkinter as tk

# LOGIC

# FEEDBACK MESSAGE
def show_error(message):
    lbl_error_feedback.config(text=message, fg="red")

def show_success(message):
    lbl_error_feedback.config(text=message, fg="green")

# CALCULATE BUTTON CALLBACK
def calculate_deficit():
    
    # Read and clean user inputs
    name = name_entry.get().strip()
    sex = sex_entry.get().strip().upper()
    age_text = age_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()
    activity = activity_entry.get().strip().upper()

    # Required fields
    if name == "" or sex == "" or age_text == "" or weight_text == "" \
            or height_text == "" or activity == "":
        show_error("Please fill in all fields.")
        return
    
    # Data type (age, weight, height must be numbers)
    try:
        age = int(age_text)
        weight = float(weight_text)
        height = float(height_text)
    except ValueError:
        show_error("Age, weight, and height must be numbers.")
        return
    
    # Input ranges
    if age < 15 or age > 100:
        show_error("Age must be between 15 and 100.")
        return
    if weight < 30 or weight > 300:
        show_error("Weight must be between 30 and 300 kg.")
        return
    if height < 100 or height > 250:
        show_error("Height must be between 100 and 250 cm.")
        return
    
    # Categories
    if sex != "M" and sex != "F":
        show_error("Sex must be M or F.")
        return
    if activity != "LIGHT" and activity != "MODERATE" and activity != "HEAVY":
        show_error("Activity input must be light, moderate, or heavy.")
        return
    
    # Calculation (Mifflin-St Jeor BMR)
    if sex == "M":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
 
    # Total Daily Energy Expenditure = BMR x activity multiplier
    if activity == "LIGHT":
        tdee = bmr * 1.375
    elif activity == "MODERATE":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.725
        
    # Deficit calculation (safe deficit 500 kcal per day)
    daily = round(tdee - 500)
    weekly = daily * 7
 
    # Update output widgets
    lbl_out_name.config(text=name + "'s Daily Calorie Limit")
    lbl_out_daily.config(text="Calories per Day: " + str(daily) + " kcal")
    lbl_out_weekly.config(text="Calories per Week: " + str(weekly) + " kcal")
 
    # History log (state="disabled" by default)
    # 1: Unlock text box so changes are allowed
    text_history.config(state="normal")
    # 2: Insert the new log entry at the very bottom (tk.END)
    text_history.insert(tk.END, name + ": " + str(daily) + " kcal/day, "
                    + str(weekly) + " kcal/week\n")
    # 3: Relock text box immediately
    text_history.config(state="disabled")
 
    # Feedback
    if daily < 1200:
        lbl_error_feedback.config(
            text="Warning: limit is below 1200 kcal/day. Consult a professional.",
            fg="orange")
    else:
        show_success("Calculation successful!")

# RESET BUTTON CALLBACK
def reset_application():
    name_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
 
    lbl_out_name.config(text="Your Daily Calorie Limit")
    lbl_out_daily.config(text="Calories per Day: ")
    lbl_out_weekly.config(text="Calories per Week: ")
 
    lbl_error_feedback.config(text="Welcome! Enter your information to get started.",
                              fg="black")
    # none for text_history alone because it's a history tracker
 
 
# Event so that when user press Enter, it would trigger calculate_deficit function
def press_enter(event):
    calculate_deficit()


# MAIN WINDOW
window = tk.Tk()
window.title("Calorie Tracker")
window.geometry("480x720")

lbl_title = tk.Label(window, text="FitDeficit: Engineering \nCalorie Architecture",
    font=('Arial', 18, 'bold'))
lbl_title.pack(pady=(5, 0))

# FEEDBACK LABEL (errors = red, success = green)
lbl_error_feedback = tk.Label(window, text="Welcome! Enter your information to get started.",
    font=('Segoe UI', 9))
lbl_error_feedback.pack(padx=5, pady=(0, 10))


# INPUT FRAME
form_input_frame = tk.Frame(window, relief="groove", borderwidth=2)
form_input_frame.pack(padx=10, pady=(0, 10))

lbl_form_header = tk.Label(form_input_frame, text="User Information",
    font=('Segoe UI', 11, 'bold'))
lbl_form_header.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# NAME
name_label = tk.Label(form_input_frame, text="Name: ", font=('Segoe UI', 10, 'bold'))
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

name_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=20)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# SEX
sex_label = tk.Label(form_input_frame, text="Sex: ", font=('Segoe UI', 10, 'bold'))
sex_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky="w")

sex_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=10)
sex_entry.grid(row=2, column=1, padx=10, pady=(5, 0), sticky="w")

sex_hint = tk.Label(form_input_frame, text="(M/F)", font=('Segoe UI', 8, 'italic'), fg="gray")
sex_hint.grid(row=3, column=1, padx=10, pady=(0, 5), sticky="w")

# AGE
age_label = tk.Label(form_input_frame, text="Age:", font=('Segoe UI', 10, 'bold'))
age_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

age_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=10)
age_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# WEIGHT
weight_label = tk.Label(form_input_frame, text="Weight (kg):", font=('Segoe UI', 10, 'bold'))
weight_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

weight_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=10)
weight_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# HEIGHT
height_label = tk.Label(form_input_frame, text="Height (cm):", font=('Segoe UI', 10, 'bold'))
height_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

height_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=10)
height_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# ACTIVITY
activity_label = tk.Label(form_input_frame, text="Activity: ", font=('Segoe UI', 10, 'bold'))
activity_label.grid(row=7, column=0, padx=10, pady=(5, 0), sticky="w")

activity_entry = tk.Entry(form_input_frame, font=('Segoe UI', 10), width=10)
activity_entry.grid(row=7, column=1, padx=10, pady=(5, 0), sticky="w")

activity_hint = tk.Label(form_input_frame, text="(Light/Moderate/Heavy)",
    font=('Segoe UI', 8, 'italic'), fg="gray")
activity_hint.grid(row=8, column=1, padx=10, pady=(0, 5), sticky="w")

# BUTTONS
reset_button = tk.Button(form_input_frame, text="Reset", font=('Segoe UI', 10),
    width=10, command=reset_application)
reset_button.grid(row=9, column=0, padx=10, pady=10)

calculate_button = tk.Button(form_input_frame, text="Calculate", font=('Segoe UI', 10),
    width=10, command=calculate_deficit)
calculate_button.grid(row=9, column=1, padx=10, pady=10)


# OUTPUT FRAME
frame_output = tk.Frame(window, relief="groove", borderwidth=2)
frame_output.pack(padx=10, pady=10)

lbl_output_header = tk.Label(frame_output, text="Tracking Results",
    font=('Segoe UI', 11, 'bold'))
lbl_output_header.pack(pady=(10, 0))

lbl_out_name = tk.Label(frame_output, text="Your Daily Calorie Limit",
    font=('Segoe UI', 13, 'italic'))
lbl_out_name.pack(padx=10, pady=5)

# RESULTS
lbl_out_daily = tk.Label(frame_output, text="Calories per Day: ",
    font=('Segoe UI', 11, 'bold'))
lbl_out_daily.pack(anchor="w", padx=10, pady=5)

lbl_out_weekly = tk.Label(frame_output, text="Calories per Week: ",
    font=('Segoe UI', 11, 'bold'))
lbl_out_weekly.pack(anchor="w", padx=10, pady=5)

history_label = tk.Label(frame_output, text="System History:", font=('Segoe UI', 11, 'bold'))
history_label.pack(anchor="w", padx=10, pady=(10, 0))


# HISTORY TRACKER
text_history = tk.Text(frame_output, height=5, width=45, font=('Arial', 10), state="disabled")
text_history.pack(padx=10, pady=(0, 10))

window.bind("<Return>", press_enter)

window.mainloop()