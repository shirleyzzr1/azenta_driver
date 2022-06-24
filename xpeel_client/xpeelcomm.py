# Option Explicit

# Dim strRsp As String
# Public bVersionTag As Boolean
# Dim iError As Integer

# Public bErrorFlag As Boolean
# Public strError As String

# Public bStatusWindowShown As Boolean

# Dim iMessage As Integer

# 'Writing commands.

# 'List:
# ' Status Command: *stat<CR><LF>     Response: *cv:XD1:Xd2:X<CR><LF> -> see pg2 comm manual XPeel
# ' Version: *version<CR><LF>         Response: *1.0<CR><LF>
# ' Reset: *reset<CR><LF>             Response: *ack<CR><LF>
# ' Calibrate: *cal:YZ<CR><LF>        Response: *ack<><> -> *done<CR><LF>
# '

# 'Ready response for the XPeel: *ready:XX,XX,XX<CR><LF>
# 'The XX fields can be any error code, in any order.


# 'Bunch of Generic commands here, handled by XPeelCmd.
# 'Also allow for error checking and handling here.

# Public Function ErrorCheck(ByVal bError As Boolean, ByVal strCmd As String) As Boolean
    If bError = False Then
    ErrorCheck = False
    Exit Function
    End If
    
    If bError = True Then
    
          Select Case MsgBox("The following error has occurred: " & strError & " Would you like to retry the " & strCmd & " command?", vbYesNo, " Retry Command?")
                Case vbYes
                    ErrorCheck = True
                    Exit Function
                Case vbNo
                    ErrorCheck = False
                    If SoftLinx.Running = 1 Then
                        Select Case MsgBox("Do you wish to stop running methods?", vbYesNo, "Continue methods?")
                            Case vbYes
                                XPeel.StopRun
                                Exit Function
                            Case vbNo
                                Exit Function
                        End Select
                    End If
            End Select
    End If
    
End Function

Public Sub XPeel_Peel(strParameters As String)
'
    Dim strXpeel As String
    
    strXpeel = "xpeel:" + strParameters

    XPeelCmd (strXpeel)
    bErrorFlag = False
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
    
    If Left(strRsp, 4) <> "*ack" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd (strXpeel)
        strRsp = GetResponse
    End If
   ' Output (StatusTranslate(strRsp))

        Do While Left(strRsp, 6) <> "*ready"
            
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        Loop
        
        If (ErrorCheck(bErrorFlag, "reset")) Then
        XPeel_Peel (strParameters)
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub

Public Sub XPeel_PlateCheck(s As String)
'

    XPeelCmd ("platecheck:" + s)
    bErrorFlag = False
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
    
    If Left(strRsp, 4) <> "*ack" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("platecheck:" + s)
        strRsp = GetResponse
    End If
   ' Output (StatusTranslate(strRsp))

        Do While Left(strRsp, 6) <> "*ready"
            
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        Loop
        
        If (ErrorCheck(bErrorFlag, "platecheck")) Then
        XPeel_PlateCheck (s)
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub

Public Sub XPeel_Reset()
'

    XPeelCmd ("reset")
    bErrorFlag = False
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
    
    If Left(strRsp, 4) <> "*ack" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("reset")
        strRsp = GetResponse
    End If
   ' Output (StatusTranslate(strRsp))

        Do While Left(strRsp, 6) <> "*ready"
            
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        Loop
        
        If (ErrorCheck(bErrorFlag, "reset")) Then
        XPeel_Reset
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_Restart()
'Used just like a power cycle of the Xpeel.

    XPeelCmd ("restart")
    bErrorFlag = False
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
    
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("restart")
        strRsp = GetResponse
    End If
   ' Output (StatusTranslate(strRsp))

        Do While Left(strRsp, 6) <> "*ready"
            
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        Loop
        
        If (ErrorCheck(bErrorFlag, "reset")) Then
        XPeel_Restart
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_Status()

    bErrorFlag = False
    XPeelCmd ("stat")
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
    
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("stat")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        Loop
        
        If (ErrorCheck(bErrorFlag, "status")) Then
        XPeel_Status
        Else
            Output (StatusTranslate(strRsp))
        End If

End Sub

Public Sub XPeel_Version()
    
    bErrorFlag = False
    XPeelCmd ("version")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("version")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "version")) Then
        XPeel_Version
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_TapeCheck()
    
    bErrorFlag = False
    XPeelCmd ("tapeleft")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("tapeleft")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "tapeleft")) Then
        XPeel_TapeCheck
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub

Public Sub XPeel_SealCheck()
    
    bErrorFlag = False
    XPeelCmd ("sealcheck")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("sealcheck")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "sealcheck")) Then
        XPeel_SealCheck
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_SealStat()
    
    bErrorFlag = False
    XPeelCmd ("sealstat")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("sealstat")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "sealstat")) Then
        XPeel_SealStat
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_SealHigher(s As String)
    
    
    bErrorFlag = False
    XPeelCmd ("sealhigher:" + s)
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("sealhigher:" + s)
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, ("sealhigher"))) Then
        XPeel_SealHigher (s)
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_SealLower(s As String)
    
    
    bErrorFlag = False
    XPeelCmd ("seallower:" + s)
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("seallower:" + s)
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, ("seallower"))) Then
        XPeel_SealLower (s)
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub
Public Sub XPeel_MoveSpool()
    
    bErrorFlag = False
    XPeelCmd ("movespool")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("movespool")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "movespool")) Then
        XPeel_MoveSpool
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub
Public Sub XPeel_MoveOut()
    
    bErrorFlag = False
    XPeelCmd ("moveout")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("moveout")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
            If strRsp = "TimedOut" Or strRsp = "Invalid" Or strRsp = "Incomplete" Then
                MsgBox "Communication error sending 'moveout' command."
                Exit Sub
            End If
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "moveout")) Then
        XPeel_MoveOut
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub

Public Sub XPeel_MoveIn()
    
    bErrorFlag = False
    XPeelCmd ("movein")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("movein")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "movein")) Then
        XPeel_MoveIn
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub

Public Sub XPeel_MoveDown()
    
    bErrorFlag = False
    XPeelCmd ("movedown")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("movedown")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "movedown")) Then
        XPeel_MoveDown
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


Public Sub XPeel_MoveUp()
    
    bErrorFlag = False
    XPeelCmd ("moveup")
    bVersionTag = True
    
    If SoftLinx.SimulateMode Then Exit Sub
    strRsp = GetResponse
            
    If Left(strRsp, 9) = "*error:09" Then 'A command may have been sent while machine was running. Resend the command.
        XPeelCmd ("moveup")
        strRsp = GetResponse
    End If
            
        Do While Left(strRsp, 6) <> "*ready"
                        
            Output (StatusTranslate(strRsp))
            strRsp = GetResponse
                       
            If Left(strRsp, 6) = "*error" Then
            strError = StatusTranslate(strRsp)
            bErrorFlag = True
                If Left(strRsp, 8) = "*error:5" Then MsgBox "The XPeel has been halted. Check it for physical errors, then press its select button to reset it. Click OK to continue.", vbCritical, "System Halted"
            End If
            
        
        Loop

        If (ErrorCheck(bErrorFlag, "moveup")) Then
        XPeel_MoveUp
        Else
            Output (StatusTranslate(strRsp))
        End If
        
End Sub


'*****************************************************
'Purpose: Issue any commands to the XPeel™
'Inputs:
'   strCraneCmd: Command to be issued.
'*****************************************************

Public Function XPeelCmd(ByVal strXPeelCmd As String, Optional bIgnoreMthdRunning As Boolean = False) As Boolean
    Dim iRetry As Integer
    Dim i As Integer
    Dim strEcho As String
    Dim strResp As String
    
    Dim strMessage As String
    Dim strCmd As String
    
    strCmd = Left(strXPeelCmd, 3)
    
    Select Case strCmd:
    Case "sta":
        strCmd = "Status"
    Case "ver":
        strCmd = "Version"
    Case "res":
        
        If Left(strXPeelCmd, 4) = "rese" Then
                strCmd = "Reset"
            Else
                strCmd = "Restart"
            End If
                
    Case "xpe":
        strCmd = "XPeel"
    Case "sea"
        
            If Left(strXPeelCmd, 6) = "sealch" Then
                strCmd = "Seal Check"
            ElseIf Left(strXPeelCmd, 6) = "seallo" Then
                strCmd = "Seal Lower"
            ElseIf Left(strXPeelCmd, 6) = "sealhi" Then
                strCmd = "Seal Higher"
            ElseIf Left(strXPeelCmd, 6) = "sealst" Then
                strCmd = "Seal Status"
            Else
            strCmd = "unknown seal command"
            End If
    Case "tap"
        strCmd = "Tape Left"
    Case "pla"
        strCmd = "Plate Check"
    Case "sen"
        strCmd = "Sense"
    Case "mov"
            If Left(strXPeelCmd, 6) = "moveup" Then
                strCmd = "Move Up"
            ElseIf Left(strXPeelCmd, 6) = "movedo" Then
                strCmd = "Move Down"
            ElseIf Left(strXPeelCmd, 6) = "movein" Then
                strCmd = "Move In"
            ElseIf Left(strXPeelCmd, 6) = "moveou" Then
                strCmd = "Move Out"
            ElseIf Left(strXPeelCmd, 6) = "movesp" Then
                strCmd = "Move Spool"
            Else
            strCmd = "unknown move command"
            End If
    Case Else
        strCmd = "unknown"
    End Select
 
 If SoftLinx.SimulateMode = True And SoftLinx.Initialized = False Then
 
    strMessage = "The " & strCmd & " command would be sent to XPeel."
    Output (strMessage)

    
    Exit Function
 End If
 strMessage = "The " & strCmd & " command is being sent to XPeel."
 Output (strMessage)



    strResp = ""


    If frmComPrts.MSComm1.PortOpen = False Then
        frmComPrts.MSComm1.PortOpen = True
    End If
    
    'Send the command to the robot

        'clear the buffer - extremely important before sending commands.
        Do While frmComPrts.MSComm1.InBufferCount > 0
            strResp = frmComPrts.MSComm1.Input
            'DoEvents
        Loop

        frmComPrts.MSComm1.Output = "*" & strXPeelCmd & vbCrLf
        
        iRetry = iRetry + 1

        

    Sleep 1000
 
    End Function


Public Function StatusTranslate(ByVal strXPeelstatus As String) As String

'Check type of incomming message. Possible Cases:

'error - from basically everything. find this case FIRST. Note this may now be part of the *ready response for the XPeel.
If Left(strXPeelstatus, 6) = "*error" Then
    Dim errCode As String
    errCode = Mid(strXPeelstatus, 8, 2)
    StatusTranslate = ErrorCodeTranslator(errCode)
    
    'since an error has occurred, before accepting any other commands, prompt the user to retry or continue processing.
    'Do this outside this function.
    
    Exit Function
    
End If
    

'ready - from everything, ensures the XPeel can accept a new command. For the XPeel, this can also report errors.
If Left(strXPeelstatus, 6) = "*ready" Then

'Do a "ready translation" here.
ReadyCodeTranslator (strXPeelstatus)

StatusTranslate = "XPeel is ready for the next command."
    Exit Function
    
End If
    

'Ack - from reset, movement, and sensor commands
If Left(strXPeelstatus, 4) = "*ack" Then
StatusTranslate = "XPeel has received the command and is now performing the process."
'when Ack is called out, then the program will poll the machine every 2 seconds for some sort of response, looking for ready.
Exit Function
End If

'tapeleft
If Left(strXPeelstatus, 5) = "*tape" Then
StatusTranslate = "Tape Check: Approximately" + Mid(strXPeelstatus, 7, 2) + "0 deseals remaining."
Exit Function
End If


'Seal detected
If Left(strXPeelstatus, 5) = "*seal" Then
StatusTranslate = "Seal detected sensor set to" + Mid(strXPeelstatus, 7, 2) + "."
Exit Function
End If


'poweron/homing - power up.
If Left(strXPeelstatus, 8) = "*poweron" Then
StatusTranslate = "XPeel is powering on now."
Exit Function
End If

If Left(strXPeelstatus, 7) = "*homing" Then
StatusTranslate = "XPeel is homing the system."
Exit Function
End If

'manual - button pressed.
If Left(strXPeelstatus, 7) = "*manual" Then
StatusTranslate = " has been issued a manual command."
Exit Function
End If

'if version is called...

If bVersionTag = True And (Left(strXPeelstatus, 2) = "*1" Or Left(strXPeelstatus, 2) = "*2" Or Left(strXPeelstatus, 2) = "*3" Or Left(strXPeelstatus, 2) = "*4") Then
StatusTranslate = "XPeel is using firmware version " & Mid(strXPeelstatus, 2, 3) & "."
bVersionTag = False
Exit Function
End If


'send a status command to the XPeel™
'get the response from that and return the string

End Function

Public Function ReadyCodeTranslator(ByVal strMessage As String) As String
    Dim strStatusA, strStatusB, strStatusC As String
    
    'Get all 3 int status codes here. Analyze in this order: Conveyor, Left DC, Right DC. Report to messagelog.
    strStatusA = (Mid(strMessage, 8, 2))
    strStatusB = (Mid(strMessage, 11, 2))
    strStatusC = (Mid(strMessage, 14, 2))

    Output (ErrorCodeTranslator(strStatusA))
    Output (ErrorCodeTranslator(strStatusA))
    Output (ErrorCodeTranslator(strStatusC))
        
End Function

'Handles all messages to a set output in this function

Public Function Output(ByVal strMsg As String)

    If strMsg = "" Then Exit Function
    
    frmRunStatus.lstLog.AddItem Time() & ": " & strMsg, 0
    SoftLinx.Message = Time() & ": " & strMsg
    
    
    
    ' ListBox must have the Focus
    frmRunStatus.lstLog.SetFocus
    frmRunStatus.lstLog.Selected(0) = True
    
    ' Force ListBox to start from the top
    If frmRunStatus.lstLog.ListIndex > 0 Then frmRunStatus.lstLog.ListIndex = 0
    

    

    
End Function

Public Function ErrorCodeTranslator(ByVal errCode As String) As String

'Cases here. Yes there is a lot.

Dim strMsg As String

Select Case errCode
        Case "00"
            strMsg = ErrorCodeTranslator = ""
            Exit Function
        
        Case "01"
            strMsg = "Conveyor Motor has stalled."
        
        Case "02"
            strMsg = "Elevator Motor has stalled."
            
        Case "03"
            strMsg = "Take Up Spool has stalled."
            
        Case "04"
            strMsg = "Seal detected."
            
        Case "05"
            strMsg = "Illegal command."
        
        Case "06"
            strMsg = "Plate not found in system."
        
        Case "07"
            strMsg = "Out of tape, or tape is broken."
        
        Case "08"
            strMsg = "Parameters not saved."
            
        Case "09"
            strMsg = "Stop button pressed while running a command."
        
        Case "10"
            strMsg = "Steal Sensor unplugged or broken."
        
        Case "20"
            strMsg = "Less than 30 seals remaining on supply spool."
        
        Case "21"
            strMsg = "Room for less than 30 seals on take up spool."
        
        Case "51"
            strMsg = "Emergency Stop: Power relay not settable. Check XPeel hardware."
        
        Case "52"
            strMsg = "Circuitry fault detected. Turn power off and check XPeel hardware."
'
'        Case Else
'            strMsg = "Unknown error."
End Select

ErrorCodeTranslator = "Message Code #" & errCode & ": " & strMsg



End Function


'*****************************************************
'Purpose: Get the response from the last command issued to the XPeel
'*****************************************************
Public Function GetResponse(Optional timeout As Long = 5000) As String
    Dim lStartTime As Long
    Dim strResponse As String
    Dim strTempResponse As String
    Dim strTempArray() As String
    Dim R As String

    lStartTime = StartHCIntervalTimer
    R = ""
    strResponse = ""
    
    While ((R <> Chr$(13)) Or (Left$(Trim(strResponse), 1) <> "*")) And (Not HCIntervalTimerExpired(lStartTime, timeout))
        R = frmComPrts.MSComm1.Input
        If R <> "" Then
            If R <> Chr$(13) And R <> Chr$(10) Then
                strResponse = strResponse & R
            End If
            lStartTime = StartHCIntervalTimer
        End If
        DoEvents
    Wend
    
    If R <> Chr$(13) Then
        If Len(strResponse) > 0 Then
            GetResponse = "Incomplete"
        Else
            GetResponse = "TimedOut"
        End If
        Exit Function
    End If
    
    If (Left$(Trim(strResponse), 1) <> "*") Then
        GetResponse = "Invalid"
        Exit Function
    End If
    
    GetResponse = Trim(strResponse)

End Function








