from abc import ABC, abstractstaticmethod
from typing import Dict, Tuple
from PIL import Image
from dataclasses import dataclass

class cropStrategy(ABC):
    @abstractstaticmethod
    def crop(self, img: Image) -> Image:
        """ Save strategy """

@dataclass
class cropNothing(cropStrategy):
    img: Image

    def crop(self, img: Image) -> Image:
        return Image

@dataclass
class ImageResizer:
    picpath: str
    savepath: str
    crop_strategy: cropStrategy
    min_width: int = 0
    min_height: int = 0
    max_width = None
    max_height = None

    def run(self) -> None:
        img = Image.open(self.picpath)
        if self.max_height == None:
            self.max_height = img.heigh
        if self.max_width == None:
            self.max_width = img.width
        img = self.expand_image(img)
        img = self.shrink_image(img)
        img = self.crop_strategy.crop(img)
        img.save(self.savepath, quality=95)

    def expand_image(self, img: Image) -> Image:
        if img.width < self.min_width or img.height < self.min_height:
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
            width, height = img.size
            while True:
                width -= 1
                height = img.height * width // img.width
                if width <= self.max_width and height <= self.max_height:
                    break
            img = img.resize((width, height), Image.LANCZOS)
        return img

def main() -> None:
    # Path to image
    # Path to save
    # Create a save strategy
    pass

if __name__ == "__main__":
    main()