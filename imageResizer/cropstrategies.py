from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple
from PIL import Image

@dataclass
class Crop(ABC):
    size: Tuple[int]
    @abstractmethod
    def crop(self, img: Image) -> Image:
        pass

@dataclass
class cropTopLeft(Crop):
    def crop(self, img: Image) -> Image:
        return img.crop((0, 0, self.size[0], self.size[1]))

@dataclass
class cropTopCenter(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        return img.crop((pos1, 0, pos1+self.size[0], self.size[1]))

@dataclass
class cropTopRight(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0])
        return img.crop((pos1, 0, img.width, self.size[1]))

@dataclass
class cropMiddleLeft(Crop):
    def crop(self, img: Image) -> Image:
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((0,pos2, self.size[0], pos2+self.size[1]))

@dataclass
class cropMiddleCenter(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((pos1,pos2, pos1+self.size[0], pos2+self.size[1]))

@dataclass
class cropMiddleRight(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = img.width - self.size[0]
        pos2 = (img.height - self.size[1]) / 2
        return img.crop((pos1,pos2, img.width, pos2+self.size[1]))

@dataclass
class cropBottomLeft(Crop):
    def crop(self, img: Image) -> Image:
        pos2 = img.height - self.size[1]
        return img.crop((0,pos2, self.size[0], img.height))

@dataclass
class cropBottomCenter(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = (img.width - self.size[0]) / 2
        pos2 = img.height - self.size[1]
        return img.crop((pos1,pos2, pos1+self.size[0], img.height))

@dataclass
class cropBottomRight(Crop):
    def crop(self, img: Image) -> Image:
        pos1 = img.width - self.size[0]
        pos2 = img.height - self.size[1]
        return img.crop((pos1,pos2, img.width, img.height))

@dataclass
class cropCustom(Crop):
    startingpoints: Tuple[int]
    def crop(self, img: Image) -> Image:
        return img.crop((self.startingpoints[0],
                        self.startingpoints[1],
                        self.startingpoints[0] + self.size[0],
                        self.startingpoints[1] + self.size[1]
                        ))
