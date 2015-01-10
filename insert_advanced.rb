=begin
	
rescue Exception => e
	
end
Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of times Insertion Sort shifts each elements when sorting an array?

If ki is the number of elements over which ith element of the array has to shift then total number of shift will be k1 + k2 + + kN.

I/P:
2  
5  
1 1 1 2 2  
5  
2 1 3 1 2


O/P:
0  
4   
=end

def merge(left_arr, right_arr)
  merged_array = []
  i, j, inversions = 0, 0, 0
 
  for k in 0...(left_arr.size + right_arr.size) do
     if ((left_arr[i] != nil and right_arr[j] != nil and left_arr[i] <= right_arr[j]) or (left_arr[i] != nil and right_arr[j] == nil))
        merged_array << left_arr[i]
        i += 1
     else
        merged_array << right_arr[j]
        j += 1
        inversions += left_arr.size - i        
     end
  end
 
  return merged_array, inversions
end
 
def sort_and_count(arr)
  return arr, 0 if (arr.size == 1)
  
  mid = arr.size / 2;
   
  left_arr  = arr[0...mid]
  right_arr = arr[(mid)...arr.size]
 
  left_sorted_part, left_inversions    = sort_and_count(left_arr)
  right_sorted_part, right_inversions  = sort_and_count(right_arr)
  merged_array, merge_inversions       = merge(left_sorted_part, right_sorted_part)
 
  return merged_array, (left_inversions + right_inversions + merge_inversions)
end
 
NUMBER_OF_TEST_CASES = gets.to_i
 
NUMBER_OF_TEST_CASES.times do
  number_of_elements_to_be_sorted = gets.to_i
  array_of_elements_to_be_sorted = gets.strip.split.map {|i| i.to_i}
 
  puts sort_and_count(array_of_elements_to_be_sorted)[1]
end