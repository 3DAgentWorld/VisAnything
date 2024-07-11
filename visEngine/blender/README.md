# visualization in BLENDER

- run the scripts in **blender environment**!
- read opencv camera (.json), opencv mesh (.ply) and auto transform to blender system!

# usage

### 1. debug camera
- `read_cam.py`: read camera json file and show in UI, using for debug camera. suppose camera json file
 is in opencv system.

### 2. rendering with blender
- `rend_circle.py`: for rendering the mesh in 360 degree. Firstly setting the mesh to center manually in blender GUI,
then run the script; you can preview the camera in blender GUI letting set_mode=True.
- `rend_via_cam.py`: read camera .json file and .ply file (mesh) and rend, usually for comparing the mesh result with 
gt image. If you do not use GUI and just rend, use the command like this:
```
"D:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b -P rend_via_cam.py
```


### 3. mesh process
- `cull_mesh_box.py`: cull mesh after setting a xyz surrounding box. for reducing size.

### 4. post process of video/images
- `compress_image.py`: compress the rendered image of blender for better showing on paper/project page. make sure:
```
---input_path/
------image_folder_01/
------image_folder_02/
...
------image_folder_99/
```
- `win_bash/compress_video`: compress video using ffmpeg in windows, for better showing on project page.
```
---input_folder/
------0001.mp4
------0002.mp4
...
------0199.mp4
```
after that, the compressed video will be saved to 
```
---input_folder/
------0001.mp4
------0002.mp4
...
------0199.mp4
------down/
---------0001_compressed.mp4
---------0002_compressed.mp4
...
---------0199_compressed.mp4
```
- `win_bash/video_to_frame.bat`: change all videos to frames in folder in windows
```
---video_dir/
------0001.mp4
------0002.mp4
...
------0199.mp4
```
if set video_dir = output_dir, then:
```
---video_dir/
------0001.mp4
------0002.mp4
...
------0199.mp4
------0001/
--------frames of video 0001.mp4
------0002/
--------frames of video 0002.mp4
...
------0199/
--------frames of video 0199.mp4
```