echo off

echo ==小薄本助手==
echo (S) 创建子文件夹    (R) 数字后缀改前缀
set /p functionalTypes = 请选择使用功能
pause>nul

if functionalTypes equ s call :CreateSubFolders
if functionalTypes equ S call :CreateSubFolders

call :Exit


:CreateSubFolders
    echo 创建子文件夹
    goto :eof


:SuffixToPrefix
    echo 数字后缀改前缀
    goto :eof


:Exit
    pause>nul
    exit