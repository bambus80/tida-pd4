#===========================================================================

# Zadanie 1.
# Dana jest lista liczb całkowitych dodatnich.
# Znajdź najdłuższy podciąg rosnący (czyli taką sekwencję liczb,
# w której każda kolejna liczba jest większa od poprzedniej)
# w tej liście.
#
# Na przykład dla listy [10, 22, 9, 33, 21, 50, 41, 60, 80],
# najdłuższy podciąg rosnący to 10, 22, 33, 50, 60, 80.

print("Zadanie 1")

input_arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

def zad1(arr: list[int]) -> list[int]:
    if not arr:
        return []
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    max_len_idx = dp.index(max_len)
    final = []
    while not max_len_idx == -1:
        final.append(arr[max_len_idx])
        max_len_idx = prev[max_len_idx]
    return final[::-1]


print(zad1(input_arr))

#===========================================================================

# Zadanie 2.
# Dana jest lista liczb całkowitych.
# Znajdź najdłuższy spójny podciąg o największej sumie w tej liście.
#
# Na przykład dla listy [2, -4, 6, 8, -10, 100, -6, 5],
# najdłuższy spójny podciąg o największej sumie to [6, 8, -10, 100].

print("\nZadanie 2")

input_arr = [2, -4, 6, 8, -10, 100, -6, 5]

def zad2(arr: list[int]) -> list[int]:
    if not arr:
        return []
    max_sum = sum = arr[0]
    start = end = start_t = 0
    for i in range(1, len(arr)):
        if sum + arr[i] < arr[i]:
            sum = arr[i]
            start_t = i
        else:
            sum += arr[i]
        if sum > max_sum or (sum == max_sum and (i - start_t) > (end - start)):
            max_sum = sum
            start = start_t
            end = i
    return arr[start:end+1]

print(zad2(input_arr))

#===========================================================================

# Zadanie 3.
# Napisz program wypisujący wszystkie możliwe niemalejące ciągi składników
# naturalnych (składniki mogą występować wielokrotnie), które w sumie dają
# zadaną liczbę n.

print("\nZadanie 3")

def zad3(n: int) -> list[int]:
    if not n:
        return [n]
    arr = []

    def backtrack(curr: list, rest: int, start: int) -> None:
        if rest == 0:
            arr.append(curr[:])
            return
        for i in range(start, rest + 1):
            curr.append(i)
            backtrack(curr, rest - i, i)
            curr.pop()

    backtrack([], n, 1)
    return arr

for i in zad3(5):
    print(i)

#===========================================================================

# Zadanie 4.
# Wygeneruj wszystkie permutacje n początkowych liter alfabetu
# i wypisz w porządku leksykograficznym.

print("\nZadanie 4")

def zad4(n: int) -> list[str]:
    if not n:
        return []
    letters = [chr(97 + i) for i in range(n)]
    final = []

    def permutate(arr):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1:] = reversed(arr[i + 1:])
        return True

    final.append("".join(letters))
    while permutate(letters):
        final.append("".join(letters))
    return final


for i in zad4(3):
    print(i)

#===========================================================================