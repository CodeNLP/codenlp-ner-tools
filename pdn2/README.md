# About

This repo demonstrate how to used PolDeepNer2 to recognize named entities using the state-of-the-art pre-trained models based on transformers.

# Contact

Michał Marcińczuk, CodeNLP <marcinczuk@gmail.com> 

# Installation

```bash
pip install -r requirements.txt
```

# Models

## KPWr

Link: https://drive.google.com/file/d/1v25pBBwlGvyMX-no1bDj0PlM-p0DBLyc/view?usp=drive_link

```bash
unzip pdn2_kpwr_ner_n82_0.8.1.zip
```

## CEN

Link: https://drive.google.com/file/d/1OGFYX8_Y9tJlmrtMooTWApbkmCc2eb1W/view?usp=sharing

```bash
unzip pdn2_cen_ner_n82_0.8.1.zip
```

# Usage

See the `demo.py` script.

```bash
python demo.py
```

Expected output:
```
python demo.py 

Model metadata
--------------
author     : Michał Marcińczuk, CodeNLP
contact    : marcinczuk@gmail.com
description: Model trained on the KPWr corpus recognizes 82 types of nested entities.
reference  : https://www.sciencedirect.com/science/article/pii/S1877050921015179
score      : F1=80.29 on the KPWr test subset (micro avg, strict evaluation).

[24:29] Chiny (nam_loc_gpe_country)
[32:40] Brazylia (nam_loc_gpe_country)
[111:132] dolara amerykańskiego (nam_oth_currency)
```
