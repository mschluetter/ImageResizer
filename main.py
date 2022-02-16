import os
from imageresizer import ImageResizer
from imageresizer.cropstrategies import cropMiddleCenter

def main() -> None:
    imgpath = os.path.join("examples", "example.jpg")
    safepath = os.path.join("examples", "output.jpg")

    resizer = ImageResizer(imgpath, safepath, max_storage=100000)
    resizer.run()

if __name__ == "__main__":
    main()