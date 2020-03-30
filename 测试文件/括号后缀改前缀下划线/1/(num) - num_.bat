@echo off

echo Start rename


:: 不包括后缀的文件名
set fileName = 
:: 文件的正确序号前缀
set number = 
:: 除去后缀的有效文件名
set effectiveName = 
:: 后缀名
set extensionName = 
:: 新文件名
set newName = 

:: 获取到需要改名的所有文件名（除了批处理的所有文件）
:: 依次重命名
FOR %%G IN (*.bmp *.jpg *.png *.tif *.gif *.pcx *.tga *.exif *.fpx *.svg *.psd *.cdr *.pcd *.dxf *.ufo *.eps *.ai *.raw *.WMF *.webp) DO (
    call :RenameFile "%%G"
)
call :Exit

:: 计算修改后的文件名
:: 重命名为 修改后文件名 + 扩展名
:RenameFile
    echo Rename %1
    call :GetNewName "%1"
    goto :eof

:: 分割暂存文件名和扩展名
:: 将文件名拆分为有效文件名和后缀
:: 把后缀里的序号挑出来，没有后缀的补 1 或默认值 1
:: 修改后文件名 = 序号_有效文件名  
:GetNewName
    :: ~n：扩展到仅文件名
    set fileName = %~n1
    :: ~x：扩展到仅扩展名
    set extensionName = %~x1
    call :GetNumber "fileName"
    call :GetEffectiveName "fileName"
    set newName = %number%_%effectiveName%%extensionName%
    echo Newname = %newName%
    goto :eof

:GetNumber
    goto :eof

:GetEffectiveName
    goto :eof

:LogHello
    echo hello
    goto :eof
    

echo End rename
call :Exit


:Exit
    pause>nul
    exit

