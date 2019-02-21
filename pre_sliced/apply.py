from pre_sliced.operands import Operand, PartitionedOperand
import inspect


def apply(f, *expression: Operand):
    arity = len(inspect.signature(f).parameters)
    assert arity == len(expression), "The size of the expression did not match the arity of the function."

    partitionings = [x.partition() for x in expression]

    def _apply(f, *expression: PartitionedOperand):
        if all(x.is_complete() for x in expression):
            return expression[-1].combine().value
        else:
            exposes = [x.expose() for x in expression]
            alpha = f(*[x.exposed_value() for x in exposes])
            exposes[-1] = exposes[-1].update(alpha)
            repartitionings = (x.repartition() for x in exposes)
            return _apply(f, *repartitionings)

    return _apply(f, *partitionings)
