# YOLO-LITE
All the trained models used while developing YOLO-LITE

# Demo
[Check out our models trained on COCO and VOC here.](https://reu2018dl.github.io/)

Below is the COCO YOLO-LITE model performing real-time object detecion at about 10 FPS from a Dell XPS 13 laptop:

![Real-time detection](https://github.com/rachuang22/tfjs-yolo-tiny-demo/raw/master/src/img/car.gif)

### Results

| DataSet       | mAP           | FPS   |
| ------------- |:-------------:| -----:|
| PASCAL VOC    | 33.57         |   21  |
| COCO          | 12.26         |   21  |


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
In order to get the FPS, we used a Python adaption of Darknet called Darkflow [here](https://github.com/thtrieu/darkflow/tree/master/darkflow).


### Web Implementation
1. To convert the model to JavaScript, we followed the following [tutorial](https://towardsdatascience.com/deep-learning-in-your-browser-a-brisk-guide-ca06c2198846).

2. Once converted to the JavaScript, refer to our two repositories of [tfjs-yolo-tiny](https://github.com/rachuang22/tfjs-yolo-tiny) and [tfjs-yolo-tiny-demo](https://github.com/rachuang22/tfjs-yolo-tiny-demo).

3. Replace line 14 in `index_coco.js` and `index_voc.js` to a link to the resulting `.json` file from step 2.