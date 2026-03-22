# NetCalc
## Network Topology Calculator
>[!NOTE]
>- The reason why I made this simple python CLI program is so that instead of doing the calculations manually like pulling up the *calculator, listing down the necessary details like Subnetmask, Wildcard Mask, Network Address, Broadcast Address, Host Range, First and Last Usable, blablabla* is so that I can **just look at the terminal and read everything there** without going back and fort with notepad. Also because I suck at calculating and *kept failing my tests with the wrong IP assignment.*
## What to download
>[!TIP]
>- You can either download
>   - **[NetCalc.py](https://raw.githubusercontent.com/SPPL23/NetworkTopologyCalculator/refs/heads/main/NetCalc.py)** <u>***Right-click***</u> and then <u>***Save as***</u>
>
>       *or*
>   - **[NetCalc.exe](https://github.com/SPPL23/NetworkTopologyCalculator/raw/refs/heads/main/dist/NetCalc.exe)** which is in the <u>***dist***</u> folder

>[!IMPORTANT]
>## <center>**Don't download the API, I was just testing something.**</center>
### Features
1. *Nothing much*, there's a **menu**. You enter the values of *1, 2,* and *3* that's all.
2. **1st option** prompts you to **enter the assigned address** by individually typing the four octets and then asks for the prefix assigned to that address.
<strong>Example: </strong>
```
Enter the assigned network address for each octet x.x.x.x
1st octet: 192
2nd octet: 168a
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
>- So far, for the **2nd option**. I made sure that **you can only enter the prefix of *8* up until *32***. *If you enter any value less than 8 or greater than 32. It will just tell you you can't enter any value from what was indicated.*

> [!WARNING]
>- For the **1st option**, *I* **forgot to limit the maximum character length or I guess integer length** *that you can enter for the first four user input. So far you can enter more than 3 digits for each octet and can* **go beyond 255**.
>- ***I'm too lazy to fix that shit now, it is what it is.***

# If you want it as a quick access CLI tool in command prompt
>[!TIP]
><strong>
>1. Make sure to save the NetCalc.exe file to a specific path/folder
>2. Go to the start menu and search environment variables
>![Step2](https://i.imgur.com/8VJWYov.png)
>3. Click `Environment Variables`
>![Step3](https://i.imgur.com/xPtf0Fa.png)
>4. On the Users tab, double click path
>![Step4](https://i.imgur.com/fUH1MDz.png)
>5. Click new, paste the current path directory of where the NetCalc.exe file is located.
>![Step5](https://i.imgur.com/wF011Zo.png)
>![Step5(2)](https://i.imgur.com/vB72aWz.png)
![Sample](https://s3.ezgif.com/tmp/ezgif-301739e2fdeecc4a.gif)
></strong>