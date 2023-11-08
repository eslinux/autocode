Set SourceDir="C:\Users\luong\Downloads\myfoler"

#folder chua file script nay
#Set TargetDir="%~dp0" 


#folder hien tai tren terminal
Set TargetDir="%cd%" 
xcopy %SourceDir% %TargetDir% /i /d /y /e
