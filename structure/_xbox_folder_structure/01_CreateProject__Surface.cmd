@echo off
set TARGETLANGUAGES=%~1
for %%D in ("%CD%") do set "PROJECTNAME=%%~nxD"
call TS2015 New-Project ^
  -Name "%PROJECTNAME%" ^
  -SourceLocation "00_source\_toLOC" ^
  -ProjectLocation "01_prep\01_trados" ^
  -LogLocation "01_prep\02_logs" ^
  -SourceLanguage "en-US" ^
  -TargetLanguages "ar-ae da-dk de-de es-es fi-fi fr-ca fr-fr it-it ja-jp nb-no nl-nl pt-pt sv-se zh-hk" ^
  -TMLocation "x:\Microsoft\HB1112921 Surface.com_FY18-Q3\_TM\Surface.com" ^
  -ProjectReference "x:\Microsoft\HB1112921 Surface.com_FY18-Q3\Projects\SurfaceCommercial\DfB\01_Jan\203404\01_prep\01_trados\203404.sdlproj" ^
  -Pretranslate -Analyze