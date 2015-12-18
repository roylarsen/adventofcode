class Part1:
  def follow_instructions(self, instructions):
    floor = 0
    for instruction in instructions:
      if instruction = "(":
        floor += 1
      else:
        floor -= 1
  return floor
