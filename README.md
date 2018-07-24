# YOLO-LITE
YOLO-LITE is a web implementation of YOLOv2-tiny trained on MS COCO 2014 and PASCAL VOC 2007 + 2012. All the trained models (cfg and weights files) used while developing YOLO-LITE are here. Our goal is to create an architecture that can do real-time object detection at a speed of 10 FPS and a mean average precision of about 30% on a computer without a GPU.

# Demo
[Check out our models trained on COCO and VOC here.](https://reu2018dl.github.io/)

Below is the COCO YOLO-LITE model performing real-time object detecion at about 10 FPS from a Dell XPS 13 laptop:

![Real-time detection](https://github.com/rachuang22/tfjs-yolo-tiny-demo/raw/master/src/img/car.gif)

### Results

| DataSet       | mAP           | FPS   |
| ------------- |:-------------:| -----:|
| PASCAL VOC    | 33.57         |   21  |
| COCO          | 12.26         |   21  |

[best PASCAL cfg](https://github.com/reu2018DL/yolo-lite) |  [best PASCAL weights](https://github.com/reu2018DL/yolo-lite)

[best COCO cfg](https://github.com/reu2018DL/yolo-lite)   |  [best COCO weights](https://github.com/reu2018DL/yolo-lite)


*Note: FPS is calculated from runnig locally on a Dell XPS 13 laptop.

# Get Started

### Training
We used AlexeyAB's Darknet for Windows to train our model.
Install Darknet [here](https://github.com/AlexeyAB/darknet).


To find the mAP for each training model, run the command under the scripts folder:

	python mapScript.py

When prompted, add the location of the cfg and the location of the weights folder.

<!--  Add weights script Description here -->

### Testing
In order to get the FPS, we used a Python adaptation of Darknet called Darkflow [here](https://github.com/thtrieu/darkflow/tree/master/darkflow).


### Web Implementation
1. To convert the model to JavaScript, we followed the following [tutorial](https://towardsdatascience.com/deep-learning-in-your-browser-a-brisk-guide-ca06c2198846).

2. Once converted to the JavaScript, refer to our two repositories of [tfjs-yolo-tiny](https://github.com/rachuang22/tfjs-yolo-tiny) and [tfjs-yolo-tiny-demo](https://github.com/rachuang22/tfjs-yolo-tiny-demo).

3. Replace line 14 in `index_coco.js` and `index_voc.js` to a link from the resulting `.json` file in Step 2:

    ```javascript
    model = await downloadModel('put your link here');
    ```
    
  ### How to prune weights
  While we found that pruning weights by a simple threshold did not really effect the mAP or FPS somoene else may find this script useful.
  To prune a weights file navigate to the weights.py file then run
  
 
   ``` python weights.py WEIGHTS_FILE_NAME THRESHOLD ```
  
