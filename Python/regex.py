def is_match_rec(t, p, n, m):
  
    # If pattern is empty, then text must also be empty
    if m == 0:
        return n == 0

    # If text is empty, then pattern can have characters followed by *s
    if n == 0:
        return (m >= 2 and p[m - 1] == '*') and is_match_rec(t, p, n, m - 2)

    # If last characters of both string and pattern match, or pattern has '.'
    if t[n - 1] == p[m - 1] or p[m - 1] == '.':
        return is_match_rec(t, p, n - 1, m - 1)

    # Handle '*' in the pattern
    if p[m - 1] == '*' and m > 1:
        # Check if '*' can represent zero occurrences of the preceding character
        zero = is_match_rec(t, p, n, m - 2)

        # Check if '*' can represent one or more occurrences of the preceding character
        one_or_more = (p[m - 2] == t[n - 1] or p[m - 2] == '.') and is_match_rec(t, p, n - 1, m)

        return zero or one_or_more

    # If no match
    return False

# Wrapper function
def is_match(t, p):
    return is_match_rec(t, p, len(t), len(p))

# Example usage
print(is_match('aab', 'a.*'))
print(is_match('aa', 'a'))
print(is_match('aa', 'a*'))
print(is_match('ab', '.*'))
print(is_match('mississippi', 'mis*is*p*.'))
