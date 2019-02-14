from pre_sliced.matrix_entities.vectors import ForwardVector, PartitionedForwardVector, ExposedForwardVector


def test_empty_vector_creation():
    x = ForwardVector([])
    assert x.value == []


def test_vector_creation():
    x = ForwardVector([1, 2, 3])
    assert x.value == [1, 2, 3]


def test_partitioning():
    x = ForwardVector([1, 2, 3])
    x_part = x.partition()
    assert (x_part.top, x_part.bottom) == ([], [1, 2, 3])


def test_exposing():
    x_part = PartitionedForwardVector([], [1, 2, 3])
    x_exp = x_part.expose()
    assert x_exp.as_tuple() == ([], 1, [2, 3])


def test_exposed_value():
    x_exp = ExposedForwardVector([], 1, [2, 3])
    chi = x_exp.exposed_value()
    assert chi == 1


def test_repartitioning():
    x_exp = ExposedForwardVector([], 1, [2, 3])
    x_part = x_exp.repartition()
    assert x_part.as_tuple() == ([1], [2, 3])


def test_vector_is_not_complete():
    x_part = PartitionedForwardVector([1], [2, 3])
    assert x_part.is_complete() == False


def test_vector_is_complete():
    x_part = PartitionedForwardVector([1, 2, 3], [])
    assert x_part.is_complete() == True


def test_combine():
    x_part = PartitionedForwardVector([1], [2, 3])
    x = x_part.combine()
    assert x.value == [1, 2, 3]


def test_combine_complete_vector():
    x_part = PartitionedForwardVector([1, 2, 3], [])
    x = x_part.combine()
    assert x.value == [1, 2, 3]


def test_combine_empty_vector():
    x_part = PartitionedForwardVector([], [])
    x = x_part.combine()
    assert x.value == []