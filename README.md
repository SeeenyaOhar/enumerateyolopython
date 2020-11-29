# Enumerate Yolo

This tool is used to data preperation for YOLOV3 image recognition training.

# Usage 

`enumerateyolo {data_path} {save_txt_file_path} {limiter}`
where 
`data_path` is the path of the data,
`save_txt_file_path` is where the output file will be created, 
`limiter` is the number of nodes in the output strings(starting from the file name)
For example: 
`data\obj\7513062eb6bf0f06d20230aef126b5dc.jpg` is a string with a `limiter` number 3
`obj\7513062eb6bf0f06d20230aef126b5dc.jpg` is a string with a `limiter` number 2

Real example:
`python enumerateyolo.py "E:\Documents\NumberPlate\obj" "E:\Documents\NumberPlate\txt.txt" 2`
