import pyscreenshot as ImageGrab

if __name__ == "__main__":
    input("Отодвиньте терминал и нажмите <ENTER> для создания скриншота...")

    im = ImageGrab.grab(bbox=(162, 92, 820, 260))
    im.save("09_02_01.png")
