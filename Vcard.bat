@echo off
setlocal

REM Verificar si Python está instalado
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python no encontrado en el sistema, descargando e instalando Python...

    REM Descargar Python (en este caso, la versión 3.12.0)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe -OutFile python_installer.exe"

    REM Verificar si el archivo se descargó correctamente
    if exist python_installer.exe (
        REM Ejecutar el instalador de Python
        start /wait python_installer.exe /quiet InstallAllUsers=0 PrependPath=1

        REM Eliminar el instalador descargado
        del python_installer.exe
    ) else (
        echo Error: No se pudo descargar el instalador de Python.
        exit /b 1
    )
)


REM Verificar si pip está instalado
python -m ensurepip --upgrade
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip no encontrado, instalando pip...
    python -m ensurepip --upgrade
)

echo Creando entorno virtual...
python -m venv EV

echo Activando entorno virtual...
call EV\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt

echo Ejecutando el script...
python Vcard-contact.py

echo Desactivando entorno virtual...
deactivate

echo Proceso completado. El proyecto ha sido ejecutado correctamente.
pause

endlocal
