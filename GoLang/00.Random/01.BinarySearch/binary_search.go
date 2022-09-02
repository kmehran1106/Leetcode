package binary_search

func BinarySearch(arr []int, value int) int {
	low := 0
	high := len(arr)

	for low <= high {
		midIndex := (high + low) / 2
		midValue := arr[midIndex]

		if midValue < value {
			low = midIndex + 1
		} else if midValue > value {
			high = midIndex - 1
		} else {
			return midIndex
		}
	}
	return -1
}
