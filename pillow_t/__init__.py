from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

if __name__ == '__main__':
    # os.chdir(r'C:\Users\cplwin\Downloads')
    # infile = r'download.jpg'
    infile = r'img.jpg'
    # infile = r'Snipaste_2023-03-21_17-17-27.png'
    # infile = r'Snipaste_2023-03-21_17-26-21.png'
    # im = Image.open(path)
    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
    with Image.open(infile) as im:
        if isinstance(im, Image.Image):
            im = im.convert('L')
            im = im.resize((300, 100))
            # threshold = 100
            # im = im.point(lambda x: 255 if x > threshold else 0)
            code = pytesseract.image_to_string(im)
            print(code)
            im.show()
