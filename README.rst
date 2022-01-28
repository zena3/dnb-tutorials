=============
dnb-tutorials
=============

Package with data science tutorials and examples using public packages from github/DeNederlandscheBank.

* Free software: MIT/X license

Features
--------

Here is what the package contains:

* Tutorial Solvency 2 data. Application of some powerful machine learning algorithms using the public Solvency 2 data of all Dutch insurance undertakings. The Solvency 2 data of individual insurance undertakings are published yearly by the Statistics department of DNB. The data represents the financial and solvency situation of each insurance undertaking at the end of each year.|
* Tutorial ruleminer package. This packages enables you to automatically generate rules from arbitrary datasets and calculate a number of metrics. The tutorial shows how it works.
* Tutorial data-patterns package. Introduction to the use of the data-pattern package (an earlier version of rulemine).
* Tutorial nafigator package. This tutorial gives an introduction to the use of NLP Annotation Format, the format that we use to store (intermediate) results from our projects with Natural Language Processing.

If you have any questions in relation to these packages and tutorials, please contact w.j.willemse@dnb.nl

Installation
------------

Clone the project::

    git clone https://github.com/DeNederlandscheBank/dnb-tutorials.git

Install the required packages::

    pip install -r requirements.txt

This installs the packages that we use.

If you have trouble installing these requirements because of conflicts with existing packages then it may be advisable to create a new environment with::

	conda create --name your-env-name python=3.7

(python 3.7 is currently required because of matplotlib)

Activate this environment with::

	conda activate your-env-name

and run::

    pip install -r requirements.txt
