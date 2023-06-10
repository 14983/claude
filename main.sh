diff .bashrc ~/.bashrc
ret=$?

if [ ${ret} -eq 0 ]; then
    echo 'doing nothing'
else
    cp ~/.bashrc ~/.bashrc.old
    cp .bashrc ~/.bashrc
fi

clear

python3 main.py
killall python3
rm -rf __pycache__
