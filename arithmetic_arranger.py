import math

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    r1, r2, r3, r4 = "", "", "", ""
    
    for query in problems:
        if '+' in query:
            plus = True
            num1, num2 = query.split(' + ')
        elif '-' in query:
            plus = False
            num1, num2 = query.split(' - ')
        else:
            return "Error: Operator must be '+' or '-'."
        try:
            num1, num2 = int(num1), int(num2)
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        width = int(math.log(max(num1, num2), 10)) + 3

        if width > 6:
            return 'Error: Numbers cannot be more than four digits.'
        r1 += f'{num1:>{width}}'
        r2 += ('+' if plus else '-') + f'{num2:>{width-1}}'
        r3 += '-'*width
        if show_answers:
            if plus:
                r4 += f'{num1+num2:>{width}}'
            else:
                r4 += f'{num1-num2:>{width}}'
        r1 += "    "
        r2 += "    "
        r3 += "    "
        r4 += "    "

    return r1[:-4] + '\n' + r2[:-4] + '\n' + r3[:-4] + '\n' + r4[:-4] if show_answers else r1[:-4] + '\n' + r2[:-4] + '\n' + r3[:-4]

if __name__ == "__main__":
  while True:
    try:
      num_problems = int(input("Enter the number of problems (max 5): "))
      if num_problems > 5:
        print("Error: Too many problems.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  problems = []
  for _ in range(num_problems):
    problem = input("Enter a problem (e.g., 32 + 698): ")
    problems.append(problem)

  print(arithmetic_arranger(problems, show_answers=True))
