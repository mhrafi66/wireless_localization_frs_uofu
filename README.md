# Wireless Device Localization Dataset
# Dataset Description

This dataset contains a large-scale collection of measurements for RSS-based localization. The data was collected using the **POWDER Testbed** at the University of Utah and includes received signal strength (RSS) measurements with either 0, 1, or 2 active transmitters.

## Overview
- **Total Samples**: 5,214 unique samples  
- **Transmitter Locations**: 5,514 unique locations  
- **Receiver Count per Sample**: 10–25 receivers  

### Sample Distribution
| **Sample Type**    | **Count** | **Receiver Count** |
|---------------------|-----------|--------------------|
| No Transmitters     | 46        | 10–25             |
| 1 Transmitter       | 4,822     | 10–25             |
| 2 Transmitters      | 346       | 11–12             |

The transmitters are handheld walkie-talkies (Baofeng BF-F8HP) operating in the FRS/GMRS band at 462.7 MHz, with a rated transmission power of 1 W. The RSS values were derived from raw IQ samples processed through a 6 kHz bandpass filter to eliminate neighboring transmissions, and the RSS was calculated as follows:

$$RSS = \frac{10}{N} \log_{10}\left(\sum_{i=1}^N x_i^2 \right)$$

---

## Measurement Parameters
| **Parameter**        | **Value**               |
|-----------------------|-------------------------|
| Frequency            | 462.7 MHz              |
| Radio Gain           | 35 dB                  |
| Receiver Sample Rate | 2 MHz                  |
| Sample Length        | N = 10,000             |
| Band-pass Filter     | 6 kHz                  |
| Transmitters         | 0–2                    |
| Transmission Power   | 1 W                    |

### Receivers:
The receivers include **Ettus USRP X310 and B210 radios**, equipped with a mix of wide- and narrow-band antennas. RSS values are uncalibrated and only relative to the device, as no calibration data was available. Each receiver took measurements with a receiver gain of 35 dB. However, devices
have different maxmimum gain settings, and no calibration data was available, so
all RSS values in the dataset are uncalibrated, and are only relative to the device.

The majority of the receivers are stationary endpoints fixed on the side of buildings, on rooftop towers, or on free-standing poles. A small set of receivers are located on  shuttles which travel specific routes throughout campus.


---

## Folder Structure

```plaintext
dataset/
├── Full_Dataset/                    # Contains the full dataset in json format
│   └── powder_462.7_rss_data.json   # Main JSON file with all data
├── Separated_Dataset_CSV/           # Contains separated one and two transmitter in .csv format
│   ├── single_tx.csv				 # csv dataset only with one transmitters
|   ├── two_tx.csv					 # csv dataset only with two transmitters
│   └── location_coordinates.json        # Receivers names with respective coordinates ('None' for the receivers which are moving)
├── Separated_Dataset_JSON/          # Contains separated data files and splits in JSON format
│   ├── all_data/
│   │   ├── single_tx.json           # Samples with 1 transmitter
│   │   ├── no_tx.json               # Samples with 0 transmitters
│   │   └── double_tx.json           # Samples with 2 transmitters
│   ├── train_test_splits/
│   │   ├── random_split/
│   │   │   ├── train.json           # 80% training data
│   │   │   └── test.json            # 20% test data
│   │   ├── grid_split/
│   │   │   ├── train.json           # Grid-based training data
│   │   │   └── test.json            # Grid-based test data
│   │   ├── seasonal_split/
│   │   │   ├── april.json           # Data collected in April
│   │   │   ├── july.json            # Data collected in July
│   │   │   └── november.json        # Data collected in November
│   │   ├── special_test_cases/
│   │   │   ├── indoor.json          # Contains only indoor datasets
│   │   │   ├── off_campus.json      # Contains off campus data
│   │   │   ├── stationary0.json     # Dataset with stationary transmitters
│   │   │   ├── stationary1.json     
│   │   │   └── stationary2.json     
│   │   └── transportation_split/
│   │       ├── walking.json         # Samples with walking transmitters
│   │       ├── cycling.json         # Samples with cycling transmitters
│   │       └── driving.json         # Samples with driving transmitters
│   └── stationary/					 # Datasets with stationary transmitters
├── Maps/                             # Contains all the maps in .tif format
│   ├── dsm.tif                      # Digital Surface Model file
│   ├── corrected_dsm.tif            # Corrected DSM File of UofU RDZ 
│   └── corrected_buildings.tif      # Corrected DSM with corrected building height
├── location_indexes.json            # Contains all the receivers name with an index
└── README.md                        # Dataset description and usage instructions
```


## Dataset Structure

### Data Format
The dataset is provided in both `.json` and `.csv` format, both as a single file and as split files.

### .json Structure

Below is a sample JSON sample of two transmitter case:

```json
{
  "2022-04-25 14:11:02": {
    "rx_data": [
      [
        -75.14881216502957,
        40.76695251464844,
        -111.85211944580078,
        "bus-4603"
      ],
      [
        -72.76890586248369,
        40.772705078125,
        -111.83783721923828,
        "bus-6183"
      ],
      [
        -66.9426657074761,
        40.76134,
        -111.84629,
        "cbrssdr1-bes-comp"
      ],
      [
        -82.52322009127514,
        40.7644,
        -111.83699,
        "cbrssdr1-honors-comp"
      ],
      [
        -68.77001181251623,
        40.77105,
        -111.83712,
        "cbrssdr1-hospital-comp"
      ],
      [
        -64.15222248890146,
        40.76895,
        -111.84167,
        "cbrssdr1-ustar-comp"
      ],
      [
        -68.39949252257873,
        40.7677,
        -111.83816,
        "ebc-nuc1-b210"
      ],
      [
        -78.83858666321109,
        40.76148,
        -111.84201,
        "garage-nuc1-b210"
      ],
      [
        -84.66956126342163,
        40.76627,
        -111.83632,
        "guesthouse-nuc2-b210"
      ],
      [
        -95.0148341336122,
        40.7616,
        -111.85185,
        "law73-nuc1-b210"
      ],
      [
        -91.05168678465658,
        40.75786,
        -111.83634,
        "madsen-nuc1-b210"
      ],
      [
        -82.40519021775879,
        40.76278,
        -111.83061,
        "sagepoint-nuc1-b210"
      ]
    ],
    "tx_coords": [
      [
        40.76778075,
        -111.84686963
      ],
      [
        40.76935595,
        -111.84657217
      ]
    ],
    "metadata": [
      {
        "power": 1,
        "transport": "walking",
        "radio": "TXA"
      },
      {
        "power": 1,
        "transport": "driving",
        "radio": "TXB"
      }
    ]
  }
}
```

- `rx_data`: A list of RSS data from each receiver, including RSS value, latitude, longitude, and device name.
- `tx_coords`: Coordinates (latitude and longitude) for each transmitter.
- `metadata`: Metadata for each transmitter, aligned with tx_coords.

**How to Load Data in Python**:
```python
import json

data_file = 'powder_462.7_rss_data.json'
with open(data_file) as f:
    data = json.load(f)
```

### .csv Structure
The Dataset also contains `single_tx.csv` and `two_tx.csv` files. This is the `csv` format representation of original `json` dataset. The columns of these two datasets are `timestamp`, `rss` values of each receiver nodes and the coordinates of the transmitters. A separate file `location_coordinates.json` contains the coordinates of all the **stationary** receiver nodes. For the moveable receivers (name starts with 'bus'), two columns in the `.csv` file includes the latitude and longtitude of a moveable node. Therefore, in the `.csv` files, there is three columns for each of the moveable receiver node with `rss` value, `x` coordinate and `y` coordinate of the node. 

# Digital Surface Model
The dataset includes a digital surface model (DSM) from a State of Utah 2013-2014 LiDAR [survey](https://doi.org/10.5069/G9TH8JNQ). This
map includes the University of Utah campus and surrounding area.
The DSM includes buildings and trees, unlike some digital elevation models.

To read the data in python:
```
import rasterio as rio
import numpy as np
import utm

dsm_object = rio.open('dsm.tif')
dsm_map = dsm_object.read(1)     # a np.array containing elevation values
dsm_resolution = dsm_object.res     # a tuple containing x,y resolution (0.5 meters) 
dsm_transform = dsm_object.transform     # an Affine transform for conversion to UTM-12 coordinates
utm_transform = np.array(dsm_transform).reshape((3,3))[:2]
utm_top_left = utm_transform @ np.array([0,0,1])
utm_bottom_right = utm_transform @ np.array([dsm_object.shape[0], dsm_object.shape[1], 1])
latlon_top_left = utm.to_latlon(utm_top_left[0], utm_top_left[1], 12, 'T')
latlon_bottom_right = utm.to_latlon(utm_bottom_right[0], utm_bottom_right[1], 12, 'T')

```
**Dataset Acknowledgement:** This DSM file is acquired by the State of Utah and its partners, and is in the public domain and can be freely distributed with proper credit to the State of Utah and its partners.  The State of Utah and its partners makes no warranty, expressed or implied, regarding its suitability for a particular use and shall not be liable under any circumstances for any direct, indirect, special, incidental, or consequential damages with respect to users of this product. 

**DSM DOI:** https://doi.org/10.5069/G9TH8JNQ
