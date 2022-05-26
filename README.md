# Structure-based virtual screening for PD-L1 dimerizers is boosted by inactive-enriched machine-learning models exploiting patent data

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
![Python][python-shield]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/sawsimeon/MLSF-PDL1/blob/main/MLSF_PDL1_logo.png.png" alt="Logo" >
  </a>


  <p align="center">
    <span style="font-weight:bold; font-style:italic">Based on Patent Data </span> 
    <br />
    <br>
    <a href="https://academic.oup.com/bioinformatics/article/37/15/2134/6126797"><strong>Powered by DeepCoy Generator »</strong></a><br>
    <br />
    <br />

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#tools-used">Tools Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#conda">Create an environment and install all the dependencies</a></li>
        <li><a href="#clone">Clone the repo</a></li>
        <li><a href="#Running">Run the test set as sdf file</a></li>
      </ul>
    </li>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
We hypothesise that applying the latest advances observed in studies based on other targets will lead to highly accurate target-specific MLSFs for PDL1. For instance, a large number of decoys (assumed inactives) in the training set boosts SBVS performance of MLSFs, but this has never been investigated for PDL1. Thus, it is not known if training should be carried out with actives only, or supplementing the latter with experimentally validated inactives, property-matched decoys or random property-unmatched decoys. Likewise, regression-based MLSFs are still to be applied to PDL1 despite the dependent variable to predict, pIC50, being real-valued. This is probably due to the most popular SBVS benchmarks not having, by contrast, employed real-valued potency to evaluate performance, but only sets of actives and decoys with binary classification metrics. As a real-valued variable contains more information than any dichotomised version of that variable, it stands to reason that regression models should perform better than classification models, other things being equal. We will thus evaluate regression models that also exploit the information about the chemical diversity of inactives, which we call inactive-enriched regression-based ML SFs. Another novel aspect of our study is investigating which combinations of featurisation schemes and supervised learning algorithms are most predictive for SBVS on PDL1. 

### Tools Used

* [Python](https://www.python.org/)
* [Jupyter](https://jupyter.org/)
* [R](https://www.r-project.org/)




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running make sure that you have installed **Anaconda** on your machine. If not check the link of installation: https://docs.anaconda.com/anaconda/install/index.html 

## 1. <span id="conda">Create a miniconda environment</span> 
* Create an environment and install all the dependencies with a Python version 3.6

```{sh}
conda create --name <envname> --file requirements.txt python=3.6
```
when the installation is done activate the environment
```{sh}
conda activate <env_name>
```

## 2. <span id="clone">Clone the repository</span>  

  ```sh
  git clone https://github.com/sawsimeon/MLSF-PDL1.git
  
  cd MLSF-PDL1
  ```

## 3. <span id="Running">Run the Test Set</span>
   ```sh
   python script/DeepCoys.py
   python script/True_Inactives.py
   ```

## Saved Models
  
Selected SFs, including GRID SVM SF build from training actives + RandomDecoys and also training actives + TrueInactives were saved as pickle files in [here](https://github.com/sawsimeon/MLSF-PDL1/tree/main/models). The [notebook folder](https://github.com/sawsimeon/MLSF-PDL1/tree/main/notebooks) contains jupyter notebooks and resultings HTML files for obtaining the PR-AUC on these two test set TrueInactives and DeepCoys. We have also added these SFs trained on all actives and these same inactives + script to generate features for other docked complexes. This is to be able to use the SFs on other docked molecules. Please see the [data folder](https://github.com/sawsimeon/MLSF-PDL1/tree/main/data).  


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact


saw.simeon@inserm.fr






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-shield]:https://img.shields.io/badge/Python-3.6-blue?style=for-the-badge&logo=python
[license-shield]: https://img.shields.io/badge/django-3.0.3-blue?style=for-the-badge&logo=django
[license-url]: https://www.djangoproject.com/
[linkedin-shield]:https://img.shields.io/badge/Bootstrap-4-blue?style=for-the-badge&logo=bootstrap
[linkedin-url]: https://getbootstrap.com/
[jquery]: https://img.shields.io/badge/jquery-blue?style=for-the-badge&logo=jquery
[jquery-url]: https://jquery.com/
[product-screenshot]: images/screenshot.png
