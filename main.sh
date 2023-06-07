cp .bashrc ~/.bashrc

clear

python3 claude.py > /dev/null 2>&1 & 
python3 run.py
killall python3
rm -rf __pycache__
