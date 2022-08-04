for i in range(1, 8):
    fname = f"{i}.csv"
    with open(fname) as f:
        lines = f.read().splitlines()

    x = []
    y = []
    z = []
    u = []
    for ln in lines:
        d = ln.split(',')
        x.append(float(d[1]))
        y.append(float(d[2]))
        z.append(float(d[3]))
        u.append(float(d[4]))

    print(fname)

    for arr in [x,y,z,u]:
        k = min(arr)
        p = max(arr) + -k
        for j in range(len(arr)):
            arr[j] += -k
            arr[j] *= 255/p

    print(min(x), max(x))
    print(min(y), max(y))
    print(min(z), max(z))
    print(min(u), max(u))

    with open(f"name_x_{i}.data", "wb") as f:
        f.write(bytes([int(q) for q in x]))

    with open(f"name_y_{i}.data", "wb") as f:
        f.write(bytes([int(q) for q in y]))

    with open(f"name_z_{i}.data", "wb") as f:
        f.write(bytes([int(q) for q in z]))

    with open(f"name_u_{i}.data", "wb") as f:
        f.write(bytes([int(q) for q in u]))

    # break

    # CTF{V1de0_Graphics_4rr4y}
