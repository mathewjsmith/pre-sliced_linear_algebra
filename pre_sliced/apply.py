from pre_sliced.operands import Operand, PartitionedOperand
import inspect


def apply(f, *operands: Operand):
    arity = len(inspect.signature(f).parameters)
    assert arity == len(operands), "The number of operands do not match the arity of the function."

    partitionings = [x.partition() for x in operands]

    def _apply(f, *operands: PartitionedOperand):
        if all(x.is_complete() for x in operands):
            return operands[-1].combine().value
        else:
            exposes = [x.expose() for x in operands]
            alpha = f(*[x.exposed_value() for x in exposes])
            exposes[-1] = exposes[-1].update(alpha)
            repartitionings = (x.repartition() for x in exposes)
            return _apply(f, *repartitionings)

    return _apply(f, *partitionings)
