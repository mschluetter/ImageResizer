import os
from imageresizer import ImageResizer
from imageresizer.cropstrategies import cropMiddleRight

def main() -> None:
    imgpath = os.path.join("example.jpg")
    safepath = os.path.join("example1.jpg")

    resizer = ImageResizer(imgpath, safepath)
    resizer.run()

if __name__ == "__main__":
    main()