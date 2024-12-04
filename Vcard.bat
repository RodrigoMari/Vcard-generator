@echo off
setlocal

REM Verificar si Python está instalado
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python no encontrado en el sistema, descargando e instalando Python. Puede tardar unos minutos...

    REM Descargar Python (en este caso, la versión 3.11.0)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe -OutFile python_installer.exe"

    REM Verificar si el archivo se descargó correctamente
    if exist python_installer.exe (
        REM Ejecutar el instalador de Python
        start /wait python_installer.exe /quiet InstallAllUsers=0 InstallLauncherAllUsers=0 PrependPath=1

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

REM Crear entorno virtual
echo Creando entorno virtual...
python -m venv EV

REM Activar entorno virtual
echo Activando entorno virtual...
call EV\Scripts\activate

REM Actualizar pip a la última versión
echo Actualizando pip...
python -m pip install --upgrade pip

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt

REM Ejecutar el script
echo Ejecutando el script...
python Vcard_contact.py

REM Agregar una pausa para evitar que la ventana se cierre inmediatamente
echo El script ha finalizado. Presione cualquier tecla para cerrar...
pause

REM Desactivar entorno virtual
echo Desactivando entorno virtual...
deactivate

echo Proceso completado. El proyecto ha sido ejecutado correctamente.
pause

endlocal