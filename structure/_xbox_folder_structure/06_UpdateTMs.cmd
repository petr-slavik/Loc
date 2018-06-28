@echo off
set TARGETLANGUAGES=%~1
call TS2015 Update-MainTMs ^
  -ProjectLocation "01_prep\01_trados" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
