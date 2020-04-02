@echo off

:: 延迟环境变量扩展
setlocal EnableDelayedExpansion


:: 此处的set仅用于记录使用到的全局变量，对实际功能没有影响

:: 不包括扩展名的文件名
set fileName= 
:: 文件的正确序号前缀
set number= 
:: 除去后缀的有效文件名
set effectiveName= 
:: 后缀名
set extensionName= 
:: 新文件名
set newName= 
:: 不包括扩展名的文件名长度
set fileNameLength=
:: 数字后缀的正括号索引
set numberBracketIndex=
:: 数字后缀的反括号索引
set numberReverseBracketIndex=
:: 数字后缀的数字
set number=

:: GetStringLength 的返回值
set getStringLengthResult=
:: LastCharIndexOf 的返回值
set lastCharIndexOfResult=


::echo Start rename

:: 获取到需要改名的所有文件名（除了批处理的所有文件）
:: 依次重命名
FOR %%G IN (*.bmp *.jpg *.png *.tif *.gif *.pcx *.tga *.exif *.fpx *.svg *.psd *.cdr *.pcd *.dxf *.ufo *.eps *.ai *.raw *.WMF *.webp) DO (
    call :RenameFile "%%G"
)
call :Exit

:: 计算修改后的文件名
:: 重命名为 修改后文件名 + 扩展名
:RenameFile
    :: %~1：获取第一个参数并去除首尾双引号，没有则无影响
    call :GetNewName "%~1"
    ::echo Rename %~1
    xcopy "%fileName%%extensionName%" ".\rename\" /i
    ren ".\rename\%fileName%%extensionName%" "%newName%"
    ::echo ----------------
    goto :eof

:: 分割暂存文件名和扩展名
:: 将文件名拆分为有效文件名和后缀
:: 把后缀里的序号挑出来，没有后缀的补 1 或默认值 1
:: 修改后文件名 = 序号_有效文件名  
:GetNewName
    ::echo Get new name by %~1
    :: ~n：扩展到仅文件名
    set fileName=%~n1
    :: ~x：扩展到仅扩展名
    set extensionName=%~x1

    call :GetNumberBracketIndex "%fileName%"
    
    call :GetNumber "%fileName%"
    call :GetEffectiveName "%fileName%"
    set newName=%number%_%effectiveName%%extensionName%
    ::echo Newname = %newName%
    goto :eof

:GetNumberBracketIndex
    call :LastCharIndexOf "%~1" "("
    set numberBracketIndex=%lastCharIndexOfResult%
    call :LastCharIndexOf "%~1" ")"
    set numberReverseBracketIndex=%lastCharIndexOfResult%

    ::echo Index of number is [%numberBracketIndex%-%numberReverseBracketIndex%]
    goto :eof

:: 括号数字后缀，是指在文件名末尾有括号括住的数字，前面可能有空格分隔也可能没有空格分隔
:: 最后一个字符是反括号
:: 有正括号
:: 中间是数字
:: 先获取正反括号索引
:: 根据索引判断是不是对的
:GetNumber
    set getNumberFileName=%~1
    set /a getNumberStartIndex=%numberBracketIndex%+1
    set /a getNumberNumberLength=%numberReverseBracketIndex%-%getNumberStartIndex%
    set getNumberNumber=!getNumberFileName:~%getNumberStartIndex%,%getNumberNumberLength%!

    ::echo number = %getNumberNumber%
    set number=%getNumberNumber%
    if not defined number set number=1
    goto :eof

:GetEffectiveName
    set getEffectiveNameFileName=%~1
    set /a getEffectiveNameEndIndex=%numberBracketIndex%
    set getEffectiveNameEffectiveName=!getEffectiveNameFileName:~0,%getEffectiveNameEndIndex%!

    if not defined getEffectiveNameEffectiveName set getEffectiveNameEffectiveName=%fileName%
    ::echo Effective name = %getEffectiveNameEffectiveName%
    set effectiveName=%getEffectiveNameEffectiveName%
    goto :eof

:LastCharIndexOf
    set lastCharIndexOfString=%~1
    set lastCharIndexOfChar=%~2

    call :GetStringLength "%~1"
    set /a lastCharIndexOfCurentIndex=%getStringLengthResult%-1

    :LastCharIndexOfForStart
        set lastCharIndexOfCurrentChar=!lastCharIndexOfString:~%lastCharIndexOfCurentIndex%,1!
        if %lastCharIndexOfCurrentChar% equ %lastCharIndexOfChar% goto :LastCharIndexOfForEnd
        set /a lastCharIndexOfCurentIndex-=1
        if %lastCharIndexOfCurentIndex% equ -1 goto :LastCharIndexOfForEnd
        goto :LastCharIndexOfForStart
        :LastCharIndexOfForEnd

    set lastCharIndexOfResult=%lastCharIndexOfCurentIndex%
    goto :eof

:GetStringLength
    set getStringLengthResult=0
    set getStringLengthString=%~1
::    ::echo getStringLengthString = %getStringLengthString%
    :GetStringLengthForStart
        set getStringLengthCurrentChar=!getStringLengthString:~%getStringLengthResult%,1!
        set /a getStringLengthResult+=1
        if defined getStringLengthCurrentChar goto :GetStringLengthForStart
    set /a getStringLengthResult-=1
::    ::echo length = %getStringLengthResult%
    goto :eof

:Exit
    pause>nul
    exit
