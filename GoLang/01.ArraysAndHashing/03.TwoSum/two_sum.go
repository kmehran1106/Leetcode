package two_sum

func TwoSum(nums []int, target int) []int {
	hashMap := make(map[int]int)

	for index, value := range nums {
		a := target - value
		b, ok := hashMap[a]
		if !ok {
			hashMap[value] = index
		} else {
			return []int{b, index}
		}
	}
	return []int{}
}
