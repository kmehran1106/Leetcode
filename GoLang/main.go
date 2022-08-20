package main

import (
	"Leetcode/01.BinarySearch"
	"Leetcode/02.MergeSort"
	"Leetcode/A01.ContainsDuplicate"
	"Leetcode/A02.ValidAnagram"
	"fmt"
)

func main() {
	binarySearchArray := []int{3, 4, 5, 6, 7, 8, 9}
	binarySearchValue := 4
	fmt.Println(binary_search.BinarySearch(binarySearchArray, binarySearchValue))

	mergeSortArray := []int{3, 4, 6, 5, 9, 8, 7}
	fmt.Println(merge_sort.MergeSort(mergeSortArray))

	containsDuplicateArray := []int{1, 2, 3, 2}
	fmt.Println(contains_duplicate.ContainsDuplicate(containsDuplicateArray))

	fmt.Println(valid_anagram.ValidAnagram("rat", "car"))
}
