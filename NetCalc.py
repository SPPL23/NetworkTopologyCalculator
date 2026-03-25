# Network Topology Calculator

from restricted_input import r_input
import pyperclip

class NetworkTopologyCalculator:
    def networkaddress(self, NA, Prefix):

        print('\nEnter the assigned network address for each octet x.x.x.x')
        o1 = int(r_input('1st octet: ', maxlength=3))
        o2 = int(r_input('2nd octet: ', maxlength=3))
        o3 = int(r_input('3rd octet: ', maxlength=3))
        o4 = int(r_input('4th octet: ', maxlength=3))
        NA = [o1, o2, o3, o4]
        NA_int = map(str, NA)
        NA_str = '.'.join(NA_int)
        Prefix = int(r_input('\nEnter the prefix length (e.g: 24): ', maxlength=2))
        if Prefix < 8 or Prefix > 32:
            print('Prefix length is out of range. Please enter a value between 0 and 32.')
            Prefix = int(r_input('\nEnter the prefix length (e.g: 24): ', maxlength=2))
        else:
            print(f'\nNetwork Address: {NA_str}/{Prefix}')
            return (NA, Prefix)

    def affectedOctet(self, NA, Prefix):
        if 1 <= Prefix <= 32:
                affected_index = (Prefix - 1) // 8
                underlined_na = ['X' if i == affected_index else str(octet) for i, octet in enumerate(NA)]
                underlined_str = '.'.join(underlined_na)
                print(f'Affected Octet: {underlined_str}')
                return underlined_str
        if Prefix == 0:
            print('Affected Octet: X.0.0.0')
            return 'X.0.0.0'
        else:
            print('Prefix length is out of range. Please enter a value between 0 and 32.')
            return ''

    def submask(self, Prefix):
        submask = [0, 0, 0, 0]
        for i in range(4):
            if Prefix >= 8:
                submask[i] = 255
                Prefix -= 8
            else:
                submask[i] = 256 - 2 ** (8 - Prefix) if Prefix > 0 else 0
                break
        print(f'Subnet Mask: {'.'.join(map(str, submask))}')
        return submask

    def wildcardmask(self, submask):
        wildcardmask = [255 - octet for octet in submask]
        print(f'Wildcard Mask: {'.'.join(map(str, wildcardmask))}')
        return wildcardmask

    def newnetworkaddress(self, NA, submask):
        newNA = [NA[i] & submask[i] for i in range(4)]
        print(f'New Network Address: {'.'.join(map(str, newNA))}')
        return newNA

    def broadcastaddress(self, NA, wildcardmask):
        broadcast = [NA[i] | wildcardmask[i] for i in range(4)]
        print(f'Broadcast Address: {'.'.join(map(str, broadcast))}')
        return broadcast

    def hostrange(self, newNA, broadcast):
        if newNA[3] < 255:
            newNA[3] += 1
        if broadcast[3] > 0:
            broadcast[3] -= 1
        print(f'Host Range: {'.'.join(map(str, newNA))} - {'.'.join(map(str, broadcast))}')
        return (newNA, broadcast)

    def totalnumhosts(self, Prefix):
        num_hosts = 2 ** (32 - Prefix)
        print(f'Total Number of Hosts: {num_hosts}')
        return num_hosts

    def usablehosts(self, num_hosts):
        if num_hosts > 2:
            usable_hosts = num_hosts - 2
            print(f'Usable Hosts: {usable_hosts}')
            return usable_hosts
        else:
            print('Usable Hosts: (Not enough hosts for network and broadcast addresses)')
            return 0

class SubnetMaskCalculator:
    def subnetmask(self, Prefix):
        submask = [0, 0, 0, 0]
        for i in range(4):
            if Prefix >= 8:
                submask[i] = 255
                Prefix -= 8
            else:
                submask[i] = 256 - 2 ** (8 - Prefix) if Prefix > 0 else 0
                break
        print(f'Subnet Mask: {'.'.join(map(str, submask))}')
        return submask

class CTCB:
    def copytocb(self, NA, prefix, submask, wildcard, newNA, broadcast, first_usable, last_usable, num_hosts, usable_hosts):
        
        sub_str = '.'.join(map(str, submask))
        wild_str = '.'.join(map(str, wildcard))

        first_str = '.'.join(map(str, first_usable))
        last_str = '.'.join(map(str, last_usable))

        text_to_copy = (
            f"NetCalc Results\n"
            f"New Network Address: {'.'.join(map(str, [newNA[i] - 1 if i == 3 else newNA[i] for i in range(4)]))}\n"
            f"Subnet Mask: {sub_str}\n"
            f"Wildcard Mask: {wild_str}\n"
            f"Broadcast Address: {'.'.join(map(str, [last_usable[i] + 1 if i == 3 else last_usable[i] for i in range(4)]))}\n"
            f"Host Range: {first_str} - {last_str}\n"
            f"Total Hosts: {num_hosts}\n"
            f"Usable Hosts: {usable_hosts}\n"
        )
        
        pyperclip.copy(text_to_copy)
        print('\n[!] Results formatted and copied to clipboard.')

NTC = NetworkTopologyCalculator()
SMC = SubnetMaskCalculator()
ClipBoard = CTCB()

class Menu:
    def display_menu(self):
        while True:
            print('\nNetwork Topology Calculator')
            print('1. Calculate Network Address')
            print('2. Calculate Subnet Mask')
            print('3. Exit / [Any other key to exit]')
            
            MMenu = input('Enter option 1-3: ')

            if MMenu == '3':
                print('Exiting the Network Topology Calculator. Goodbye!')
                break

            try:
                if MMenu == '1':
                    NA, prefix = NTC.networkaddress(None, None)
                    affected_str = NTC.affectedOctet(NA, prefix)
                    submask = NTC.submask(prefix)
                    wildcard = NTC.wildcardmask(submask)
                    newNA = NTC.newnetworkaddress(NA, submask)
                    broadcast = NTC.broadcastaddress(NA, wildcard)
                    first_usable, last_usable = NTC.hostrange(newNA, broadcast)
                    num_hosts = NTC.totalnumhosts(prefix)
                    usable_hosts = NTC.usablehosts(num_hosts)
                    
                    choice = input('\nCopy results to clipboard? (y/n): ').lower()
                    if choice == 'y':
                        ClipBoard.copytocb(NA, prefix, submask, wildcard, newNA, broadcast, first_usable, last_usable, num_hosts, usable_hosts)
                
                elif MMenu == '2':
                    prefix_input = r_input('\nEnter the prefix length (e.g: 8 - 32): ', maxlength=2)
                    prefix = int(prefix_input)
                    
                    if 8 <= prefix <= 32:
                        submask = SMC.subnetmask(prefix)
                    else:
                        print('Prefix length is out of range. Please enter 8-32.')
                
                else:
                    print('Exiting the Network Topology Calculator. Goodbye!')
                    break

            except ValueError:
                print('Invalid input. Please enter numeric values.')
            
            input("\nPress Enter to return to the menu...")

        return MMenu
        
Start = Menu()
Start.display_menu()