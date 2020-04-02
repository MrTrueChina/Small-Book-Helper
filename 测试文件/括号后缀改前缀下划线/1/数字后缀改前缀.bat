@echo off

:: �ӳٻ���������չ
setlocal EnableDelayedExpansion


:: �˴���set�����ڼ�¼ʹ�õ���ȫ�ֱ�������ʵ�ʹ���û��Ӱ��

:: ��������չ�����ļ���
set fileName= 
:: �ļ�����ȷ���ǰ׺
set number= 
:: ��ȥ��׺����Ч�ļ���
set effectiveName= 
:: ��׺��
set extensionName= 
:: ���ļ���
set newName= 
:: ��������չ�����ļ�������
set fileNameLength=
:: ���ֺ�׺������������
set numberBracketIndex=
:: ���ֺ�׺�ķ���������
set numberReverseBracketIndex=
:: ���ֺ�׺������
set number=

:: GetStringLength �ķ���ֵ
set getStringLengthResult=
:: LastCharIndexOf �ķ���ֵ
set lastCharIndexOfResult=


::echo Start rename

:: ��ȡ����Ҫ�����������ļ���������������������ļ���
:: ����������
FOR %%G IN (*.bmp *.jpg *.png *.tif *.gif *.pcx *.tga *.exif *.fpx *.svg *.psd *.cdr *.pcd *.dxf *.ufo *.eps *.ai *.raw *.WMF *.webp) DO (
    call :RenameFile "%%G"
)
call :Exit

:: �����޸ĺ���ļ���
:: ������Ϊ �޸ĺ��ļ��� + ��չ��
:RenameFile
    :: %~1����ȡ��һ��������ȥ����β˫���ţ�û������Ӱ��
    call :GetNewName "%~1"
    ::echo Rename %~1
    xcopy "%fileName%%extensionName%" ".\rename\" /i
    ren ".\rename\%fileName%%extensionName%" "%newName%"
    ::echo ----------------
    goto :eof

:: �ָ��ݴ��ļ�������չ��
:: ���ļ������Ϊ��Ч�ļ����ͺ�׺
:: �Ѻ�׺��������������û�к�׺�Ĳ� 1 ��Ĭ��ֵ 1
:: �޸ĺ��ļ��� = ���_��Ч�ļ���  
:GetNewName
    ::echo Get new name by %~1
    :: ~n����չ�����ļ���
    set fileName=%~n1
    :: ~x����չ������չ��
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

:: �������ֺ�׺����ָ���ļ���ĩβ��������ס�����֣�ǰ������пո�ָ�Ҳ����û�пո�ָ�
:: ���һ���ַ��Ƿ�����
:: ��������
:: �м�������
:: �Ȼ�ȡ������������
:: ���������ж��ǲ��ǶԵ�
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
