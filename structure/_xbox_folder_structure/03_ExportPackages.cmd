@echo off
set TARGETLANGUAGES=%~1
call TS2015 Export-Package ^
  -ProjectLocation "01_prep\01_trados" ^
  -PackageLocation "02_totrans" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
  -ProjectTM "CreateNew" ^
  -RecomputeAnalysis

call 031_email.py