@echo off
set TARGETLANGUAGES=%~1
for %%D in ("%CD%") do set "PROJECTNAME=%%~nxD"
call TS2015 New-Project ^
  -Name "%PROJECTNAME%" ^
  -SourceLocation "00_source\_toLOC" ^
  -ProjectLocation "01_prep\01_trados" ^
  -SourceLanguage "en-US" ^
  -TargetLanguages "en-gb es-mx fr-fr fr-CA de-de pt-br zh-tw zh-cn it-it ja-jp ko-kr sv-se es-es nb-no ru-ru nl-nl pl-pl fi-fi pt-pt ar-ae tr-tr he-il" ^
  -TMLocation "x:\Microsoft\_ASG Digital_account management\TMs" ^
  -ProjectReference "x:\Microsoft\HB1114835_Digital Other April May FY2019\Projects\05_May\XX_Xbox Video May\24_E3_Olympus_SyncSheet\01_prep\01_trados\24_E3_Olympus_SyncSheet.sdlproj"


REM  -Pretranslate ^
REM  -Analyze


REM OST SHEET

call 014_WOL_MT_fix.py

echo
"c:\Program Files (x86)\SDL\SDL Trados Studio\Studio4\SDLTradosStudio.exe" /openProject "%CD%\01_prep\01_trados\%PROJECTNAME%.sdlproj"