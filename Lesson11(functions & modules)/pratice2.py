def reverse(s):
    if s == "":
        return ""

    result = reverse(s[1:]) + s[0]
    print(f"Returning: {result!r}")
    return result

final_result = reverse("hello")
print("\nFinal result:", final_result)

# hello
# s(ello) + s_prev[0](h) = elloh
# s(llo) + s_prev[0](e) lloe