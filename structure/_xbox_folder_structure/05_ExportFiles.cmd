@echo off
set TARGETLANGUAGES=%~1

echo "files are copyied from _QA folder back to project folder"
robocopy 03_fromtrans\_QA 01_prep\01_trados *.sdlxliff /S 

call TS2015 Export-TargetFiles ^
  -ProjectLocation "01_prep\01_trados" ^
  -ExportLocation "04_postprep" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
