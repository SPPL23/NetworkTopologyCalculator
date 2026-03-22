# Network Topology Calculator

class NetworkTopologyCalculator:
    def networkaddress(self, NA, Prefix):
        # Input Assigned Network Address
        print(f"\nEnter the assigned network address for each octet x.x.x.x")
        o1 = int(input("1st octet: "))
        o2 = int(input("2nd octet: "))
        o3 = int(input("3rd octet: "))
        o4 = int(input("4th octet: "))
        NA = [o1, o2, o3, o4]
        NA_int = map(str, NA)
        NA_str = ".".join(NA_int)
        Prefix = int(input(f"\nEnter the prefix length (e.g: 24): "))
        while Prefix < 8 or Prefix > 32:
            print(f"Prefix length is out of range. Please enter a value between 0 and 32.")
            Prefix = int(input(f"\nEnter the prefix length (e.g: 24): "))
        print(f"\nNetwork Address: {NA_str}/{Prefix}")
        return NA, Prefix
    
    def affectedOctet(self, NA, Prefix):
        AffOct = Prefix / 8
        underlined_str = ""
        match AffOct:
            case AffOct if AffOct <= 1.00 and AffOct != 0.00:
                affected_index = 0
                underlined_na = [f"{octet}"
                                if i == affected_index
                                else str(octet)
                                for i, octet in enumerate(NA)]
                underlined_str = ".".join(underlined_na)
                print(f"Affected Octet: {underlined_str}")
            case AffOct if AffOct <= 2.00 and AffOct != 0.00:
                affected_index = 1
                underlined_na = [f"{octet}"
                                if i == affected_index
                                else str(octet)
                                for i, octet in enumerate(NA)]
                underlined_str = ".".join(underlined_na)
                print(f"Affected Octet: {underlined_str}")
            case AffOct if AffOct <= 3.00 and AffOct != 0.00:
                affected_index = 2
                underlined_na = [f"{octet}"
                                if i == affected_index
                                else str(octet)
                                for i, octet in enumerate(NA)]
                underlined_str = ".".join(underlined_na)
                print(f"Affected Octet: {underlined_str}")
            case AffOct if AffOct <= 4.00 and AffOct != 0.00:
                affected_index = 3
                underlined_na = [f"{octet}"
                                if i == affected_index
                                else str(octet)
                                for i, octet in enumerate(NA)]
                underlined_str = ".".join(underlined_na)
                print(f"Affected Octet: {underlined_str}")
            case default:
                print(f"Prefix length is out of range. Please enter a value between 0 and 32.")
        return underlined_str
    
    def submask(self, Prefix):
        submask = [0, 0, 0, 0]
        for i in range(4):
            if Prefix >= 8:
                submask[i] = 255
                Prefix -= 8
            else:
                submask[i] = (256 - (2 ** (8 - Prefix))) if Prefix > 0 else 0
                break
        print(f"Subnet Mask: {'.'.join(map(str, submask))}")
        return submask

    def wildcardmask(self, submask):
        wildcardmask = [255 - octet for octet in submask]
        print(f"Wildcard Mask: {'.'.join(map(str, wildcardmask))}")
        return wildcardmask
    
    def newnetworkaddress(self, NA, submask):
        newNA = [NA[i] & submask[i] for i in range(4)]
        print(f"New Network Address: {'.'.join(map(str, newNA))}")
        return newNA
    
    def broadcastaddress(self, NA, wildcardmask):
        broadcast = [NA[i] | wildcardmask[i] for i in range(4)]
        print(f"Broadcast Address: {'.'.join(map(str, broadcast))}")
        return broadcast
    
    def hostrange(self, newNA, broadcast):
        if newNA[3] < 255:
            newNA[3] += 1
        if broadcast[3] > 0:
            broadcast[3] -= 1
        print(f"Host Range: {'.'.join(map(str, newNA))} - {'.'.join(map(str, broadcast))}")
        return newNA, broadcast
    
    def totalnumhosts(self, Prefix):
        num_hosts = (2 ** (32 - Prefix))
        print(f"Total Number of Hosts: {num_hosts}")
        return num_hosts
    
    def usablehosts(self, num_hosts):
        if num_hosts > 2:
            usable_hosts = num_hosts - 2
            print(f"Usable Hosts: {usable_hosts}")
            return usable_hosts
        else:
            print(f"Usable Hosts: (Not enough hosts for network and broadcast addresses)")
            return 0
        
class SubnetMaskCalculator:
    def subnetmask(self, Prefix):
        submask = [0, 0, 0, 0]
        for i in range(4):
            if Prefix >= 8:
                submask[i] = 255
                Prefix -= 8
            else:
                submask[i] = (256 - (2 ** (8 - Prefix))) if Prefix > 0 else 0
                break
        print(f"Subnet Mask: {'.'.join(map(str, submask))}")
        return submask
    
NTC = NetworkTopologyCalculator()
SMC = SubnetMaskCalculator()

class Menu:
    def display_menu(self):
        print(f"\nNetwork Topology Calculator\n1. Calculate Network Address\n2. Calculate Subnet Mask\n3. Exit")
        MMenu = input(f"\nEnter option 1-3: ")

        while MMenu != "3":
            try:
                if MMenu == "1":
                    NA, prefix = NTC.networkaddress(None, None)
                    affected_str = NTC.affectedOctet(NA, prefix)
                    submask = NTC.submask(prefix)
                    wildcard = NTC.wildcardmask(submask)
                    newNA = NTC.newnetworkaddress(NA, submask)
                    broadcast = NTC.broadcastaddress(NA, wildcard)
                    first_usable, last_usable = NTC.hostrange(newNA, broadcast)
                    num_hosts = NTC.totalnumhosts(prefix)
                    usable_hosts = NTC.usablehosts(num_hosts)
                    Start.display_menu()
                    break
                elif MMenu == "2":
                    prefix = int(input(f"\nEnter the prefix length (e.g: 8 - 32): "))
                    if prefix < 8 or prefix > 32:
                        print(f"Prefix length is out of range. Please enter a value between 8 and 32.")
                        continue
                    else:
                        submask = SMC.subnetmask(prefix)
                        Start.display_menu()
                        break
                else:
                    print(f"Exiting the Network Topology Calculator. Goodbye!")
                    break
            except ValueError:
                print(f"Invalid input. Please enter numeric values for octets and prefix length.")

        return MMenu
    
Start = Menu()
Start.display_menu()

