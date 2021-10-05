import cv2

PICTURES = {'облачно': ['weather_img/cloud.jpg', (0, 0, 0)],
            'дождь': ['weather_img/rain.jpg', (255, 0, 0)],
            'дождь/гроза': ['weather_img/rain.jpg', (255, 0, 0)],
            'ясно': ['weather_img/sun.jpg', (0, 255, 255)],
            'снег': ['weather_img/snow.jpg', (255, 255, 0)]
            }

IMAGE_TEMPLATE = 'weather_img/probe.jpg'
FONT = cv2.FONT_HERSHEY_COMPLEX
FONT_SIZE = 0.8
TEXT_COLOR = (255, 0, 0)
DATE_POZ = (160, 230)
TEMPERATURE_POZ = (100, 120)
WEATHER_POZ = (200, 180)


class ImageMaker:
    def __init__(self, date, temperature, weather):
        self.date = date
        self.temperature = temperature
        self.weather = weather

    def generate_image(self, number):
        day_weather_image = cv2.imread(IMAGE_TEMPLATE)

        self.make_gradient(day_weather_image)
        self.insert_text(day_weather_image)
        self.insert_picture(day_weather_image)

        output_file = 'weather_img_' + str(number) + '.jpg'
        with open(output_file, 'w'):
            cv2.imwrite(output_file, day_weather_image)

    def insert_picture(self, day_weather_image):
        if self.weather in PICTURES:
            picture_path = PICTURES[self.weather][0]
        else:
            picture_path = PICTURES['облачно'][0]
        weather_picture = cv2.imread(picture_path)
        day_weather_image[50:150, 200:300, :] = weather_picture

    def insert_text(self, day_weather_image):
        coord_texts = [{'coord': DATE_POZ, 'text': self.date}, {'coord': TEMPERATURE_POZ, 'text': self.temperature},
                       {'coord': WEATHER_POZ, 'text': self.weather}]
        for info in coord_texts:
            cv2.putText(img=day_weather_image, text=info['text'], org=info['coord'], fontFace=FONT,
                        fontScale=FONT_SIZE, color=TEXT_COLOR, thickness=1)

    def make_gradient(self, day_weather_image):
        g, b, r = PICTURES[self.weather][1]
        for n in range(255):
            color = (g, b, r)
            day_weather_image[n:n + 1, :] = color
            if g < 255:
                g += 1
            if b < 255:
                b += 1
            if r < 255:
                r += 1
