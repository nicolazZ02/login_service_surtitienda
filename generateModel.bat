@ECHO OFF
::Script del titulo que se reutilizara
ECHO ----------------------------------------
ECHO - Autor: Richard Ramires               -
ECHO - Fecha: 2023-01-02                    -
ECHO - Version 1.0.0                        -
ECHO ----------------------------------------
ECHO ****************************************
ECHO *   Generar modelo de base de datos    *
ECHO ****************************************

:: Obtener ruta actual
set ruta=%cd%
ECHO Ruta actual: %ruta%
::Activar entorno virtual de python en la ruta actual
call "%ruta%\venv\Scripts\activate.bat"
REM Ingresar datos de conexion a la base de datos
set /p user=Usuario:
set /p password=Password:
set /p host= Host:
set /p table= Table:
set /p database= Base de datos:
set /p port= Puerto:


sqlacodegen mysql://%user%:%password%@%host%/%database% --tables %table% --outfile %table%.py
venv\Scripts\activate.bat