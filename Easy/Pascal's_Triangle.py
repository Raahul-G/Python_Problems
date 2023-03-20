class Solution:
  def generate(self, numarrays: int) -> List[List[int]]:
    result = []
    for i in range(numarrays):
        array = [1] * (i + 1)  
        for j in range(1, i):
          array[j] = result[i-1][j-1] + result[i-1][j]            
        result.append(array)  
    return result
