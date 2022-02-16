from dataclasses import dataclass
from typing import Protocol, Tuple
from PIL import Image

class Crop(Protocol):
    def crop(self, img: Image) -> Image:
        ...

@dataclass
class cropTopLeft:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        return img.crop((0, 0, self.size[0], self.size[1]))

@dataclass
class cropTopCenter:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        return img.crop((pos1, 0, pos1+self.size[0], self.size[1]))

@dataclass
class cropTopRight:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0])
        return img.crop((pos1, 0, img.width, self.size[1]))

@dataclass
class cropMiddleLeft:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((0,pos2, self.size[0], pos2+self.size[1]))

@dataclass
class cropMiddleCenter:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((pos1,pos2, pos1+self.size[0], pos2+self.size[1]))

@dataclass
class cropMiddleRight:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = img.width - self.size[0]
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((pos1,pos2, img.width, pos2+self.size[1]))

@dataclass
class cropBottomLeft:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos2 = img.height - self.size[1]
        return img.crop((0,pos2, self.size[0], img.height))

@dataclass
class cropBottomCenter:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        pos2 = img.height - self.size[1]
        return img.crop((pos1,pos2, pos1+self.size[0], img.height))

@dataclass
class cropBottomRight:
    size: Tuple[int]
    img: Image = None
    def crop(self, img: Image) -> Image:
        pos1 = img.width - self.size[0]
        pos2 = img.height - self.size[1]
        return img.crop((pos1,pos2, img.width, img.height))

@dataclass
class cropCustom:
    size: Tuple[int]
    startingpoints: Tuple[int]
    def crop(self, img: Image) -> Image:
        return img.crop((self.startingpoints[0],
                        self.startingpoints[1],
                        self.startingpoints[0] + self.size[0],
                        self.startingpoints[1] + self.size[1]
                        ))
