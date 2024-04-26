from typing import Any, List
import uuid
import pathlib

import aiofiles
from aiofiles import os

from src.exception.photo import PictureSaveException, PictureDeleteException
from src.utility import PillowImage
from PIL import Image


class PictureOperator:
    def __init__(self):
        self.based_url = f"{pathlib.Path(__file__).parent.parent.parent.resolve()}\\resources\\"
        self.new_picture_name = None
        self.path_to_picture = None
        self.uuid = uuid

    async def save_picture(self, new_picture: memoryview) -> str:
        try:
            async with aiofiles.open(file=self.path_to_picture, mode="w+b") as picture:
                await picture.write(new_picture)
                await picture.close()
            return self.new_picture_name
        except PictureSaveException as error:
            raise PictureSaveException(f"Ошибка сохранения картинки {self.new_picture_name}!")

    async def remove_picture_by_name(self, picture_name: str) -> str:
        try:
            path_to_picture = self.based_url + picture_name
            await os.remove(path=path_to_picture)
            return f"Картинка {picture_name} была успешно удалена!"
        except PictureDeleteException as error:
            raise PictureDeleteException(f"Ошибка удаления картинки {picture_name}!")

    async def generate_picture_name(self, type_picture: str) -> None:
        self.new_picture_name: str = type_picture + "__" + self.uuid.uuid4().hex + ".png"

    async def set_path_to_file(self) -> None:
        self.path_to_picture = self.based_url + self.new_picture_name


class PictureService:
    def __init__(self):
        self.picture_operator = PictureOperator()
        self.pillow_image = PillowImage()

    async def save_picture(self, type_picture: str, new_picture) -> str:
        try:
            await self.picture_operator.generate_picture_name(type_picture=type_picture)
            await self.picture_operator.set_path_to_file()
            await self.pillow_image.save_image_pillow(photo=new_picture)
            image_buffer = await self.pillow_image.get_buffer_with_image()
            new_photo_name = await self.picture_operator.save_picture(new_picture=image_buffer)
            return new_photo_name
        except PictureSaveException as error:
            return "Ошибка сохранения картинки!"

    async def update_picture(self, old_picture_name: str, new_picture_type: str, picture) -> str:
        await self.picture_operator.remove_picture_by_name(picture_name=old_picture_name)
        await self.picture_operator.generate_picture_name(type_picture=new_picture_type)
        await self.picture_operator.set_path_to_file()
        new_picture_name = await self.picture_operator.save_picture(new_picture=picture)
        return new_picture_name

    async def delete_pictures(self, pictures_name: List[str]) -> str:
        try:
            for picture_name in pictures_name:
                await self.picture_operator.remove_picture_by_name(picture_name=picture_name)
            return "Все картинки были удалены!"
        except PictureDeleteException as error:
            return "Ошибка удаления картинок!"

    async def delete_picture(self, picture_name: str) -> str:
        try:
            result = await self.picture_operator.remove_picture_by_name(picture_name=picture_name)
            return result
        except PictureDeleteException:
            return "Ошибка удаления картинки!"
