n = int(input(""))
nums = [int(x) for x in input().split()]

''' mejorSuma = 0

for i in range(n):
    for j in range(i, n):
        mejorSuma = max(mejorSuma, sum(nums[i:j+1]))

print(mejorSuma) '''

mejorSumaLocal = 0
for i in range(n):
    mejorSumaLocal = max(nums[i] + mejorSumaLocal, nums[i])
    mejorSumaGlobal = max(mejorSumaLocal, mejorSumaGlobal)

print(mejorSumaGlobal)