@echo off
title Candidato PRO — Kit Político 2026
chcp 65001 > nul
cls
echo =======================================================
echo   🏛️ CANDIDATO PRO — KIT POLÍTICO ELEIÇÕES 2026
echo   Template Baseado no uPolitico
echo =======================================================
echo.
cd /d "%~dp0"

echo [1/2] Abrindo no navegador em http://localhost:3005...
start "" http://localhost:3005

echo [2/2] Iniciando servidor local na porta 3005...
echo Pressione Ctrl+C para encerrar.
echo.
python serve.py
pause
