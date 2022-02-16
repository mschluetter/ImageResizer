# Image resizer
This is a generic image resizer. You can use it to shrink or expand images to maximum sizes. By choosing a crop strtategy you can cut the image on an exact pixel size.
# Installation
The usage requires the pillow lirbary. You can install it with pip:
```
pip install pillow
```
# Usage
You can use the resizer in three ways:
<ul>
    <li>Resizing images</li>
    <li>Crop an image in exact dimensions</li>
    <li>Combining resizing and cropping</li>
</ul>
The resizing and cropping happens in the ImageResizer class. When you want to crop an image, you import a crop strategy (see down below). The Image resizer has the following parameters:

```python
ImageResizer(picpath: str, 
            savepath: str, 
            crop_strategy: Crop = None,
            min_width: int = 0,
            min_height: int = 0,
            max_width: int = None,
            max_height: int = None,
            max_storage: int = None)
```
<ul>
    <li><strong>picpath</strong>: The path to the image. I recommend os.path.join() for that.</li>
    <li><strong>savepath</strong>: The path where the new image has to be saved. When you save the image you can provide a suffix of the common images from <a href="https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html?highlight=writer">Pillow Image file formats</a>. I recommend os.path.join() for the path.</li>
    <li><strong>crop_strategy</strong>: Default in None. When you want to crop the image you choose the crop strategy and pass it here.</li>
    <li><strong>min_width & min_height</strong>: Defaults are 0. If your image has a minimum size you can pass it here. Just pass the values you need. The image will expand with locked aspect ratio.</li>
    <li><strong>max_width & max_height</strong>: Defaults are set to the original image width and height when you leave it empty. This is the maximum width and height an image will have. You just need to pass the values you need. The image will be shrink with locked aspect ratio.</li>
    <li><strong>max_storage</strong>: Maximum storage space in bytes. For 4MB you need to enter 4,000,000. If the image is larger than needed, the quality will be reduced. The smallest quality is 50% (Downsizing of DPI).
    </ul>

## Resizing Images with minimum and maximum
For resizing you can set minimum and maximum pixels. The actual resizing will happen relatively. If 
```python
import os
from imageresizer import ImageResizer

imgpath = os.path.join("examples", "example.jpg")
safepath = os.path.join("examples", "output.jpg")

resizer = ImageResizer(imgpath, safepath, max_width=1200, max_height=800)
resizer.run()
```