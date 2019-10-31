def register(abstract_class):
    def _registerer(concrete_class):
        if getattr(abstract_class, '__backend__', None):
            raise ValueError(
                f'{abstract_class.__backend__} is already registered '
                f'as a backend for {abstract_class}; cannot register '
                f'{concrete_class} as another one.'
            )
        else:
            abstract_class.__backend__ = concrete_class

        return concrete_class

    return _registerer
