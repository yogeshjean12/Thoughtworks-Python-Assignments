def function_outside():
    msg = "Hi"
    def function_inside():
        nonlocal msg
        msg = "Hello"
        print(msg)
    function_inside()
    print(msg)

function_outside()