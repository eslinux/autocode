

::You can create a new environment variable, or edit the value of an existing environment variable (but not its name) from the Command Prompt too. 
::The command you have to enter is:
::	setx variable_name “value” if you want to create a user environment variable
::	setx variable_name “value” /m if you’re going to create a system environment variable
::For example, we typed setx TEST “C:\digitalcitizen” and created a user variable named TEST with the value C:\digitalcitizen.


::How to delete an environment variable from Command Prompt
::To delete an environment variable from Command Prompt, type one of these two commands, depending on what type that variable is:
::REG delete “HKCU\Environment” /F /V “variable_name” if it’s a user environment variable, or
::REG delete “HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment” /F /V “variable_name” if it’s a system environment variable.
::For example, we typed REG delete “HKCU\Environment” /F /V “TEST” and our TEST environment variable was gone from the user’s profile.


::set environment variable permanently
::run in administrator
setx github_path "C:\Users\user\Documents\GitHub"

::check this command by open other command prompt and run command below
::or open Registry editor and browse to HKEY_CURRENT_USER\Environment to see
echo %github_path%

::delete
delete “HKCU\Environment” /F /V “github_path”