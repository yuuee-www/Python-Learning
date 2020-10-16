def test_is_in():
    assert is_in([1,2,3],1)
    assert is_in([1,2,3],3)
    assert not is_in([1,2,3],4)
    assert not is_in([],1)

def is_in(aList, target):
    for item in aList:
        if item == target:
            return True
    return False