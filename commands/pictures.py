import os
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import requests
from io import BytesIO


def nomc(name: str):
    card = Image.open(f"custom/nomc.png")
    width, height = card.size
    side = 175  # <-
    pfp = Image.open("work/user.png").resize((side, side))
    mask = Image.new('L', (side, side), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, side, side), fill=255)
    pfp.putalpha(mask)
    pfp.save('work/user_circular.png')
    cir = Image.open("work/user_circular.png")
    combined_image = Image.new("RGB", (width, height))  # RGB
    mid = side / 2
    combined_image.paste(card, (0, 0))
    combined_image.paste(cir, (int((width / 2 - mid)-1), int(39)), cir)  # <-
    combined_image.save("work/welcome_card.png")
    img = Image.open("work/welcome_card.png")
    font = ImageFont.truetype("fonts/nomc.TTF", 70)
    draw = ImageDraw.Draw(img)
    x = 2
    draw.text((int((width / 2)+x), int(360+x)), f"{name}", (0, 0, 0, 128), anchor="mm", font=font)
    draw.text((int(width / 2), int(360)), f"{name}",
              (255, 255, 255), anchor="mm", font=font)
    img.save("work/final.png")
    return


def make_banner(banner: str, color: str, name: str, join_information: str, greet: str):
    card = Image.open(f"banners/{banner}/{color}.png")
    width, height = card.size

    if width > height:
        side = int(height * 0.6)
    else:
        side = int(width * 0.6)
    pfp = Image.open("work/user.png").resize((side, side))
    mask = Image.new('L', (side, side), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, side, side), fill=255)
    pfp.putalpha(mask)
    pfp.save('work/user_circular.png')
    cir = Image.open("work/user_circular.png")

    combined_image = Image.new("RGB", (width, height))

    mid = side / 2

    combined_image.paste(card, (0, 0))
    combined_image.paste(cir, (int(width / 2 - mid), int(height / 2 - mid)), cir)

    combined_image.save("work/welcome_card.png")

    img = Image.open("work/welcome_card.png")
    font = ImageFont.truetype("fonts/font.TTF", 40)

    draw = ImageDraw.Draw(img)
    draw.text((int(width / 2), int(height / 2 - mid * 1.30)),
              f"{name} {join_information}",
              (255, 255, 255), anchor="mm", font=font)

    draw.text((int(width / 2), int(height / 2 + mid * 1.35)), f"{greet}", (255, 255, 255),
              anchor="mm", font=font)

    img.save("work/final.png")
    return


def get_picture(url: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image.save("work/user.png")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return


def clear(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")
    return
