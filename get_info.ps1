Get-WmiObject -Class win32_LocalTime
Get-Process
Get-WmiObject -Class win32_UserAccount
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true -ComputerName . | Format-Table -Property IPAddress
