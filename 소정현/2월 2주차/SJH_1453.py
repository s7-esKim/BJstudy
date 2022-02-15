number = int(input())

guest_want = list(map(int, input().split()))

guest = {}

return_person = 0
for i in guest_want:
    if i in guest.keys():
        return_person += 1
    else:
        guest[i] = 1

print(return_person)