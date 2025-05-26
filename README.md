Heart Disease Prediction

A machine learning project for predicting the presence of heart disease using patient data and a logistic regression model. This repository contains the Jupyter Notebook for model development and the dataset used for training and evaluation.

Table of Contents

Overview

Project Structure

Dataset

Features Used

Model and Methodology

Usage

Results


OVERVIEW

This project aims to predict whether a patient has heart disease based on various medical attributes. Using a Logistic Regression model, the project demonstrates the process of data loading, preprocessing, model training, and evaluation in a reproducible Jupyter Notebook.

PROJECT STRUCTURE

├── HeartDiseasePrediction.ipynb   # Jupyter Notebook with code and explanations

├── heart_disease_data.csv         # Dataset used for training and testing



DATASET


File: heart_disease_data.csv

Source: UCI Heart Disease dataset

Records: 303

Attributes:

age: Age of the patient

sex: Sex (1 = male; 0 = female)

cp: Chest pain type (0-3)

trestbps: Resting blood pressure (mm Hg)

chol: Serum cholesterol (mg/dl)

fbs: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

restecg: Resting electrocardiographic results (0-2)

thalach: Maximum heart rate achieved

exang: Exercise induced angina (1 = yes; 0 = no)

oldpeak: ST depression induced by exercise

slope: Slope of the peak exercise ST segment (0-2)

ca: Number of major vessels (0-3) colored by fluoroscopy

thal: Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)

target: 1 = presence of heart disease, 0 = absence




FEATURE USED


All columns except target are used as features for prediction. The target column is the label.



MODEL and METHODOLOGY


Model: Logistic Regression (from scikit-learn)

Workflow:

Data loading and inspection

Splitting data into training and testing sets

Model training using logistic regression

Model evaluation using accuracy score



USAGE


Open the notebook and follow the step-by-step instructions.

The notebook loads the dataset, preprocesses the data, trains a logistic regression model, and evaluates its performance.

You can modify the code to experiment with other models or preprocessing steps.



RESULT


The model is evaluated using accuracy score.

Example output:

Accuracy: (as calculated in the notebook; see output cells for results)

