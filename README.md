# Project Name
Lab 01. BMI category reporter

## Setup
conda create -n aigc5005-lab01 python=3.14.6 -y
conda activate aigc5005-lab01
pip install -r requirements.txt

## Run
python app.py

## Example
Enter your height in centimeter: 164
Enter your height in kg: 58

Your BMI is 21.6. This is usually classed as a Healthy weight.
This is great. Eating a healthy diet and being physically active are important for reducing your cancer risk, even at a healthy weight.

## Known limitations
Single-line input not supported: Height and weight must be entered separately rather than in a single line.
No input retry loop: When invalid input is entered, the program raises a `SystemExit` and terminates immediately instead of asking the user to re-enter the value.
