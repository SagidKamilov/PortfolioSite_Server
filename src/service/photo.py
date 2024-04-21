from typing import Any, List
import uuid
import pathlib

import aiofiles
from aiofiles import os

from src.exceptions.photo import PhotoSaveException, PhotoDeleteException
from src.utility import PillowImage
from PIL import Image


class PhotoOperator:
    def __init__(self):
        self.based_url = f"{pathlib.Path(__file__).parent.parent.parent.resolve()}\\resources\\"
        self.new_photo_name = None
        self.path_to_photo = None
        self.uuid = uuid

    async def save_photo(self, new_photo: memoryview) -> str:
        try:
            async with aiofiles.open(file=self.path_to_photo, mode="w+b") as photo:
                await photo.write(new_photo)
                await photo.close()
            return self.new_photo_name
        except PhotoSaveException as error:
            raise PhotoSaveException(f"Ошибка сохранения картинки {self.new_photo_name}!")

    async def remove_photo_by_name(self, photo_name: str) -> str:
        try:
            path_to_photo = self.based_url + photo_name
            await os.remove(path=path_to_photo)
            return f"Картинка {photo_name} была успешно удалена!"
        except PhotoDeleteException as error:
            raise PhotoDeleteException(f"Ошибка удаления картинки {photo_name}!")

    async def generate_photo_name(self, type_photo: str) -> None:
        self.new_photo_name: str = type_photo + "__" + self.uuid.uuid4().hex + ".png"

    async def set_path_to_file(self) -> None:
        self.path_to_photo = self.based_url + self.new_photo_name


class PhotoService:
    def __init__(self):
        self.photo_operator = PhotoOperator()
        self.pillow_image = PillowImage()

    async def save_photo(self, type_photo: str, new_photo) -> str:
        try:
            await self.photo_operator.generate_photo_name(type_photo=type_photo)
            await self.photo_operator.set_path_to_file()
            await self.pillow_image.save_image_pillow(photo=new_photo)
            image_buffer = await self.pillow_image.get_buffer_with_image()
            new_photo_name = await self.photo_operator.save_photo(new_photo=image_buffer)
            return new_photo_name
        except PhotoSaveException as error:
            return "Ошибка сохранения картинки!"

    async def update_photo(self, old_photo_name: str, new_photo_type: str, photo) -> str:
        await self.photo_operator.remove_photo_by_name(photo_name=old_photo_name)
        await self.photo_operator.generate_photo_name(type_photo=new_photo_type)
        await self.photo_operator.set_path_to_file()
        new_photo_name = await self.photo_operator.save_photo(new_photo=photo)
        return new_photo_name

    async def delete_photos(self, photos_name: List[str]) -> str:
        try:
            for photo_name in photos_name:
                await self.photo_operator.remove_photo_by_name(photo_name=photo_name)
            return "Все картинки были удалены!"
        except PhotoDeleteException as error:
            return "Ошибка удаления картинок!"

    async def delete_photo(self, photo_name: str) -> str:
        try:
            result = await self.photo_operator.remove_photo_by_name(photo_name=photo_name)
            return result
        except PhotoDeleteException:
            return "Ошибка удаления картинки!"
