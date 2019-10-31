def register(abstract_class):
    def _registerer(concrete_class):
        abstract_class.register(concrete_class)
        return concrete_class

    return _registerer
