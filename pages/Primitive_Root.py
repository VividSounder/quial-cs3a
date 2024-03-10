import streamlit as st

def primitive_roots_hunter(q, g):
    if q > 1:
        if (q % 2) == 0:
            st.write(f"{q} is not a prime number!!")
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
                            st.write(f"{p}^{h} mod {q} = {f}", end=", ")
                        if h == (q-1):
                            st.write(f"{p}^{h} mod {q} = {f} ==> {p} is primitive root of {q}", end=", ")
                            prim_or_not = True
                            primitive_roots.append(p)
                    elif f in placeholder:
                        placeholder.clear()
                        st.write("")
                        break
            if g in primitive_roots:
                st.write(f"{g} is primitive root: {prim_or_not} {primitive_roots}")
            else:
                st.write(f"{g} is NOT a primitive root of {q} - List of Primitive roots: {primitive_roots}")
    else:
        st.write(f"{q} is not a prime number!!")
        return

def main():
    st.title("Primitive Roots Hunter")
    q = st.number_input("Enter a prime number (q):", min_value=2, step=1)
    g = st.number_input("Enter a candidate primitive root (g):", min_value=2, step=1)

    if st.button("Find Primitive Roots"):
        st.write("Primitive Roots:")
        primitive_roots_hunter(int(q), int(g))

if __name__ == "__main__":
    main()
