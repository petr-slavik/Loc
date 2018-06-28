@echo off
set TARGETLANGUAGES=%~1
for %%D in ("%CD%") do set "PROJECTNAME=%%~nxD"

::call 010_unzip_archive.py
::cd 00_source\_flat

call TS2015 New-Project ^
  -Name "%PROJECTNAME%" ^
  -SourceLocation "00_source\_flat" ^
  -ProjectLocation "01_prep\01_trados" ^
  -LogLocation "01_prep\02_logs" ^
  -SourceLanguage "en-US" ^
  -TargetLanguages "zh-cn" ^
  -TMLocation "x:\Microsoft\_ASG Digital_account management\TMs" ^
  -ProjectReference "x:\Microsoft\HB1112534_Digital Other Q4 2017\Xbox_Engineering\_trans\20180307_xbox_13708_zh-cn\01_prep\01_trados\20180307_xbox_13708_zh-cn.sdlproj" ^

call 013_segment_action.py

echo ">>>>CHECK PROJECT FILES IN TRADOS STUDIO<<<<<<"
echo "Next manuall steps in Trados are Translation count, pre-translate, update TMs and Analyze"
echo "Run 02_create_analysis_xbox.py for creating analysis sheet"
echo "Then run 03_ExportPackages.cmd script and send HO mail to PMs"
"c:\Program Files (x86)\SDL\SDL Trados Studio\Studio4\SDLTradosStudio.exe" /openProject "%CD%\01_prep\01_trados\%PROJECTNAME%.sdlproj"
