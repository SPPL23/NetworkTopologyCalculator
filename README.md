# NetCalc
## Network Topology Calculator
>[!NOTE]
>- The reason why I made this simple python CLI program is so that instead of doing the calculations manually like pulling up the *calculator, listing down the necessary details like Subnetmask, Wildcard Mask, Network Address, Broadcast Address, Host Range, First and Last Usable, blablabla* is so that I can **just look at the terminal and read everything there** without going back and fort with notepad. Also because I suck at calculating and *kept failing my tests with the wrong IP assignment.*
### UPDATE 03/25/2026
>[!WARNING]
>Used modules restricted_input(r_input) to restrict user input's character limit to 3.
> - The user is now unable to input more than 3 characters/numbers and can only enter the numbers 0 to 255.
> - Added the module pyperclip which will now prompt the user to copy to clipboard of the results you have inputted on option 1 of the menu.
## What to download
>[!TIP]
> - ### Automated set up for NetCalc.exe under the NetCalc_Installation folder. Just make sure to run the NetCalcSetUp.exe

>[!IMPORTANT]
>## <center>**Don't download the API, I was just testing something.**</center>
### Features
1. *Nothing much*, there's a **menu**. You enter the values of *1, 2,* and *3* that's all.
2. **1st option** prompts you to **enter the assigned address** by individually typing the four octets and then asks for the prefix assigned to that address.
<strong>Example: </strong>
```
Enter the assigned network address for each octet x.x.x.x
1st octet: 192
2nd octet: 168
3rd octet: 100
4th octet: 69

Enter the prefix length (e.g: 24): 26

 *Prints out all of the necessary/calculated results*
```
3. **2nd option** prompts you to **enter only the prefix**
<strong>Example: </strong>
```
Enter the prefix length (e.g: 8 - 32): 25
Subnet Mask: 255.255.255.128
```
4. **3rd** is **literally just an exit** even though you can just press CTRL and C
### Limitations
> [!IMPORTANT]
>- There is no windowed application, for now I am only capable of implementing python CLI programs.
>- So far, the **1st option**. You can only enter the values 0 up until 255 and can only enter 3 digits. You are also literally unable to put 4 or greater digits, I made sure you don't reset to the 1st octet if you enter less than 0 or greater than 255.
>- For the **2nd option**. I made sure that **you can only enter the prefix of *8* up until *32***. *If you enter any value less than 8 or greater than 32. It will just tell you you can't enter any value from what was indicated.*

> [!CAUTION]
>- ***This week 03/24/2026, I am motivated to make a program and publish it on github***
>- ### Next week, I'm probably going to be indefinitely lazy as shit and not even touch VSCode.

# If you want it as a quick access CLI tool in command prompt
>[!TIP]
># Sample / Demonstration
![Sample](NetCalcDemo.gif)
