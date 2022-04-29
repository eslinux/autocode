
::if you want to create a user environment variable
setx github_path "C:\Users\user\Documents\GitHub"
echo %github_path%


::if you’re going to create a system environment variable
setx /m github_path "C:\Users\user\Documents\GitHub"
echo %github_path%