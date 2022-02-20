import os
from imageresizer import ImageResizer
from imageresizer.cropstrategies import cropTopCenter

def main() -> None:
    imgpath = os.path.join("examples", "example.jpg")
    safepath = os.path.join("examples", "output4.jpg")
    crop = cropTopCenter((700, 400))

    resizer = ImageResizer(imgpath, safepath, crop, max_width=700, max_height=400)
    resizer.run()

if __name__ == "__main__":
    main()