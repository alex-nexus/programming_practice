# https://www.youtube.com/watch?v=VNbkzsnllsU


def largest_rec(bin_heights):
  largest = 0
  for index in range(len(bin_heights)):
    largest_rec_for = find_largest_rec_for(index, bin_heights)
    if largest_rec_for > largest:
      largest = largest_rec_for
  return largest


def find_largest_rec_for(index, bin_heights):
  index_height = bin_heights[index]
  left_max = index
  right_max = index

  for i in range(index - 1, -1, -1):
    if bin_heights[i] >= index_height:
      left_max = i
    else:
      break

  for i in range(index + 1, len(bin_heights)):
    if bin_heights[i] >= index_height:
      right_max = i
    else:
      break
  print((index, index_height, left_max, right_max, index_height * (right_max - left_max + 1)))
  return index_height * (right_max - left_max + 1)


bin_heights = [1, 3, 2, 1, 2]
print(bin_heights)
# print(find_largest_rec_for(0, bin_heights))
print(largest_rec(bin_heights))
#
# bin_heighs2 = [1, 3, 2, 1, 2]
# print(largest_rec(bin_heighs2))
