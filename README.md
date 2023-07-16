
# <h1 align=center>Baby-Cry-Project</h1>

<p align="center">
  <img width='300' height='250' src='/Assets/Namaste.jpg'> 
</p>

I developed this project along with my peer during my 6 months internship at IIT Jammu. Baby Cry Classifier is built using ML and Deep Learning models to classify the baby cry into 5 different categories viz. bellypain, burping, discomfort, hungry and tired.

## Data Collection 
Data is in the form of audio files. We have taken the data from donateacry and we have also collected real-time data from the hospitals and parents.

### **Statistics of data:**

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
  
  ## **Features Extraction**  
  This module is for extracting features for Naive Bayes Classifier.<br>
  For Naive Bayes Model, features extracted are:
   + rms energy: Root Mean Square of energy is equals to sqrt(sum(energy**2))/len(energy))
   + zcr: Zero Cross Rate is the rate at which a signal changes from positive to zero to negative or from negative to zero to positive. In simpler words, it's the rate at which the signal passes through the origin.
   
   After extracting features, these features will be used to create the dataframe.<br>
   Dataframe has the following columns:
    <ul>
  <li>Energy</li>
  <li>ZCr</li>
  <li>label</li>
    </ul>
    
   Each category is assigned an integer which is the label for that category.
   <ul>
   <li> bellypain - 1 </li>
   <li> burping - 2 </li>
   <li> discomfort - 3  </li>
   <li> hungry - 4  </li>
   <li> tired - 5 </li>
    </ul>
    
   After that dataframe is converted to an excel sheet.<br>
   Also, data is split into train and test dataset. For that I have made the use of dataframe.drop function.
   For test data, 15 random samples have been taken from each category.
   
   Finally, train dataframe and test dataframe are converted to excel sheet.
   
   **Packages/Libraries Used :** numpy, librosa, pandas, math <br>
   <a href='/Features Extraction.ipynb'> <strong> <em> Visit Module </strong> </em> </a>
   
  ## **Naive Bayes Classifier**
  This module contains the code for Naive Bayes Classifier. It is divided into 5 steps. <br>
   **STEP 1**: READING EXCEL SHEETS <br>
   **STEP 2**: DERIVING STATISTICS(mean, std. deviation, length) OF COLUMNS - ENERGY & ZCR TO SUMMARIZE DATASET <br>
   **STEP 3**: SUMMARIZE DATASET BY CLASS <br>
   **STEP 4**: CALCULATING GAUSSIAN PROBABILITY DISTRIBUTION FUNCTION <br>
   **STEP 5**: CALCULATE PROBABILITIES <br>
       1. Calculate Class prob. i.e. P(class) = Rows in class / Total Rows in training Dataset <br>
       2. Calculate Prob. for each input value in the row using the Gaussian probability density function and the statistics for that column and of that class <br>
    
   **Packages/Libraries Used :** numpy, librosa, pandas, math <br>
   <a href='/Naive Bayes Classifier.ipynb'> <strong> <em> Visit Module </strong> </em> </a>
   
   
   Accuracy is not much impressive. It's just 50.667%. <br>
   So, we decided to use the Neural Network for  classification.
   
  ## **Naive Bayes Classifier**
  This module contains the code for Classification using Sequential Neural Network. 
  
  It has five layers. First four layers have relu activation function and fifth layer has the softmax activation function.
  
  Firstly, features are extracted. Features extracted are MFCC.
  Mel-frequency cepstral coefficients (MFCCs) are coefficients that collectively make up an MFC. For that I have used librosa.feature.mfcc(). It will return 125   MFCCs.
  
  Then these features are fed into the neural network. It is trained for 3000 epochs.
  
  
  **Packages/Libraries Used :** numpy, librosa, pandas, math, keras, tensorflow <br>
   <a href='/Neural Network.ipynb'> <strong> <em> Visit Module </strong> </em> </a>
   
   
   Accuracy is 83.529%. It's much impressive for this size of data. <br>
  
    
