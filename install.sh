#!/bin/bash

# Install Python & Rich Module
apt update && apt install python -y 2>/dev/null || pkg install python -y 2>/dev/null
pip install rich requests

# Clone Repo & Move Script
git clone https://github.com/YOUR_GITHUB_USERNAME/SUKUNAV1-Installer.git $HOME/SUKUNAV1
cp $HOME/SUKUNAV1/SUKUNAV1.py /usr/local/bin/SUKUNAV1
chmod +x /usr/local/bin/SUKUNAV1

# Clean Up
rm -rf $HOME/SUKUNAV1

echo "✅ Installation Complete! Type 'SUKUNAV1' to start downloading."
