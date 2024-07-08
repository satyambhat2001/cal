# Use the latest Windows Server Core image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Set up PowerShell as the default shell
SHELL ["powershell", "-Command"]

# Install required components for sendemail
RUN Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force ; \
    Install-Module -Name BurntToast -Force ; \
    Install-Module -Name posh-git -Force ; \
    Invoke-WebRequest -Uri https://github.com/catonmat/sendemail/raw/master/sendemail.exe -OutFile C:\sendemail.exe

# Environment variables for sendemail
ENV SMTP_SERVER email@outlook.com
ENV SMTP_PORT 587
ENV SMTP_USER satyambhat@aarkglobalinc.com
ENV SMTP_PASSWORD Simple@321
