class Server:
    def __init__(self, hostname, ip_address, ram_gb, powered=False):
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram_gb = ram_gb
        self.powered = powered

    def power_on(self):
        self.powered = True

    def power_off(self):
        self.powered = False

    def update_ram(self, new_ram_gb):
        try:
            value = float(new_ram_gb)
        except (TypeError, ValueError):
            raise ValueError("RAM value must be a number")
        if value <= 0:
            raise ValueError("RAM must be positive")
        self.ram_gb = value

    def __str__(self):
        status = "on" if self.powered else "off"
        return f"{self.hostname} ({self.ip_address}) - {self.ram_gb}GB - {status}"


class DataCenter:
    def __init__(self, region_name):
        self.region = region_name
        self.servers = []

    def register_server(self, server):
        if not hasattr(server, "hostname"):
            raise TypeError("register_server expects a Server-like object")
        self.servers.append(server)

    def active_hostnames(self):
        return [s.hostname for s in self.servers if getattr(s, "powered", False)]

    def show_active(self):
        active = self.active_hostnames()
        if not active:
            print(f"Data center {self.region}: no active servers")
            return
        print(f"Data center {self.region}: active servers:")
        for h in active:
            print(f"- {h}")


def demo():
    dc = DataCenter("us-east-1")
    s1 = Server("Web-01", "10.0.0.10", 8)
    s2 = Server("Db-01", "10.0.0.11", 16)
    dc.register_server(s1)
    dc.register_server(s2)
    s2.power_on()
    dc.show_active()


if __name__ == "__main__":
    demo()
