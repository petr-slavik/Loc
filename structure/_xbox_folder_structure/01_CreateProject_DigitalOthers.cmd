@echo off
set TARGETLANGUAGES=%~1
for %%D in ("%CD%") do set "PROJECTNAME=%%~nxD"
call TS2015 New-Project ^
  -Name "%PROJECTNAME%" ^
  -SourceLocation "00_source\_toLOC" ^
  -ProjectLocation "01_prep\01_trados" ^
  -SourceLanguage "en-US" ^
  -TargetLanguages "ar-AE de-DE en-GB es-ES es-MX fi-FI fr-CA fr-FR it-IT ja-JP ko-KR nb-NO nl-NL pl-PL pt-BR pt-PT ru-RU sv-SE zh-CN zh-TW he-IL tr-TR" ^
  -TMLocation "x:\Microsoft\_ASG Digital_account management\TMs" ^
  -ProjectReference "x:\Microsoft\HB1113293_Digital Other Q2 FY2018\Projects\04_April\XXX_Xbox Videos April\04_PUBG GIF\01_prep\01_trados\04_PUBG GIF.sdlproj" ^
  -Pretranslate ^
  -Analyze
