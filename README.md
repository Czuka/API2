# API2

This API allows you to interact with Creo Parametric using the Creoson library and CreoSetup.

## Prerequisites

- Creo Parametric with actual licence installed on your device.
- Python 3.x installed.
- Creoson library installed. You can install it using pip:

1. Clone this repository to your local machine:
   
2. Install the required dependencies:

3. Start CreoSon Setup conected to localization of Common Files in directory instalation of Creo Parametric

4. Run the main with seted correct path to directories:
   pathToCreoRunBat = C://...path to creo directories .../PTC/Creo 7.0.1.0/Parametric/bin/parametric.bat
   pathToCreoMaterials = C://...path to creo directories .../PTC/Creo 7.0.1.0/Common Files//text/materials-library/Standard-Materials_Granta-Design/Ferrous_metals//
   workingDirectory = C:\... path to directory creo model with paterns
   modelFile = projekcik.prt  -name of your template project

   -in case of error you should restart CreoSon Setup

# Project objectives

The objective of this project is to create an API that controls the Creo Parametric with Creoson library to automate and speed up the process of creating shelf support models ready for further strength calculations. 


