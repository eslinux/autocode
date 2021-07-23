
'============================================= Progress bar ===============================================================
Class ProgressBar
    Private m_PercentComplete
    Private m_CurrentStep
    Private m_ProgressBar
    Private m_Title
    Private m_Text
    Private m_Top
    Private m_Left

    'Initialize defaults
    Private Sub Class_Initialize()
        m_PercentComplete = 1
        m_CurrentStep = 0
        m_Title = "Progress"
        m_Text = ""
        m_Top = 100
        m_Left = 150
    End Sub

    Public Function SetTitle(pTitle)
        m_Title = pTitle
        if IsObject(m_ProgressBar) then
            m_ProgressBar.Document.title = m_PercentComplete & "% Complete : " & m_Title
            m_ProgressBar.Document.GetElementById("pc").InnerHtml = m_PercentComplete & "% Complete : " & m_Title
        end if
    End Function

    Public Function SetText(pText)
        m_Text = pText
        if IsObject(m_ProgressBar) then m_ProgressBar.Document.GetElementById("text").InnerHtml = m_Text
    End Function

    Public Function SetTop(pTop)
        m_Top = pTop
    End Function

    Public Function SetLeft(pLeft)
        m_Left = pLeft
    End Function

    Public Function GetTop()
        GetTop = m_ProgressBar.top
    End Function

    Public Function GetLeft()
        GetLeft = m_ProgressBar.left
    End Function

    Public Function Update(percentComplete)
        If percentComplete > 100 Then
            m_PercentComplete = 100
        elseif percentComplete < 1 then
            m_PercentComplete = 1
        else
            m_PercentComplete = percentComplete 
        end if
        UpdateProgressBar()
    End Function

    Public Function Show()
        Set m_ProgressBar = CreateObject("InternetExplorer.Application")
        'in code, the colon acts as a line feed
        m_ProgressBar.navigate2 "about:blank" : m_ProgressBar.width = 800 : m_ProgressBar.height = 380 : m_ProgressBar.toolbar = false : m_ProgressBar.menubar = false : m_ProgressBar.statusbar = false : m_ProgressBar.visible = True : m_ProgressBar.Resizable = False : m_ProgressBar.top = m_Top : m_ProgressBar.left = m_Left
        m_ProgressBar.document.write "<body Scroll=no style='margin:100px;'><div style='text-align:center;padding:15px;'><span name='pc' id='pc'>0% Complete</span></div>"
        m_ProgressBar.document.write "<div id='statusbar' name='statusbar' style='border:1px solid blue;line-height:22px;height:30px;color:blue;'>" _
            & "<table width='100%' height='100%'><tr><td id='progress' style='width:1%' bgcolor='#0000FF'></td><td></td></tr></table></div>"
        m_ProgressBar.document.write "<div style='text-align:center;padding:15px;'><span id='text' name='text'></span></div>"
    End Function

    Public Function Close()
        m_ProgressBar.quit
    End Function

    Private Function UpdateProgressBar()
        if m_CurrentStep <> m_PercentComplete then
            If m_PercentComplete = 100 Then
                m_ProgressBar.Document.GetElementById("statusbar").InnerHtml = "<table width='100%' height='100%'><tr><td bgcolor='#0000FF'></td></tr></table>"
            else
                m_ProgressBar.Document.GetElementById("progress").style.width = m_PercentComplete & "%"
            end if
            m_ProgressBar.Document.title = m_PercentComplete & "% Complete : " & m_Title
            m_ProgressBar.Document.GetElementById("pc").InnerHtml = m_PercentComplete & "% Complete : " & m_Title
            m_ProgressBar.Document.GetElementById("text").InnerHtml = m_Text
            m_CurrentStep = m_PercentComplete
        end if 
    End Function
End Class

sub test_ProgressBar()
	'Declare progressbar and percentage complete
	Dim pb
	Dim percentComplete
	'Setup the initial progress bar
	Set pb = New ProgressBar
	percentComplete = 0
	pb.SetTitle("Step 1 of 5")
	pb.SetText("Copying bin/Debug Folder")
	pb.SetTop(150) ' These are optional
	pb.SetLeft(300) ' These are optional
	pb.Show()

	'Loop to update the percent complete of the progress bar
	'Just add the pb.Update in your code to update the bar
	'Text can be updated as well by pb.SetText
	Do While percentComplete <= 100
		wscript.sleep 500
		pb.Update(percentComplete)
		percentComplete = percentComplete + 10
	Loop
	wscript.sleep 2000
	pb.Close()

	'This shows how you can use the code for multiple steps
	Set pb = New ProgressBar
	percentComplete = 0
	pb.SetTitle("Step 2 of 5")
	pb.SetText("Copying bin/Release Folder")
	pb.Show()
	pb.Update(percentComplete)
	Do While percentComplete <= 100
		wscript.sleep 500
		pb.Update(percentComplete)
		percentComplete = percentComplete + 10
	Loop
	msgbox "Completed", vbSystemModal
	pb.Close()
	wscript.quit

end sub








'================================================== Progress simple text ==========================================================
Class ProgressWaiting
    Private m_ProgressBar
	
    Private m_Top
    Private m_Left
	Private m_Width
    Private m_Height

    'Initialize defaults
    Private Sub Class_Initialize()
        m_Top = 100
        m_Left = 150
		m_Width = 400
		m_Height = 200
    End Sub

    Public Function SetTitle(pTitle)
        if IsObject(m_ProgressBar) then
            m_ProgressBar.Document.title = pTitle
        end if
    End Function

    Public Function SetText(pText)
        if IsObject(m_ProgressBar) then 
			m_ProgressBar.Document.GetElementById("text").InnerHtml = pText
		end if
    End Function

    Public Function SetWindow(pTop, pLeft, pWidth, pHeight)
		m_Top = pTop
        m_Left = pLeft
		m_Width = pWidth
		m_Height = pHeight
    End Function

    Public Function Show()
        Set m_ProgressBar = CreateObject("InternetExplorer.Application")
        m_ProgressBar.navigate2 "about:blank" : m_ProgressBar.width = m_Width : m_ProgressBar.height = m_Height : m_ProgressBar.toolbar = false : m_ProgressBar.menubar = false : m_ProgressBar.statusbar = false : m_ProgressBar.visible = True : m_ProgressBar.Resizable = False : m_ProgressBar.top = m_Top : m_ProgressBar.left = m_Left
        m_ProgressBar.Document.title = ""
		
		'Message to user
		m_ProgressBar.document.write "<div style='text-align:center;padding:15px;'><span id='text' name='text'></span></div>"
    End Function

    Public Function Close()
        m_ProgressBar.quit
    End Function
End Class


sub test_ProgressWaiting()
	Dim pb
	Set pb = New ProgressWaiting

	pb.Show()
	pb.SetTitle("Progress")
	pb.SetText("Copying... please wait...")
	
	percentComplete = 0
	Do While percentComplete <= 100
		wscript.sleep 500
		pb.SetText("Copying...  " & percentComplete)
		percentComplete = percentComplete + 10
	Loop
	
	pb.Close()
	MsgBox "Copy finished"
	
end sub 



call test_ProgressWaiting()



