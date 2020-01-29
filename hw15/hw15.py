import ipaddress


class Router:
    interfaces = {}
    route_table = {}

    def add_interface(self, name, address):
        self.interfaces[name] = ipaddress.ip_interface(address)
        self.route_table[self.interfaces[name].network] = self.interfaces[name].ip

    def del_interface(self, name):
        del(self.interfaces[name])

    def get_interfaces(self):
        res = ''
        for k, v in self.interfaces.items():
            res += f'interface {k}: {str(v)}\n'
        return res

    def add_route(self, destination, gateway):
        network = ipaddress.ip_network(destination, False)
        address = ipaddress.ip_address(gateway)
        for net in self.route_table.keys():
            if address in net:
                self.route_table[network] = address
                break
        else:
            raise Exception("Gateway is not available")

    def del_route(self, destination):
        del(self.route_table[ipaddress.ip_network(destination, False)])

    def get_routes(self):
        res = ''
        for k, v in self.route_table.items():
            res += f'route to {str(k)} via {str(v)}\n'
        return res


if __name__ == '__main__':
    r1 = Router()
    r1.add_interface('eth1', '192.168.5.14/24')
    print(r1.get_interfaces())

    r1.add_route('172.16.0.0/16', '192.168.5.1')
    # r1.add_route('172.24.0.0/16', '192.168.8.1')
    r1.add_route('172.24.0.0/16', '172.16.8.1')
    print(r1.get_routes())
