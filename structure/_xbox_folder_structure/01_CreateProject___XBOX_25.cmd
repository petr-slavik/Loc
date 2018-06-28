@echo off
set TARGETLANGUAGES=%~1
for %%D in ("%CD%") do set "PROJECTNAME=%%~nxD"

call 010_unzip_archive.py
cd 00_source\_flat
call rename_files_left___.py
cd ..
cd ..
call 011_move_renamed_files.py

call TS2015 New-Project ^
  -Name "%PROJECTNAME%" ^
  -SourceLocation "00_source\_flat" ^
  -ProjectLocation "01_prep\01_trados" ^
  -LogLocation "01_prep\02_logs" ^
  -SourceLanguage "en-US" ^
  -TargetLanguages "%TARGETLANGUAGES%" ^
  -TMLocation "x:\Microsoft\_ASG Digital_account management\TMs" ^
  -ProjectReference "x:\Microsoft\HB1113293_Digital Other Q2 FY2018\Xbox_Engineering\_trans\20180201_xbox_13194_update\01_prep\01_trados\20180201_xbox_13194_update.sdlproj" ^
  
call 012_delete_extra_files_from_trados_project.py
call 013_segment_action.py

echo ">>>>CHECK PROJECT FILES IN TRADOS STUDIO<<<<<<"
echo "Next manuall steps in Trados are Translation count, pre-translate, update TMs and Analyze"
echo "Run 02_create_analysis_xbox.py for creating analysis sheet"
echo "Then run 03_ExportPackages.cmd script and send HO mail to PMs"
"c:\Program Files (x86)\SDL\SDL Trados Studio\Studio4\SDLTradosStudio.exe" /openProject "%CD%\01_prep\01_trados\%PROJECTNAME%.sdlproj"