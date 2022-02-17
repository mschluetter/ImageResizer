from PIL import Image
from dataclasses import dataclass
from .cropstrategies import Crop
import os

@dataclass
class ImageResizer:
    picpath: str
    savepath: str
    crop_strategy: Crop = None
    min_width: int = 0
    min_height: int = 0
    max_width: int = None
    max_height: int = None

    def run(self) -> None:
        img = Image.open(self.picpath)
        if self.max_height == None:
            self.max_height = img.height
        if self.max_width == None:
            self.max_width = img.width
        img = self.expand_image(img)
        img = self.shrink_image(img)
        if self.crop_strategy != None:

            img = self.crop_strategy.crop(img)

        path = os.path.split(self.savepath)
        suffix = path[1].split(".")[1]
        if suffix.upper() == "JPG":
            suffix = "JPEG"
        img.save(self.savepath, quality=95, format=suffix, subsampling=0)

    def expand_image(self, img: Image) -> Image:
        if img.width < self.min_width or img.height < self.min_height:
            #print("expand")
            width, height = img.size
            while True:
                width += 1
                height = img.height * width // img.width
                if width >= self.min_width and height >= self.min_height:
                    break
            img = img.resize((width, height), Image.LANCZOS)
        return img

    def shrink_image(self, img: Image) -> Image:
        if img.width > self.max_width or img.height > self.max_height:
            #print("shrink")
            width, height = img.size
            while True:
                width -= 1
                height = img.height * width // img.width
                if self.crop_strategy != None:
                    if width <= self.crop_strategy.size[0] or height <= self.crop_strategy.size[1]:
                        break
                if width <= self.max_width and height <= self.max_height:
                    break
            img = img.resize((width, height), Image.LANCZOS)
        return img