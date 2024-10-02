import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Worker:
    @staticmethod
    async def sketch(fp):
        img = cv2.imread(fp)
        pencil, coloured = cv2.pencilSketch(img, sigma_s=3, sigma_r=0.07, shade_factor=0.07)
        cv2.imwrite("resources/output/sketch.png", pencil)

    @staticmethod
    async def colorSketch(fp):
        img = cv2.imread(fp)
        pencil, coloured = cv2.pencilSketch(img, sigma_s=3, sigma_r=0.07, shade_factor=0.07)
        cv2.imwrite("resources/output/colorsketch.png", coloured)

    @staticmethod
    async def Canny(fp):
        img = cv2.imread(fp)
        cannyImg = cv2.Canny(img, threshold1=100, threshold2=250)
        cv2.imwrite("resources/output/canny.png", cannyImg)

    @staticmethod
    async def brazzers(fp):
        with Image.open("resources/templates/brazzers.png") as bzpic:
            with Image.open(fp) as img:
                resizedbz = bzpic.resize((int(bzpic.width*(img.width/1400)), int(bzpic.height*(img.height/1000))))
                img.paste(resizedbz, (img.width - resizedbz.width, img.height - resizedbz.height))
                img.save('resources/output/brazzers.png')

    @staticmethod
    async def ship(avatar1, avatar2):
        img = cv2.imread("resources/templates/heart.png")
        img_width = 225
        img_height = 225

        avatar1 = cv2.imread(avatar1)
        resizedav1 = cv2.resize(avatar1, (img_width, img_height))

        avatar2 = cv2.imread(avatar2)
        resizedav2 = cv2.resize(avatar2, (img_width, img_height))

        out = np.hstack((resizedav1, img, resizedav2))

        cv2.imwrite('resources/output/ship.png', out)

    @staticmethod
    async def paisebarbadbc(text):
        with Image.open("resources/templates/paisabarbad.jpg") as img:
            if len(text) < 34:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 45)
                draw.multiline_text((40, 200), text=text, fill=(255, 0, 0), font=font)
                img = img.crop((0, 160, img.width, img.height))

            elif 34 <= len(text) <= 67:
                thetext = ''
                c = 1
                for x in text:
                    if c % 34 == 0:
                        thetext += f"-\n{x}"
                    else:
                        thetext += x
                    c += 1

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 45)
                draw.multiline_text((40, 160), text=thetext, fill=(255, 0, 0), font=font)

                img = img.crop((0, 120, img.width, img.height))

            elif 68 <= len(text) <= 100:
                thetext = ''
                c = 1
                for x in text:
                    if c % 34 == 0:
                        thetext += f"-\n{x}"
                    else:
                        thetext += x
                    c += 1

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 45)
                draw.multiline_text((40, 115), text=thetext, fill=(255, 0, 0), font=font)

                img = img.crop((0, 65, img.width, img.height))

            else:
                thetext = ''
                c = 1
                for x in text:
                    if c % 34 == 0:
                        thetext += f"-\n{x}"
                    else:
                        thetext += x
                    c += 1

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 45)
                draw.multiline_text((40, 80), text=thetext, fill=(255, 0, 0), font=font)

                img = img.crop((0, 40, img.width, img.height))

            img.save('resources/output/paisebarbad.png')

    @staticmethod
    async def trump(text):
        with Image.open("resources/templates/trump.jpg") as img:
            if len(text) <= 47:
                font = ImageFont.truetype("resources/fonts/opensans.ttf", 18)
                draw = ImageDraw.Draw(img)
                draw.multiline_text((15, 55), text=text, fill=(0, 0, 0), font=font)

                img.save('resources/output/trump.png')
            else:
                theText = ''
                c = 1
                for x in text:
                    if c % 48 == 0:
                        if x == " ":
                            theText += "\n"
                        else:
                            theText += f"-\n{x}"

                    else:
                        theText += x
                    c += 1

                font = ImageFont.truetype("resources/fonts/opensans.ttf", 18)
                draw = ImageDraw.Draw(img)
                draw.multiline_text((15, 55), text=theText, fill=(0, 0, 0), font=font)

                img.save('resources/output/trump.png')

    @staticmethod
    async def drake(text1, text2):
        with Image.open("resources/templates/drake.png") as img:
            font = ImageFont.truetype("resources/fonts/Itim.ttf", 22)
            draw = ImageDraw.Draw(img)
            if len(text1) < 27:
                draw.multiline_text((int(img.width / 2 + 10), int(img.height / 4)), text=text1, fill=(0, 0, 0),
                                    font=font)
            else:
                c = 1
                upperText = ''
                for x in text1:
                    if c % 27 == 0:
                        upperText += f'-\n{x}'
                        c += 1
                    else:
                        upperText += x
                        c += 1

                draw.multiline_text((int(img.width / 2 + 10), 30), text=upperText, fill=(0, 0, 0), font=font)

            if len(text2) < 27:
                draw.multiline_text((int(img.width / 2 + 10), int(350)), text=text2, fill=(0, 0, 0), font=font)

            else:
                c = 1
                lowerText = ''
                for x in text2:
                    if c % 27 == 0:
                        lowerText += f'-\n{x}'
                        c += 1
                    else:
                        lowerText += x
                        c += 1

                draw.multiline_text((int(img.width / 2 + 10), 270), text=lowerText, fill=(0, 0, 0), font=font)

            img.save('resources/output/drake.png')

    @staticmethod
    async def write_motivation(text):
        filename = 'resources/output/motivation.png'
        with Image.open("resources/templates/motivation.jpg") as img:
            if len(text) < 28:  # len(text) < 33:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 80)
                draw.text((170, 400), text=text, fill=(0, 0, 0), font=font)
                img.save(filename)

            elif 28 <= len(text) <= 186:
                c = 1
                motivation = ''
                for x in text:
                    if c % 33 == 0:
                        motivation += f'-\n{x}'
                    else:
                        motivation += x
                    c += 1

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 80)
                draw.text((100, 250), text=motivation, fill=(0, 0, 0), font=font)
                img.save(filename)

            else:
                c = 1
                motivation = ''
                for x in text:
                    if c % 33 == 0:
                        motivation += f'-\n{x}'
                    else:
                        motivation += x
                    c += 1

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("resources/fonts/yrsa.ttf", 80)
                draw.text((100, 100), text=motivation, fill=(0, 0, 0), font=font)
                img.save(filename)

    @staticmethod
    async def whathow(fp):
        with Image.open("resources/templates/whathow.jpg") as img:
            with Image.open(fp) as avatar:
                resizedAvatar = avatar.resize((110, 110))
                img.paste(resizedAvatar, (133, 55))
                img.save('resources/output/whathow.png')

    @staticmethod
    async def detailscard(avatar, name, email, pswd, phno, virginstatus, networth, profession):
        with Image.open("resources/templates/details.png") as img:
            font = ImageFont.truetype("resources/fonts/opensans.ttf", 28)
            draw = ImageDraw.Draw(img)
            draw.text((402, 91), text=name, fill=(0, 0, 0), font=font)
            draw.text((402, 124), text=email, fill=(0, 0, 0), font=font)
            draw.text((445, 157), text=pswd, fill=(0, 0, 0), font=font)
            draw.text((440, 192), text=phno, fill=(0, 0, 0), font=font)
            draw.text((408, 224), text=virginstatus, fill=(0, 0, 0), font=font)
            draw.text((455, 258), text=networth, fill=(0, 0, 0), font=font)
            draw.text((457, 291), text=profession, fill=(0, 0, 0), font=font)

            with Image.open(avatar) as av:
                res = av.resize((218, 218))
                img.paste(res, (59, 116))

                img.save('resources/output/detailscard.png')
