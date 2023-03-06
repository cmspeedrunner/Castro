@echo off
set iconPath= C:\Castro\resources\icon.ico
set key=HKCR\.cst
set value=CSTFile
set newDesc=Castro Source File

assoc .cst=cstfile


reg add %key% /v Content Type /t REG_SZ /d "%newDesc%" /f
reg add HKCR\%value% /v FriendlyTypeName /t REG_SZ /d "%newDesc%" /f
reg add HKCR\%value%\DefaultIcon /ve /d "%iconPath%" /f