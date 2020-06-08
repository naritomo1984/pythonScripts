# pythonScripts

**combineTexture.py**
![sample](illust.png)
This script will combine the multiple textures into one texture.(Use all textures inside the directory)

The script takes 3 argments *folderpath*, *image resolution*, *texture type*.  
E.g. python3 combineTexture.py ./tex/ 1024 base.  
Texture types including "base", "normal", "metalic", "roughness", "ao", "emissive".  
Tesolution should be same as original texture resolution.  
Python and PIL environment required.  
