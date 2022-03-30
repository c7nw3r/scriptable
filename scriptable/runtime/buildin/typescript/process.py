from scriptable.api.property_resolver import PropertySource


class Process:

    def __init__(self, property_source: PropertySource):
        self.property_source = property_source

    def __call__(self, *args):
        pass

    def __getitem__(self, item):
        if item == "env":
            return self.property_source
        raise ValueError(f"cannot handle {item}")

    def __contains__(self, item):
        return item == "env"
