{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNUhKQTIEkrHv3fDTgsw1ml"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yhHKxrmBCVmt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ac03cee-0f84-4929-ce5f-a24a0dcad2e2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pydub"
      ],
      "metadata": {
        "id": "8BCwqOAPCazH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5f8d1cf4-681b-40ee-a057-81fbbaf542f9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pydub\n",
            "  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)\n",
            "Installing collected packages: pydub\n",
            "Successfully installed pydub-0.25.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pydub import AudioSegment\n",
        "import librosa\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "cCdc3sL-Cf01"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Stats:\n",
        "*   bellypain = 80\n",
        "*   burping = 40\n",
        "*   discomfort = 135\n",
        "*   hungry = 80\n",
        "*   tired = 80\n",
        "\n",
        "To bring uniformity, we will make all folders to have 80 audio files.\n",
        "All audios are longer than 5 seconds and maximum lie between 5-7 seconds\n",
        "Now, what to do is:\n",
        "*   For all folders except burping: We will extract starting 2.5 seconds of audio files and store them in the new location \n",
        "*   For burping: As its number is only 40, so to make them 80, we will extract starting 2.5 seconds as well as next 2.5 seconds of audio and store these two created files in the new location. This will result in 80 files of burping.\n",
        "\n",
        "We will also keep a check if files have not exceeded the count of 80 because discomfort has 135 files and we want only 80.\n",
        "\n",
        "The following function performs the above mentioned tasks:"
      ],
      "metadata": {
        "id": "KC3OvPRMF3_B"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def audioTrim(path, new_path, burpingt='False'):\n",
        "\n",
        "    count = 1\n",
        "    i = '000'   #To number the files of that folder\n",
        "\n",
        "    #files is the list of all audio files of the passed folder path\n",
        "    files = librosa.util.find_files(path)\n",
        "\n",
        "    for file in files:\n",
        "      #because we want to have 80 files of each folder\n",
        "      if count<81:\n",
        "        audio = AudioSegment.from_wav(file)\n",
        "        \n",
        "        #Extracting starting 2.5 seconds\n",
        "        start_sec = 0*1000\n",
        "        end_sec = 2.5*1000\n",
        "        extract = audio[start_sec:end_sec]\n",
        "        j = str(int('9' + i) + 1)[1:]           #To number the files of that folder\n",
        "        print(j)\n",
        "        name = new_path+j+\".wav\"\n",
        "        print(name)\n",
        "        extract.export(name, format=\"wav\")\n",
        "        i = j\n",
        "        if burpingt==True:\n",
        "          start_sec = 2.5*1000\n",
        "          end_sec = 5*1000\n",
        "          extract = audio[start_sec:end_sec]\n",
        "          j = str(int('9' + i) + 1)[1:]\n",
        "          print(j)\n",
        "          name = new_path+j+\".wav\"\n",
        "          print(name)\n",
        "          extract.export(name, format=\"wav\")\n",
        "          i = j\n",
        "        count = count+1"
      ],
      "metadata": {
        "id": "K4_pBhKcEUKb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/belly_pain\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/bellypain/\")\n",
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/burping\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/burping/\", True)\n",
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/discomfort\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/discomfort/\")\n",
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/hungry\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/\")\n",
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/tired\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/tired/\")"
      ],
      "metadata": {
        "id": "hN0pCxvfCfCd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "audioTrim(\"/content/drive/MyDrive/Cry_Clips/hungry\", \"/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SCTrwBNqyHkm",
        "outputId": "e26b649b-a39a-44b8-87a6-2a79c49b2fbd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "001\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/001.wav\n",
            "002\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/002.wav\n",
            "003\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/003.wav\n",
            "004\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/004.wav\n",
            "005\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/005.wav\n",
            "006\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/006.wav\n",
            "007\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/007.wav\n",
            "008\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/008.wav\n",
            "009\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/009.wav\n",
            "010\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/010.wav\n",
            "011\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/011.wav\n",
            "012\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/012.wav\n",
            "013\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/013.wav\n",
            "014\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/014.wav\n",
            "015\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/015.wav\n",
            "016\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/016.wav\n",
            "017\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/017.wav\n",
            "018\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/018.wav\n",
            "019\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/019.wav\n",
            "020\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/020.wav\n",
            "021\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/021.wav\n",
            "022\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/022.wav\n",
            "023\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/023.wav\n",
            "024\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/024.wav\n",
            "025\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/025.wav\n",
            "026\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/026.wav\n",
            "027\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/027.wav\n",
            "028\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/028.wav\n",
            "029\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/029.wav\n",
            "030\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/030.wav\n",
            "031\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/031.wav\n",
            "032\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/032.wav\n",
            "033\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/033.wav\n",
            "034\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/034.wav\n",
            "035\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/035.wav\n",
            "036\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/036.wav\n",
            "037\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/037.wav\n",
            "038\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/038.wav\n",
            "039\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/039.wav\n",
            "040\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/040.wav\n",
            "041\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/041.wav\n",
            "042\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/042.wav\n",
            "043\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/043.wav\n",
            "044\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/044.wav\n",
            "045\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/045.wav\n",
            "046\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/046.wav\n",
            "047\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/047.wav\n",
            "048\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/048.wav\n",
            "049\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/049.wav\n",
            "050\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/050.wav\n",
            "051\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/051.wav\n",
            "052\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/052.wav\n",
            "053\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/053.wav\n",
            "054\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/054.wav\n",
            "055\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/055.wav\n",
            "056\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/056.wav\n",
            "057\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/057.wav\n",
            "058\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/058.wav\n",
            "059\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/059.wav\n",
            "060\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/060.wav\n",
            "061\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/061.wav\n",
            "062\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/062.wav\n",
            "063\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/063.wav\n",
            "064\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/064.wav\n",
            "065\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/065.wav\n",
            "066\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/066.wav\n",
            "067\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/067.wav\n",
            "068\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/068.wav\n",
            "069\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/069.wav\n",
            "070\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/070.wav\n",
            "071\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/071.wav\n",
            "072\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/072.wav\n",
            "073\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/073.wav\n",
            "074\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/074.wav\n",
            "075\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/075.wav\n",
            "076\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/076.wav\n",
            "077\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/077.wav\n",
            "078\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/078.wav\n",
            "079\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/079.wav\n",
            "080\n",
            "/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry/080.wav\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "files = librosa.util.find_files('/content/drive/MyDrive/Baby Cry Project/Cry Clips/hungry')\n",
        "len(files)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PLKoaWvayLwX",
        "outputId": "8161b430-7ad0-4424-a878-78885fc0f28e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "80"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "zl38j4Uc-6vn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}