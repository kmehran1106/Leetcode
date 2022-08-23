package contains_duplicate

func ContainsDuplicate(nums []int) bool {

	hashMap := make(map[int]bool)

	for _, value := range nums {
		_, ok := hashMap[value]
		if ok {
			return true
		} else {
			hashMap[value] = true
		}
	}

	return false

}
