# Breast Cancer Detection in Mammograms using Deep Neural Networks

## Abstract

Breast cancer has become the most common form of cancer in Indian, recently having over- taken cervical cancer in urban cities. Immense research has been carried out on breast cancer and several automated machines for detection have been formed, however, they are far from perfection and medical assessments need more reliable services. Also, very little research has been performed on Indian datasets, which are significantly different than the available foreign resources. Indian breasts are more dense and hence differ in texture, lesion size and com- position. Our works aims to reproduce the state of the art results reported by researchers using deep learning approaches to automate breast cancer detection and extend them to build deep learning breast cancer detection networks which are more specific to Indian breast types and alongside use metadata of age, breast density, past history and other available informa- tion to enable more accurate judgement and treatment. Working in close collaboration with a radiologist from AIIMS Delhi, our work develops alternative object detection frameworks, ensemble and transformer networks to improve and enhance both classification and detection of breast lesions. Various analysis technique have been applied to measure performance and conduct thorough investigation of our experiments.

## Acknowledgments

We thank Prof. Chetan Arora for giving us this project and providing us the guidance and support for all our work. We also thank Prof. Subhashis Banerjee for the insightful discussions and his continuous advice. We express our gratitude towards Dr. Krithika Rangarajan for constantly being there to help us and enabling us to learn and appreciate the field.

## Problem Statement

Breast cancer impacts nearly 1.5 million women in all over the world each year and causes the greatest number of cancer-related death of women. Trends say 1 in every 8 women will be diag- nosed with breast cancer in her lifetime. Breast cancer has become the most common form of cancer in Indian urban cities, recently having overtaken cervical cancer and 2nd most common in rural India. There has been a shocking increase in the number of cases affecting women at a much younger age than 25 years ago. Most women today in India fall pray to breast cancer at around their 40s, which is much younger than when cancer hits in foreign countries.

The major causes of breast cancer are mostly genetic - damaged DNA and family history. However, other risk factors can be lifestyle or environmental related, like alcohol consumption - studies reveal that women who consume 3 drinks a day have a 1.5 times higher chance of being affected, obesity, hormonal treatments - an increased level of estrogen due to hormone replace- ment therapy of birth control pills can link to breast cancer, sedentary life without physical exercise. Other reasons such as bearing a child late in life or improper breastfeeding may also be responsible.
However, the biggest reasons are the lack of awareness, treatment and screening methods. Non availability of expert radiologists and diagnostic centres and delay in extending necessary care is a major concern. In an attempt to assist this growing cause, we aim to develop deep learning models to detect suspicious lesions and hence provide timely and effective diagnosis.

One may argue that immense research has been carried out on breast cancer and similar learning machines have been developed in the past. However, we found that although these machines exist, they are far from perfection and medical assessments need more reliable services. Also, very little research has been performed on Indian datasets. Most results and infact all datasets too, are only available for foreign patients. We notice several variations in the breast develop- ment and structure of Indian women including age difference when cancer initiates and breast tissues - Indian breasts are more fibrous, hence whiter and denser. We therefore feel that the same networks when applied on Indian cases cannot yield accurate information.

Our aim is to build deep learning breast cancer detection models which are more specific to Indian breast types and alongside use metadata of age, breast density, past history and other available information to enable more accurate judgement and treatment.

## Datasets

### DDSM
The DDSM (Digital Database for Screening Mammography) dataset is one of the most famous databases for breast mammographic research. It is a resource popularly used by the entire mammographic image analysis research community. Primary support for this project was a grant from the Breast Cancer Research Program of the U.S. Army Medical Research and Materiel Command. The Massachusetts General Hospital, the University of South Florida, and Sandia National Laboratories have also contributed. Additional cases were provided from Washington University School of Medicine. The dataset contains nearly 2500 studies with 12 volumes of normal images, containing 695 cases; 15 volumes of cancerous, containing 855 cases; 14 volumes benign, containing 870 cases; and 2 volumes of benign without callback, containing 141 cases.

### INbreast
The INbreast database is a mammographic database, with images ac- quired at a Breast Centre, located in a University Hospital (Hospital de So Joo, Breast Centre, Porto, Portugal). INbreast has a total of 115 cases (410 images), out of which 90 cases are of women from both breasts (4 images per case) and 25 cases are from mastectomy patients (2 images per case). Several types of lesions (masses, calcifications, asymmetries, and distortions) are included. Accurate contours made by specialists are also provided in XML format. The dataset was acquired on request from the owners.

### Indian AIIMS Dataset

A professional radiologist from AIIMS, is part of our project. She provided us with the AIIMS dataset. However, since these images were unannotated, she an- notated nearly 3000 images for us. Annotations were done in three ways - as per the BIRADS scoring, as per mass or calcification, as per actionable or non-actionable. The images were in .dicom and were converted to .png. Annotations were obtained in an xml file in PASCAL VOC format. We experimented with all sizes of lesions, small masses, large masses, calcification spots, clusters and node lesions.

## Proposed Network 1

Since a single model indicated a strong ability to detect masses but were not sufficient for detection of calcifications which are much smaller and very different as compared to masses. We hence concluded that the same model cannot generalize to detect both masses and calcification. To address this problem, we developed an expert - discriminator network which trains two experts - one for masses and the other for calcifications. Both the experts were trained using the same faster RCNN framework, the only difference was that the loss terms were considered only for masses in the first expert and only for calcifications in the second. The aim was to overfit the one on masses and the other on calcifications so that the two units together are able to detect both types of lesions with high accuracy.
Post training, when a new image is to be processed, it is sent through the two experts which will both perform their detections. The max scores from the two models is picked and those predictions are made.

!(/images/proposed1)

## Sanity Check

An important consideration to make while evaluating the obtained results is to ensure they are obtained as expected and are thus consistent with out understanding of the network’s working. For this, we needed methods to ensure that the important information in the image which is yielding the predictions is indeed coming the same area of the image which has the object and not from some other unrelated part in the image. For this, we need to check the attention maps produced by the network and analyze the salient regions. For this we attempted several different techniques - Making CAMS, GRADCAMs, performing sliding window analysis and perturbation analysis.

### GRADCAM

Compared to CAM, GradCAM doesn’t require feature maps to be directly before the softmax layers like in the case of CAM. Due to this reason, CAM is only applicable for specific types of Neural Nets while GradCAM are a generalisation to CAM and can be used with a variety of CNNs. The algorithm steps are briefly as follows: Gradients of the score(before the soft- max layer) for the chosen class C are computed: yc with respect to feature map Ak of the last conv layer. Gradients are global average pooled (mean over all the gradients calculated for every position of the map) to get weights Bk. This weight Bk captures the importance of the feature map k for a target class c. Weighted sum of the feature maps (where the weight for the kth feature map is Bk calculated in the previous step). Finally this map is passed through the Relu function to remove the negative pixels as they belong to the classes not in consideration.

We tried to implement the GradCAM for Faster-RCNN visualization. However, the atten- tion regions were not consistent with where the object was in the image. We could also not find any other resources where GradCAM has been implemented for Faster-RCNN to validate our steps. We suspect the reason for inconsistent CAMs could be the intermediate Region Proposal Network (RPN), which could be leading to incorrect gradient calculation. The gradient is cal- culated for the score for a class with respect to the feature map of the last conv layer, but here since they are separated by the RPN, we are unsure if it can yield the same performance as in a classification network.

Since our aim is to verify that Faster-RCNN does have localization capabilities, we have tried 3 other different methods for the same using occluded regions - where we blacken our parts of the input image and analyze the changes. Our hypothesis is that if blackening out a certain region of the image is causing major changes in the predicted boxes/confidences, then that region was salient and important for the task.

## Perturbation Technique - I

Take an image and make occlusions on the image in a sliding window style where the window is of 3 scales or sizes, approximately 1000-2000 images per test image depending on the size of the image. Run these images through the Faster-RCNN model. First did this for normal images like cats and dogs and ran it through FRCNN trained on VOC. Once we get the predictions for these images, for each pixel in the image we calculate a score. This score is the sum of the confidence scores of the bounding boxes in which the pixel is present. Then we normalize these scores and make a heat map. We got the following heatmaps for cat, dog, and breast:

!(/images/cat1)
!(/images/dog1)
!(/images/breast1)

## Perturbation Technique - II

The above procedure has certain flaws which are eradicated in the perturbation technique II: The same procedure as above is followed initially; do the occlusions and get the predictions of these occluded images. Then we output the predictions of the original non-occluded images using FRCNN pretrained model. Then for each occluded image, we calculate the IOU between the predicted bounding box of that image and the predicted bounding box of the original image. We then add value : 1-IOU, to all the pixels within the occluded region. The reason for doing this is that if the IOU is high, that means that the occlusion didnt result in any change, thus the occluded region didnt have any attention. Whereas on the other hand if the IOU is low, that means that occlusion affected the prediction and hence is comprised of the attention region. If for a given occluded image there is no prediction, IOU =0. Finally we take this heatmap and normalize it and super-impose on the original image. Here are the results for normal images(using model trained on VOC) and breast images, using pretrained FRCNN model and Retinanet:

!(/images/breast2)
!(/images/breast3)

## Proposed Network 2

After some analysis of the false positives and false negatives from the various testing datasets we used, we found out that in most of the cases the misses were in breasts which were dense. After performing experiments on mass vs calcification performance we realised that the shortcoming is not in separately identifying mass and calcifications, but in lesions belonging to breasts of different densities. Particularly, it was noticed that obscure masses often hidden in the fibro- grandular tissure were undetected. To tackle this problem, we hypothesized that if the dense tissues are normalised using an intensity transformation, the results may improve. Therefore we designed a network for density contrast modification. Our hypothesis was backed by the results presented in the paper: Photometric Transformer Networks and Label Adjustment for Breast Density Prediction.

!(/images/proposed2)

We use Photometric Tranformer Network to normalise the intensity of the images and hence reduce the deviation in the density of the breasts. For doing so, we designed a 5 layered Convolutional Neural Network with a 10 softmax outputs (S). These are the k=10 parameters which will be used in the function ’h’ to transform the input images. The authors introduce a function h, which uses k parameters. These k parameters and the function h is used to transform the input image and normalise it’s density. This neural network is trained on the fly with the Retinanet. As the function h is continuous and differentiable at all points, the loss can be fully back-propagated.


