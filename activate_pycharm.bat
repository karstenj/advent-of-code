@echo off
call C:\TOOLS\miniconda3\Scripts\activate.bat
call conda activate aoc
set PATH=C:\TOOLS\miniconda3;C:\TOOLS\miniconda3\Scripts\C:\TOOLS\miniconda3\Library\bin;%PATH%
call "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\bin\pycharm64.exe"