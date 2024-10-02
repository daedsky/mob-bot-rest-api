import random
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
from worker import Worker
from typing import Optional

app = FastAPI()


def write_image(fp, content):
    with open(fp, 'wb') as f:
        f.write(content)


@app.get('/')
async def home():
    return {"endpoints": "/docs"}


@app.get('/sketch')
async def sketch(imgurl: str):
    fp = 'resources/temp/sketch_img.png'
    img = requests.get(imgurl).content
    write_image(fp, img)
    await Worker.sketch(fp)
    return FileResponse('resources/output/sketch.png')


@app.get('/colorsketch')
async def colorsketch(imgurl: str):
    fp = 'resources/temp/colorsketch_img.png'
    img = requests.get(imgurl).content
    write_image(fp, img)
    await Worker.colorSketch(fp)
    return FileResponse('resources/output/colorsketch.png')


@app.get('/canny')
async def canny(imgurl: str):
    fp = 'resources/temp/canny_avatar.png'
    img = requests.get(imgurl).content
    write_image(fp, img)
    await Worker.Canny(fp)
    return FileResponse('resources/output/canny.png')


@app.get('/brazzers')
async def brazzers(imgurl: str):
    fp = 'resources/temp/brazzers_avatar.png'
    img = requests.get(imgurl).content
    write_image(fp, img)
    await Worker.brazzers(fp)
    return FileResponse('resources/output/brazzers.png')


@app.get('/ship')
async def ship(imgurl1: str, imgurl2: str):
    fp1 = 'resources/temp/ship_avatar1.png'
    fp2 = 'resources/temp/ship_avatar2.png'
    img1 = requests.get(imgurl1).content
    img2 = requests.get(imgurl2).content
    write_image(fp1, img1)
    write_image(fp2, img2)
    await Worker.ship(fp1, fp2)
    return FileResponse('resources/output/ship.png')


@app.get('/paisebarbad')
async def paisebarbad(text: str):
    await Worker.paisebarbadbc(text)
    return FileResponse('resources/output/paisebarbad.png')


@app.get('/trump')
async def trump(text: str):
    await Worker.trump(text)
    return FileResponse('resources/output/trump.png')


@app.get('/drake')
async def drake(text1: str, text2: str):
    await Worker.drake(text1, text2)
    return FileResponse('resources/output/drake.png')


@app.get('/motivation')
async def motivaton(text: str):
    await Worker.write_motivation(text)
    return FileResponse('resources/output/motivation.png')


@app.get('/whathow')
async def whathow(imgurl: str):
    fp = 'resources/temp/whathow.png'
    img = requests.get(imgurl).content
    write_image(fp, img)
    await Worker.whathow(fp)
    return FileResponse('resources/output/whathow.png')


@app.get('/detailscard')
async def detailscard(*, imgurl: str,
                      name: str,
                      profession: str,
                      status: str,
                      email: Optional[str] = None,
                      pswd: Optional[str] = None,
                      ph_no: Optional[int] = None,
                      networth: Optional[int] = None):
    fp = 'resources/temp/detailscard_avatar.png'
    img = requests.get(imgurl).content
    write_image(fp, img)

    email = email if email else f"{name}{random.randint(111, 9999)}@gmail.com"
    pswd = pswd if pswd else f"{name}{random.randint(111, 9999)}"
    ph_no = str(ph_no) if ph_no else str(random.randint(7777777777, 9999999999))
    networth = f"{networth}$" if networth else f"{str(random.randint(-10000, 10000))}$"

    await Worker.detailscard(fp, name, email, pswd, ph_no, status, networth, profession)

    return FileResponse('resources/output/detailscard.png')
