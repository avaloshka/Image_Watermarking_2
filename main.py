import PIL
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog


def upload_file(event=None):
    filename = filedialog.askopenfilename()
    # Get path to image
    image = tk.PhotoImage(filename)

    try:
        with Image.open(f'{image}').convert('RGBA') as base:
            # Transparent text
            txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
            # Font
            fnt = ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf", 40)
            # Get a drawing context
            d = ImageDraw.Draw(txt)
            # Draw text half opacity
            d.text((10, 10), "alexvaloshka.com", font=fnt, fill=(255, 255, 255, 128))
            # Draw text full opacity
            # d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

            out = Image.alpha_composite(base, txt)
            out.show()

    except PIL.UnidentifiedImageError:
        print('This type of file is not supported, please try again!')


root = tk.Tk()
root.title('Watermarking Program')
root.minsize(200, 100)
label1 = tk.Label(root, text='Please enter image you would like to be Watermarked', font=('Arial', 12) ).grid(column=0, row=0, columnspan=2)
button = tk.Button(root, text='OPEN', command=upload_file)
label2 = tk.Label(root, text='').grid(column=0, row=1, columnspan=3)
button.grid(column=3, row=2)

root.mainloop()