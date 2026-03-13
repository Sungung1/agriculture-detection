# Agriculture Detection

## Overview

Agriculture Detection is a crop-analysis prototype that combines an agriculture-themed web interface with an image-upload workflow for future plant-health or disease-detection models.

## Tech Stack

- Python
- Flask
- HTML/CSS/JavaScript
- Bootstrap

## Architecture

Input crop image -> Detection pipeline -> Analysis processing -> Advisory output

## Usage

```bash
pip install -r requirements.txt
python train.py
python inference.py
```

## Results

This repository currently serves as a deployable product prototype. The upload flow and page templates are in place so model outputs can be connected without redesigning the frontend.
