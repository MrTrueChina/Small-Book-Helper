:: �ر�ָ����ʾ
@echo off

set /p subFoldersNumber=������Ҫ���������ļ��е�����±꣨��0��ʼ������Ϊ0��

:: set����ֵ�� /p���ⲿ����
:: set /p ������ = ��ʾ��


:DetectionParameters
    set /a subFoldersNumber = %subFoldersNumber%/1
    set /a subFoldersNumber = %subFoldersNumber%-1
    if %subFoldersNumber% LSS 0 goto ParameterError
    set /a subFoldersNumber = %subFoldersNumber%+1
    goto CreatSubFolders

    :: set /a��֧����ѧ����ĸ�ֵ��%������%����Ǽ��������ٷֺž���Ϊ��������������Ϊ�ַ���
    :: set /a ������ = ����
    :: / �������ģ���������ȡ���������������С�������ִ�����ʾ��Ӧ�����÷�������

    :: LSS������������ں�С�ںŶ����������ض�������ˣ�����С��Ҫ�� LSS

    :: ���򲻻ᣬ�������ʱ��Ĳ������Ǵ������ƺ��ͻ���Ϊ0������ô��Ϊ0��״����Ϊ������������


:CreatSubFolders
    for /f "delims=" %%i in ("%cd%") do set currentFolder=%%~nxi
    :: ~nx���������ļ������׺��
    echo ��ȡ��ǰ�ļ������ƣ�%currentFolder%

    set /a subFoldersNumber = %subFoldersNumber% + 1
    echo ��ʼ�������ļ��У�����%subFoldersNumber%��

    set /a currentIndex = 0
    :CreatSubFolderForStart
        echo �����±�Ϊ%currentIndex%�����ļ��У�%currentFolder% %currentIndex%
        set subFolder = %currentFolder% %currentIndex%
        md "%currentFolder% %currentIndex%"
        set /a currentIndex = %currentIndex%+1

        if %currentIndex% LSS %subFoldersNumber% goto CreatSubFolderForStart

    echo ������ɣ���������˳�
    goto Exit

:: ԭ����ͨ��goto�ͱ�־����currentIndex��ʵ��ѭ��Ч��
:: md�������ļ��У����������·���Ͱ������·�����пո���ļ�����Ҫ��˫����������



:ParameterError
    echo �������󣬰�������˳�
    goto Exit


:Exit
    pause>nul
    exit
