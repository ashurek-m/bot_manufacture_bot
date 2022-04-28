@echo off


call %~dp0venv\Scripts\activate

cd %~dp0

set TOKEN=1663374359:AAG04PvFvcjDGqRe8Jynv6yO50ofM4SrvQ0


python bot_telegram.py

pause
