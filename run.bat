@echo off
title PhoneScan-Kato
cd ./src/
python index.py
set /p id=Presiona la tecla Enter para finalizar el programa...
echo %id%