# PROJECTS GUIDELINES

In this repository you can find the main projects link to udacity self-driving car nano degrees. Repository is divided in the following projects. To run the project files it's required to create an .env in your machine. 


# UDACITY Project

In this project I will explain how I completed all the different projects for the SELF DRVING CAR ENGINEERING nanodegree. 

## COMPUTER VISION
This part focus on the camera sensor and how to process raw digital images before feedigh them into different algorithms, such as neural networks. We will build convolutional neural networks using AWS TensorFlow and learn how to classify and detect objects in images. We will learn Machine learning workflow and their basics. 

AWS services are costly and complicated to use, for that reason I've started using OPENCV framework to detect cars and then PYTORCH to learn how to create models from data. Finally, I've used a tensorflow model to identify objects in images. 


## SENSOR FUSION
Detect objects in a 3D lidar point cloud using a deep-learning approach, and then evaluate detection performance using a set of metrics. How to fuse camera and lidar detections and track objects over time with an Extended Kalman Filter. Finally, hands-on experience with multi-target tracking, where you will initializer, update and delete tracks, assign measurements to tracks with data association techniques, and manage several tracks simultaneously.  



## LOCALIZATION
All about robotic localization, from one-dimensional motion models up to using three-dimensional point cloud maps obtained from lidar sensors. Implementing the bicycle motion model, an approach to use simple motion to estimate location at the next time step, before gathering sensor data. In order to do 1D object tracking we will use Markov localization. From there we will implement two scan matching algorithms, Iterative Closest Point (ICP) and Normal Distributions Transform (NDP), which work with 2D and 3D data. Finally, you will utilize these scan mathing algorithms in the Point Cloud Library (PCL) to localize a simulated car with lidar sensing, using a 3D point cloud map obtained from the CARLA simulator.



## PLANNING
Applying model-driven and data-driven approaches to predict how oterh vehicles on the road will behave. You'll construct a finite state machine to decide which of several maneuvers your own vehicle should undertake. Finally, a safe and comfortable trajectory to execute a maneuver will be generated. 


## CONTROL
How to activate the throttle and the steering wheel of the car to move it following a trajectory described by coordinates. We will cover the most basic but also the most common controller: the Proportional Integral Derivative or PID controller. 


# CREATE ENVIRONMENT

1 - Create a virtual environment: Open terminal and run using conda: ‘ conda create --name myenv python=3.x ‘ You can replace ‘ myenv ‘ with your chosen name and python version you prefer. 

2 - Activate the environment in terminal for windows using  ‘ myenv\Scripts\activate ‘ and for macOS and Linus use source activate myenv. For that, you need to be in the right folder. 

3 - Run next folder to ensure environment is working: 01_ObjectDetection -> OPENCV_ImageObjectDetection.py which will run OPENCV from conda enviroment. You should see next results: 


## Notes

This scripts work under virtual enviorment .env with the following packages:

1. pip install pillow == 9.5.0
2. pip install opencv-python



