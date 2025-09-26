
# Spectrum Recovery 🌠

<p align = "center">
<img src = "https://wallpaperaccess.com/full/47178.jpg" width = "800" height = "300" />
</p>


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![GitHub top language](https://img.shields.io/github/languages/top/Alcatraz312/Spectrum-recovery)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Alcatraz312/Spectrum-recovery)

## Overview

When an exoplanet passes in front of its host star, a small amount of starlight filters through the planet's atmosphere. This technique, known as transit spectroscopy, enables researchers to analyze atmospheric composition. However, these signals are incredibly faint, often hidden by complex, time-dependent noise from both the instruments and the stars themselves.

This project focuses on recovering the true exoplanet spectrum from these noisy observations. This project was done as a part of [NeurIPS - Ariel Data Challenge 2025](https://www.kaggle.com/competitions/ariel-data-challenge-2025).

The stimulated data used for this project is from ESA's Ariel mission, which aims to characterize 1,000 exoplanets after its 2029 launch.
To know more about the project and its current status, check [Wiki](https://github.com/Alcatraz312/Spectrum-recovery/wiki)

## Getting Started

### Prerequisites

Before using the program, you will need the following: 

* Python version 3.10 or higher 
* Jupyter Notebook
* Account on [Kaggle](https://www.kaggle.com/)

### Installation

1. Fork and clone this GitHub repository to your local machine:

```python 
git clone https://github.com/<name>/Spectrum-recovery.git
```
2. Go inside the project directory:

```python
cd Spectrum-recovery
```
3. Create a virtual python environment for your project: 

```python
python -m venv <name of your environment>
```
4. Activate the virtual environment
* Linux:

```python
. <path_to_env>/bin/activate
```
* WSL:
```python
source <path_to_env>/bin/activate
```

* Windows (Powershell):

```python
<path_to_env>/Scripts/Activate.ps1
```

* Windows (Command Prompt):

```python
<path_to_env>/Scripts/Activate.bat
```

5. Upgrade pip to the latest version:

```python
python.exe -m pip install --Upgrade pip
```

6. Install the required python packages using pip:

```python
pip install -r requirements.txt
```

7. Login or create an account on [Kaggle](https://www.kaggle.com/) to get access to the dataset.

8. The data files and folders for this project are of a very large size.
So it is suggested that a kaggle notebook is created for working with the same.

## Contribution
1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes, and ensure that your code follows the PEP 8 style guide.

3. Write tests to cover your code if applicable.

4. Create a pull request with a clear description of your changes and why they are needed.

5. Your pull request will be reviewed, and once approved, it will be merged into the main branch.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Alcatraz312/Spectrum-recovery/blob/main/LICENSE) file for details.
