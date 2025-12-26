def build_pipeline(operation_names):

    operations = {                              # Define supported operations
        "double": lambda x: x * 2,
        "triple": lambda x: x * 3,
        "increment": lambda x: x + 1,
        "decrement": lambda x: x - 1,
        "square": lambda x: x ** 2,
        "negate": lambda x: -x
    }

    for name in operation_names:                # Validate operation names
        if name not in operations:
            raise KeyError(name)


    def pipeline(x):                    # Build the pipeline function
        value = x
        for name in operation_names:
            value = operations[name](value)
        return value

    return pipeline