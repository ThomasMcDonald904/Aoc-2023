import re
nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("input.txt", "r") as file:
    lines = [line for line in file.read().split("\n")][:-1]

bar = []
for line in lines:
    foo = [str(nums[value]) if not value.isnumeric() else value for value in re.findall(r"(?=(" + "|".join(list(nums.keys()) + list(map(lambda x: str(x), nums.values()))) + "))", line)]
    bar.append(foo)

cumul = 0
for line in lines:
    line = re.sub(r"\D*", "", line)
    cumul += int(line[0] + line[-1])
# Task 1
print(cumul)

cumul = 0
for line in bar:
    cumul += int(line[0] + line[-1])
# Task 2
print(cumul)
