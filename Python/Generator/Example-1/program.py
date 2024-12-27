def remote_control_next():
    yield "CN"
    yield "HBO"
    yield "Sports"

for ch in remote_control_next():
    print(ch)
