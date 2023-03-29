## Cognitive Computing - Automatic License Plate Recognition using OCR algorithms
![Project Workflow](https://i.imgur.com/8KRkaL3.png)

### Introduction
Public Kaggle Dataset: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

In this project, four different OCR (Optical Character Recognition) algorithms were used to compare and identify the best one for the dataset being used. The diagram below demonstrates the developed process to perform these comparisons and how the proposed workflow was implemented.

![Project's Diagram](https://i.imgur.com/bprM9GW.png)

Technologies: 

    - Python (Jupyter Lab)
    - OpenCV
    - YOLOv5
    - OCR Algorithms (EasyOCR, Pytesseract, KerasOCR)


### Challenges faced and solutions imposed
The project flow can be summarized into two scopes:

1. Receiving the dataset of car images and using edge detection with OCR to label the text of each car plate in a .csv file.
2. Receiving the dataset of car images and analyzing the plate of each one, performing a crop on the correct location using the YOLOv5 architecture and, after that, transcribing that image to text, saving the composition label of the car | car plate in .csv using different OCR techniques.

Therefore, the project would only be composed of the set -> edge detection + EasyOCR. However, as the project progressed, errors were noticed in both the car plate cropping and the OCR algorithm. In this sense, a new approach was tried to make this cropping more automated and correct. For this, YOLOv5 was used to make a more correct crop of these car plates, as well as other OCR techniques to improve the results.

However, only the new car plate cropping approach was not visually sufficient for the effectiveness and excellence of the supposed metrics and values. Therefore, two more OCR techniques were added, which were pytesseract and KerasOCR, both of which proved to be much better than EasyOCR. Between the two, KerasOCR is a much more meticulous algorithm, where it can analyze tiny details, which can be good from one perspective and bad from another, as it detects characters that are not theoretically relevant to the analysis of the plate, as well as understanding the spacing between words of the car plate better, causing the image-to-text transcription to go through a manipulation to be saved in CSV. On the other hand, Pytesseract, despite not being so meticulous in its detections, was the model that best fit and had the most accurate output for this project, in addition to being faster in response.

Finally, for the purpose of comparison between the techniques used, we conducted tests with 20 samples to evaluate the OCRs using WER (Word Error Rate) and CER (Character Error Rate).

### How to use the code:

#### Virtual Environment

```
# Windows

# Create conda environment and activate
conda create --name ocrproject python=3.7
conda activate ocrproject

# Install Libraries
pip install -r requirements.txt
```

#### Implementation

The code was built in Jupyter Lab, so we need to use it for some things in the code to work, such as creating directories, pytesseract configuration, etc.

This created class contains two proposed solutions:

```
1. More classical approach, using edge detection (OpenCV) to identify the car plates, and then using EasyOCR for image to text transcription.

    To use this solution, run this command below:

    *Remember that in these methods, you need the dataset with the original images, from the kaggle dataset provided.

    -> PlateRecognition().OpenCVeasy(path = "original_samples/", folder_name = "results", show_steps = False)

    where

        * path = location where the dataset was placed
        * folder_name = name of the folder that will be created and where the script results will be allocated
        * show_steps = good method for when using manual detection, where it can show step-by-step what is happening with the image to be transcribed. (opcional)
        * save_fig = save images with bounding boxes around detected license plates. (opcional)

2. The second solution uses YOLOv5, training the model and using YOLOv5's own resource to crop the images where the respective car plates are located. After that, there are three options for extracting the plate characters, using EasyOCR, Pytesseract or KerasOCR.

    To use this solution, you can use 3 types of OCR algorithms.

    *Remember that in these methods, you need the dataset with the properly cropped images, using helper/[yolo_cropped_images.ipynb] for this (yolov5 implementation). The output of this file will be the cropped images that will be used for these codes below:

    -> PlateRecognition().YOLOeasy(path = "cropped_samples/", folder_name = "results")

    -> PlateRecognition().YOLOpytesseract(path = "cropped_samples/", folder_name = "results")  

    -> PlateRecognition().YOLOkeras(path = "cropped_samples/", folder_name = "results") 

    where

        * path = location where the dataset was placed (in this case, it is already the result returned from the yolov5 crop, not the original dataset)
        * folder_name = name of the folder that will be created and where the script results will be allocated.
        * show_steps = good method for when using manual detection, where it can show step-by-step what is happening with the image to be transcribed. (opcional)
```

### Next steps

1. Perform pre-processing for image enhancement
2. Check for the existence of a better configuration for pytesseract (psm, oem, etc. parameters)
3. Compare OCR results with Machine Learning implementation








