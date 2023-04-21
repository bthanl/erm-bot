@echo off

::width
FOR /F "delims=" %%i IN ('ffprobe -v error -select_streams v:0 -show_entries stream^=width -of default^=nk^=1:nw^=1 %~1') DO set /a width=%%i

::height
FOR /F "delims=" %%i IN ('ffprobe -v error -select_streams v:0 -show_entries stream^=height -of default^=nk^=1:nw^=1 %~1') DO set /a height=%%i

set /a fps = 30

ffmpeg -hide_banner -loglevel warning -i "%1" -ignore_loop 1 -i %~dp0lmao.gif -filter_complex "[1][0]scale2ref=w=in_w:h=in_h[v1][v0];[v1]split[o1][o2];[v0][o1]overlay=0:0, palettegen[p];[0][o2]overlay=0:0 [out];[out][p]paletteuse[final];[final]fps=fps=%fps%" %~dp0..\temp\final.gif -y

gifski -r %fps% -W %width% -H %height% -o "%~dp0..\temp\%~n1_new.gif" %~dp0..\temp\final.gif

::file deletion handled by python
::del %~dp0..\temp\* /F /Q