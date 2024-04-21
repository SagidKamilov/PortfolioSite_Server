from io import BytesIO
from PIL import Image


class PillowImage:
    def __init__(self):
        self.buffer = BytesIO()

    async def save_image_pillow(self, photo):
        open_photo = Image.open(fp=photo)
        open_photo.save(fp=self.buffer, format="PNG")

    async def get_buffer_with_image(self):
        return self.buffer.getbuffer()
