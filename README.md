# Digit Classifier 

## An application that can classify user-drawn digits, built using Python and [Teachable Machine](teachablemachine.withgoogle.com).

![two](https://user-images.githubusercontent.com/93237883/177375597-8cb85395-4dd7-4983-95b0-916575b04742.png)

![nine](https://user-images.githubusercontent.com/93237883/177375693-3533e982-d21c-435d-bb0b-cbb9feafb7ca.png)

## :grey_question: How to use it?
- Install Python Virtual Environment: ```pip install virtualenv```
- Make a new directory for the project 
- Activate the virtual environment: ```virtualenv digitclassifiier```, where _digitclassifier_ is the name of the virtual environment.
- Install all the project files from GitHub
- Install all required dependencies using: ```pip install -r requirements.txt```

## :white_flag: How does it work? 
- The application displays a window to accept a digit in your handwriting.
- You can press: **1 - to Clear Screen**, and **2 - to Run The Neural Network**.
- When the neural network is run, the application first takes a screenshot of the window with your handwriting.
- Next, it runs it against the neural network.
- It automatically selects the best match and presents it to you.
- You can now press 1 to clear screen and draw another digit.

[**NOTE**: Since the application uses a self-made model, with limited number of images, it is advisable to use _legible_ handwriting before running the model. Also, please try to draw digits towards the center of the application window.]
