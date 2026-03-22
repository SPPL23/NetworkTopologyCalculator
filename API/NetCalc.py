# Updated NetCalc.py
class NetworkTopologyCalculator:
    # We removed input() so the API can pass data directly here
    def get_all_metrics(self, octets, prefix):
        submask = self.submask(prefix)
        wildcard = self.wildcardmask(submask)
        new_na = [octets[i] & submask[i] for i in range(4)]
        broadcast = [octets[i] | wildcard[i] for i in range(4)]
        
        # Calculate host range without modifying the original lists
        first_usable = list(new_na)
        last_usable = list(broadcast)
        if first_usable[3] < 255: first_usable[3] += 1
        if last_usable[3] > 0: last_usable[3] -= 1

        num_hosts = (2 ** (32 - prefix))
        
        return {
            "network_address": f"{'.'.join(map(str, new_na))}/{prefix}",
            "subnet_mask": ".".join(map(str, submask)),
            "wildcard_mask": ".".join(map(str, wildcard)),
            "broadcast": ".".join(map(str, broadcast)),
            "host_range": f"{'.'.join(map(str, first_usable))} - {'.'.join(map(str, last_usable))}",
            "total_hosts": num_hosts,
            "usable_hosts": max(0, num_hosts - 2)
        }

    def submask(self, prefix):
        mask = [0, 0, 0, 0]
        temp_prefix = prefix
        for i in range(4):
            if temp_prefix >= 8:
                mask[i] = 255
                temp_prefix -= 8
            else:
                mask[i] = (256 - (2 ** (8 - temp_prefix))) if temp_prefix > 0 else 0
                break
        return mask

    def wildcardmask(self, submask):
        return [255 - octet for octet in submask]

# Note: Keep your existing Menu class below if you still want the CLI to work!