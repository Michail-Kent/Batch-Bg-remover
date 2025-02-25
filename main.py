import os
from tkinter import *
from tkinter import filedialog, messagebox
import requests
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np


REMOVE_BG_API_KEY = 'Ljf2VcdCyS1EoeBZUHjFjHuz'


def enhance_image(input_path):
    try:
        img = Image.open(input_path)
        
        
        if img.width < 1000 or img.height < 1000:
            img = img.resize((img.width * 2, img.height * 2))  

       
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)  
        
     
        img = img.filter(ImageFilter.SHARPEN)

        return img

    except Exception as e:
        messagebox.showerror("Error", f"Failed to enhance image: {e}")
        return None

def remove_background(input_path, output_path):
    try:
        
        enhanced_img = enhance_image(input_path)
        if enhanced_img is None:
            return

        with open(input_path, 'rb') as input_file:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': input_file},
                data={'size': 'auto'},
                headers={'X-Api-Key': REMOVE_BG_API_KEY},
            )
        
        if response.status_code == 200:
           
            with open(output_path, 'wb') as output_file:
                output_file.write(response.content)
            messagebox.showinfo("Success", "Background removed successfully.")
        else:
            messagebox.showerror("Error", f"Failed to remove background. Status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove background: {e}")


def process_batch():
    input_files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not input_files:
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    for input_file in input_files:
        filename = os.path.basename(input_file)
        output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_no_bg.png")
        remove_background(input_file, output_file)

    messagebox.showinfo("Batch Processing", "Background removal completed for all selected images.")


def process_single():
    input_file = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(title="Save Image As", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not output_file:
        return

    remove_background(input_file, output_file)


root = Tk()
root.title("Background Remover")
root.geometry("300x200")


single_button = Button(root, text="Remove Background (Single)", width=25, command=process_single)
single_button.pack(pady=20)

batch_button = Button(root, text="Remove Background (Batch)", width=25, command=process_batch)
batch_button.pack(pady=10)


root.mainloop()
