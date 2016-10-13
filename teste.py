x = 'text on a string'
print('test')
print(x)


I've been trying to run some piece of code on terminal using this command, but the selected code never run properly. Seems that the command run it line by line, using the command python -c "commands" which makes the terminal not run all the selection. Follow the terminal message:

Microsoft Windows [Version 10.0.14942]                                                                                                                                                                                                 
(c) 2016 Microsoft Corporation. All rights reserved.                                                                                                                                                                                   
                                                                                                                                                                                                                                       
C:\Development\Python\PythonTrainning>c:\python35\python.exe -c "x = 'text on a string'                                                                                                                                                
                                                                                                                                                                                                                                       
C:\Development\Python\PythonTrainning>print('test')                                                                                                                                                                                    
Unable to initialize device PRN                                                                                                                                                                                                        
                                                                                                                                                                                                                                       
C:\Development\Python\PythonTrainning>print(x)"                                                                                                                                                                                        
                                                                                                                                                                                                                                       
C:\Development\Python\PythonTrainning>