# String Reversal
import customtkinter as ctk

# Creating the interface
app = ctk.CTk()
app.geometry("400x200")
app.title("String Reversor")

def string_reversor(data):
    # this function collects the input 
    # then reverses the string by slicing it
    return data[::-1]

# Adding Widgets
label = ctk.CTkLabel(app, text = "Enter a string to reverse:")
label.pack(pady = 10)

entry = ctk.CTkEntry(app)
entry.pack(pady = 10)

button = ctk.CTkButton(app, text = "Reverse", command = lambda: output_label.configure(text=f"Reversed: {string_reversor(entry.get())}"))
button.pack(pady = 10)

output_label = ctk.CTkLabel(app, text = "Reversed: ")
output_label.pack(pady = 10)

app.mainloop()