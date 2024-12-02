@echo off
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
