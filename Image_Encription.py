
# import numpy as np
# from PIL import Image

# # Load the image
# image_path = 'WhatsApp Image 2024-06-14 at 11.57.45 AM.jpeg'
# img = Image.open(image_path)
# pixels = np.array(img)

# # Define a more secure encryption function using a PRNG
# def encrypt_pixels(pixels, key):
#     np.random.seed(key)
#     random_values = np.random.randint(0, 256, pixels.shape, dtype=np.uint8)
#     encrypted_pixels = pixels ^ random_values
#     return encrypted_pixels

# # Define the corresponding decryption function
# def decrypt_pixels(encrypted_pixels, key):
#     np.random.seed(key)
#     random_values = np.random.randint(0, 256, encrypted_pixels.shape, dtype=np.uint8)
#     decrypted_pixels = encrypted_pixels ^ random_values
#     return decrypted_pixels

# # Encrypt the image
# key = 12345  # example key
# encrypted_pixels = encrypt_pixels(pixels, key)

# # Save the encrypted image
# encrypted_img = Image.fromarray(encrypted_pixels)
# encrypted_image_path = 'encrypted_image_secure.jpeg'
# encrypted_img.save(encrypted_image_path)

# # Decrypt the image
# decrypted_pixels = decrypt_pixels(encrypted_pixels, key)
# decrypted_img = Image.fromarray(decrypted_pixels)
# decrypted_image_path = 'decrypted_image_secure.jpeg'
# decrypted_img.save(decrypted_image_path)

# # Verify that the images have been saved
# import os
# os.path.exists(encrypted_image_path), os.path.exists(decrypted_image_path)
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

# Define a more secure encryption function using a PRNG
def encrypt_pixels(pixels, key):
    np.random.seed(key)
    random_values = np.random.randint(0, 256, pixels.shape, dtype=np.uint8)
    encrypted_pixels = pixels ^ random_values
    return encrypted_pixels

# Define the corresponding decryption function
def decrypt_pixels(encrypted_pixels, key):
    np.random.seed(key)
    random_values = np.random.randint(0, 256, encrypted_pixels.shape, dtype=np.uint8)
    decrypted_pixels = encrypted_pixels ^ random_values
    return decrypted_pixels

# Function to load an image
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpeg *.jpg *.png")])
    if file_path:
        img = Image.open(file_path)
        return np.array(img), file_path
    return None, None

# Function to save an image
def save_image(image, title="Save Image"):
    file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg"), ("PNG files", "*.png")], title=title)
    if file_path:
        img = Image.fromarray(image)
        img.save(file_path)
        return file_path
    return None

# Encrypt button action
def encrypt_action():
    pixels, file_path = load_image()
    if pixels is not None:
        key = key_entry.get()
        if key.isdigit():
            key = int(key)
            encrypted_pixels = encrypt_pixels(pixels, key)
            save_image(encrypted_pixels, "Save Encrypted Image")
            messagebox.showinfo("Success", "Image encrypted and saved successfully!")
        else:
            messagebox.showerror("Error", "Key must be a numeric value")
    else:
        messagebox.showerror("Error", "No image selected")

# Decrypt button action
def decrypt_action():
    pixels, file_path = load_image()
    if pixels is not None:
        key = key_entry.get()
        if key.isdigit():
            key = int(key)
            decrypted_pixels = decrypt_pixels(pixels, key)
            save_image(decrypted_pixels, "Save Decrypted Image")
            messagebox.showinfo("Success", "Image decrypted and saved successfully!")
        else:
            messagebox.showerror("Error", "Key must be a numeric value")
    else:
        messagebox.showerror("Error", "No image selected")

# Create the GUI
root = tk.Tk()
root.title("Image Encryptor/Decryptor")
root.geometry("400x200")

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter Encryption/Decryption Key:").grid(row=0, column=0, columnspan=2, pady=10)

key_entry = ttk.Entry(frame)
key_entry.grid(row=1, column=0, columnspan=2, pady=10)

encrypt_button = ttk.Button(frame, text="Encrypt Image", command=encrypt_action)
encrypt_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

decrypt_button = ttk.Button(frame, text="Decrypt Image", command=decrypt_action)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()
