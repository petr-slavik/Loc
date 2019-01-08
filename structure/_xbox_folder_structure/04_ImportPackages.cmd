@echo off
call TS2015 Import-Package ^
  -ProjectLocation "01_prep\01_trados" ^
  -PackageLocation "03_fromtrans" ^
  
robocopy 01_prep\01_trados\ 03_fromtrans\_QA /S /XF *.sdlproj *.backup /XD en-US Packages Reports

call 041_redundant_characters_checker.py