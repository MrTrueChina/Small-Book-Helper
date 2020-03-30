@echo off

::@echo off：关闭过程显示，默认显示每个操作，实际使用的时候看了也没用，要改的时候自然会再打开
echo  

set /p subFoldersNumber=输入需要创建的子文件夹的最大下标（从0开始但不能为0）

::set：赋值， /p：外部输入
:: set /p 变量名 = 提示语


:DetectionParameters
    set /a subFoldersNumber = %subFoldersNumber%/1
    set /a subFoldersNumber = %subFoldersNumber%-1
    if %subFoldersNumber% LSS 0 goto ParameterError
    set /a subFoldersNumber = %subFoldersNumber%+1
    goto CreatSubFolders

    ::set /a：支持数学计算的赋值，%变量名%大概是加了两个百分号就视为变量名，不加视为字符串
    :: set /a 变量名 = 运算
    :: / 是整除的，可以用来取整，但如果参数是小数则会出现错误提示，应该是用法有问题

    ::LSS：批处理里大于号小于号都被用来做重定向符号了，所以小于要用 LSS

    ::正则不会，如果运算时候的参数不是纯数字似乎就会视为0，就这么用为0的状况作为错误来处理了


:CreatSubFolders
    for /f "delims=" %%i in ("%cd%") do set currentFolder=%%~ni
    echo 获取当前文件夹名称：%currentFolder%

    set /a subFoldersNumber = %subFoldersNumber% + 1
    echo 开始创建子文件夹，共计%subFoldersNumber%个

    set /a currentIndex = 0
    :CreatSubFolderForStart
        echo 创建下标为%currentIndex%的子文件夹：%currentFolder% %currentIndex%
        set subFolder = %currentFolder% %currentIndex%
        md "%currentFolder% %currentIndex%
        set /a currentIndex = %currentIndex%+1

        if %currentIndex% LSS %subFoldersNumber% goto CreatSubFolderForStart

    echo 创建完成，按任意键退出
    goto Exit

::原理是通过goto和标志量（currentIndex）实现循环效果
::md：创建文件夹，不输入绝对路径就按照相对路径，有空格的文件夹名要用双引号括起来



:ParameterError
    echo 参数错误，按任意键退出
    goto Exit


:Exit
    pause>nul
    exit
