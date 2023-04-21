ffmpeg -hide_banner -loglevel error -i "%~1" %~dp0..\temp\%~n1a1.png -y

::height
FOR /F "delims=" %%i IN ('ffprobe -v error -select_streams v:0 -show_entries stream^=height -of csv^=s^=x:p^=0 %~dp0..\temp\%~n1a1.png') DO set height=%%i

::width
FOR /F "delims=" %%i IN ('ffprobe -v error -select_streams v:0 -show_entries stream^=width -of csv^=s^=x:p^=0 %~dp0..\temp\%~n1a1.png') DO set width=%%i

::make gif
gifski --repeat -1 -W %width% -H %height% -Q 100 --extra -o "%~dp0..\temp\%~n1.gif" %~dp0..\temp\%~n1a1.png %~dp0..\temp\%~n1a1.png

::file deletion handled by python
::del %~dp0..\temp\* /F /Q