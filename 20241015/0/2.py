def count(s):
    gl = set("aeiou")
    sogl = set("bcdfghjklmnpqrstvwxyz")

    s = set(el for el in s if el.islower())

    our_gl = s & gl
    out_sogl = s & sogl

    print(f"гласных {len(our_gl)}")
    print(f"согласных {len(out_sogl)}")


count(input())

