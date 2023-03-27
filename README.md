
# <h1 align=center>Baby-Cry-Project</h1>

<p align="center">
  <img width='300' height='250' src='/Assets/Namaste.jpg'> 
</p>

I developed this project along with my peer during my 6 months internship at IIT Jammu. Baby Cry Project is developed using ML and Deep Learning models to classify the baby cry into 5 different categories viz. bellypain, burping, discomfort, hungry and tired.

## Data Collection 
We have taken the data from donateacry and we have also collected real time data from the hospitals and parents.

### **Statistics of data :**

  + bellypain = 80
  + burping = 40
  + discomfort = 135
  + hungry = 80
  + tired = 80
  
## **Data Preparation**  
This module is coded to bring uniformity in data in order to prepare it for training.
To bring uniformity, we will make all folders to have 80 audio files. All audios are longer than 5 seconds and maximum lie between 5-7 seconds Now, what to do is:

  + For all folders except burping: We will extract starting 2.5 seconds of audio files and store them in the new location
  + For burping: As its number is only 40, so to make them 80, we will extract starting 2.5 seconds as well as next 2.5 seconds of audio and store these two created       files in the new location. This will result in 80 files of burping.
  
We will also keep a check if files have not exceeded the count of 80 because discomfort has 135 files and we want only 80.

**Packages/Libraries Used :** from pydub AudioSegment, librosa, pandas <br>
 <a href='/Data Preparation.ipynb'> <strong> <em> Visit Module </strong> </em> </a>
 
 <hr>
 
 We have trained two models for this project:
  1. **Naive Bayes Classifier** : This was to dip our hands in ML
  2. **Neural Network** : To get ourselves completely drenched in ML and Deep Learning
