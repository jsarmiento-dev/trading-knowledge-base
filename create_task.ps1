$taskName = "Trading Transcript Downloader"
$scriptPath = "C:\trading-knowledge-base\run_transcript.bat"
$action = New-ScheduledTaskAction -Execute $scriptPath
$trigger = New-ScheduledTaskTrigger -Daily -At 3:30AM
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Force -User "SYSTEM"
Write-Host "Task created successfully"
