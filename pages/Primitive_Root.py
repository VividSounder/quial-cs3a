q = int(input())
g = int(input())

def primitive_roots_hunter(q, g):
    if q > 1:
        if (q % 2) == 0:
            print(f"{q} is not a prime number!!")
            return
        else:
            prim_or_not = False
            placeholder = []
            primitive_roots = []
            for i in range(q-1):
                for j in range(q):
                    p = i + 1
                    h = j + 1 
                    f = (p ** h) % q
                    if f not in placeholder:
                        placeholder.append(f)
                        if h <= (q-2):
                            print(f"{p}^{h} mod {q} = {f}", end= ", ")
                        if h == (q-1):
                            print(f"{p}^{h} mod {q} = {f} ==> {p} is primitive root of {q}", end=",")
                            prim_or_not = True
                            primitive_roots.append(p)
                    elif f in placeholder:
                        placeholder.clear()
                        print("")
                        break
            if g in primitive_roots:
                print(f"{g} is primitive root: {prim_or_not} {primitive_roots}")
            else:
                print(f"{g} is NOT primitive root of {q} - List of Primitive roots: {primitive_roots}")
    else:
        print(f"{q} is not a prime number!!")
        return
        
primitive_roots_hunter(q, g)
