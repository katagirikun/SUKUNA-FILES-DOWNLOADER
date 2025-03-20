#!/usr/bin/env python3

import os
import sys
import requests
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

# 🎯 File Save Location
save_path = "/storage/emulated/0/Download/CROZNXSKINS/game_patch_3.7.0.19735.pak"
url = "https://download1530.mediafire.com/f3zmsm4na8og7wXK6jASCsN-bRjN_myZK8J4mm4rW0QM9gpOvkJHh2NE28BckfYl9xiHDkFaCQq2GOmj3m9O60_B5qiihwL8mt42tKyll3te9KUAfnza9ta2Ra0sSVxVmG5cAWr7X433Za1d1X25Zc82gv_-AIn6Y81Pm8fHgGs/7dkwm3yjqx0q1q9/game_patch_3.7.0.19735.pak"

# 📦 Download Function
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    
    with open(save_path, "wb") as file, Progress(
        "[cyan]🚀 Downloading...", 
        BarColumn(), 
        DownloadColumn(), 
        TransferSpeedColumn(), 
        TimeRemainingColumn()
    ) as progress:
        
        task = progress.add_task("Download", total=total_size)
        
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                progress.update(task, advance=len(chunk))

    print("\n✅ Download Complete! File saved at:", save_path)

# 🚀 Start Download
download_file(url, save_path)
