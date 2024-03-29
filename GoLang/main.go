package main

import (
	"Leetcode/00.Random/01.BinarySearch"
	"Leetcode/00.Random/02.MergeSort"
	"Leetcode/01.ArraysAndHashing/01.ContainsDuplicate"
	"Leetcode/01.ArraysAndHashing/02.ValidAnagram"
	"Leetcode/01.ArraysAndHashing/03.TwoSum"
	"Leetcode/01.ArraysAndHashing/04.GroupAnagrams"
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

	s, t := "rat", "tar"
	fmt.Println(valid_anagram.ValidAnagram(s, t))

	twoSumArray := []int{2, 7, 11, 15}
	twoSumTarget := 9
	fmt.Println(two_sum.TwoSum(twoSumArray, twoSumTarget))

	groupAnagramsArray := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(group_anagrams.GroupAnagrams(groupAnagramsArray))
}
