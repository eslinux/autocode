
1. [subst] command
	::Create virtual drive
	subst <drive:> \path\to\folder

	Ex:
	subst E: C:\Users\user\workspace


	::Remove Virtual Drive Created with Subst
	subst <drive:> /D

	Ex:
	subst N: /D
	
2. [Net use] command
★https://lazyadmin.nl/it/net-use-command/

	::Create virtual drive
	Net use N: \\172.20.10.4\myshare /persistent:yes

	# Authenticate with the username and password
	Net use N: \\VBoxSvr\Win11\Documents /user:username password /p:yes
	
	::Remove Virtual Drive Created
	Net use N: /delete
	