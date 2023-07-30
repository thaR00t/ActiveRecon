#/bin/bash


sudo tr -d '\r' <ar-tool.py> ar-tool-linux.py

sudo chmod +x ar-tool-linux.py
sudo mv ar-tool-linux.py ar-tool
sudo mv ar-tool /usr/bin/

echo "Installation Done..."

clear

ar-tool --help
