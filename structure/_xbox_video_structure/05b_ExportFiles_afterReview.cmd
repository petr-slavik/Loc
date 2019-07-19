@echo off
set TARGETLANGUAGES=%~1


call TS2015 Export-TargetFiles ^
  -ProjectLocation "01_prep\01_trados" ^
  -ExportLocation "04_postprep\_afterReview" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
