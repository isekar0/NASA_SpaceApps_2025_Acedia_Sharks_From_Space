# NASA_SpaceApps_2025_Acedia_Sharks_From_Space
Submission for NASA SpaceApps Challenge 2025
Team: Acedia


## Note:

Due to limited time, a lot of the code might not run correctly on other machines and environments as it was not tested for cross-platform performace.
Device specs:
OS            Arch Linux x86_64
Kernel        Linux 6.16.10-arch1-1
CPU           11th Gen Intel(R) Core(TM) i5-11400H 2.7 GHz
GPU 1         NVIDIA GeForce RTX 3050 Mobile [Discrete]
GPU 2         Intel UHD Graphics @ 1.4 GHz [Integrated]
Memory        31.08 GiB
Disk          1.69 TiB 

Additionally, the last parts of the code where the oceanographic features are being merged and then used to train a model do not work due to issues with correctly chunking and loading the data.

## Instructions

1) Install dependencies with '''pip install -r requirements.txt'''

   - We didn't actually use the xgboost library since we could not install it due to network issues.
   - Use '''pip install xgboost'''

   - It should be noted, there are a few libraries such as PyTorch which were installed but, due to time constraints, never used.
2) Run dataset_downloader.py

   - This will access PODAAC and download the needed files
3) Run obdaac_download.py using the http_manifest_xxx.txt

   - This will access AQUA MODIS, see instructions on the site for the prompt
4) Run bounding_box_and_merge_data.ipynb, detect_eddies.ipynb, process_shark_data.ipynb, clean_zarr_data.ipynb, merge_zarr_data.ipynb, machine_learning.ipynb, in order

## Citations and data-usage

See citations.txt for citations to datasets accessed and articles referenced 
