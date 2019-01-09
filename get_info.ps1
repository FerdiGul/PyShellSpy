Get-WmiObject -Class win32_LocalTime
$str +="`n"
$str*20
Get-Process
Get-WmiObject -Class win32_UserAccount
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true -ComputerName . | Format-Table -Property IPAddress
Get-ItemProperty -Path Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
Get-Service

