@echo off
set /p cmm="Inserisci commit: "
git add .
git commit -m "%cmm%"
git push