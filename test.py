from testwith import describe, it

with describe("testing a test"):
    with it("should pass"):
        i = 1
        assert i == 1
    with it("should fail"):
        i = 1
        assert i == 2
    with it("should fail, too"):
        i = 1
        assert i == 1+3
    with it("will pass, nonetheless"):
        i = "abc"
        assert i[0] == "a"
    with it("should raise a different exception, yielding different result"):
        raise Exception("oh, man!")
    with it("should pass again"):
        i = 2+2
        assert i == 4
