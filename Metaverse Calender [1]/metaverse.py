import math  # to find lcm

def readFile(file):  # read the date from a file
  with open(file, "r") as f:
    content = f.read().splitlines()

  return content


def find_lcm(list):  # find the LCM of a list of any length
  lowest_common_multiple = 0

  for i in range(len(list)):
    list[i] = int(list[i])

  if len(list) > 1:
    lowest_common_multiple = math.lcm(list[0], list[1])

  for i in range(len(list)):
    lowest_common_multiple = math.lcm(lowest_common_multiple, list[i])

  return lowest_common_multiple

def main():
  content = readFile("input.txt")

  # Find the LCM for each day interval

  for i in range(int(
      content[0])):  # function to find number of simultaneous days
    M = (content[2 * (i + 1) - 1].split(' '))[1]
    frequency = list(content[2 * (i + 1)].split(' '))

    simultaneous_days = 0
    lcm = find_lcm(frequency)
    x = 0
    while x <= (int(M) - 1):
      x += lcm
      simultaneous_days += 1

    output = f"Case #{i+1}: {simultaneous_days}\n"

    with open("output.txt", "a") as f:
      f.write(output)

if __name__ == '__main__':
  main()