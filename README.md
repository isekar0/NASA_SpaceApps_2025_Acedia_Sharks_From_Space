# NASA_SpaceApps_2025_Acedia_Sharks_From_Space
Submission for NASA SpaceApps Challenge 2025
Team: Acedia


## Note:

Due to limited time, a lot of the code might not run correctly on other machines and environments. Additionally, the last parts of the code where the oceanographic features are being merged and then used to train a model do not work.

## Instructions

1) Install dependencies with '''pip install -r requirements.txt'''

   - It should be noted, there are a few libraries such as PyTorch which were installed but, due to time constraints, never used.
2) Run dataset_downloader.py

   - This will access PODAAC and download the needed files
3) Run obdaac_download.py using the http_manifest_xxx.txt

   - This will access AQUA MODIS, see instructions on the site for the prompt
4) Run bounding_box_and_merge_data.ipynb, detect_eddies.ipynb, process_shark_data.ipynb, clean_zarr_data.ipynb, merge_zarr_data.ipynb, machine_learning.ipynb, in order

## Citations and datausage

The link to the datasets in the website submission does not lead anywhere, see citations.txt for citations to the datasets used and the articles referenced
