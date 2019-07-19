@echo off
set TARGETLANGUAGES=%~1
call TS2015 Export-Package ^
  -Task "Review" ^
  -ProjectLocation "01_prep\01_trados" ^
  -PackageLocation "05_toReview" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
  -ProjectTM "CreateNew" ^
  -RecomputeAnalysis

call 031_email.py