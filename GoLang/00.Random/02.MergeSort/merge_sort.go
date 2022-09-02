package merge_sort

func MergeSort(arr []int) []int {
	result := []int{}

	if len(arr) > 1 {

		mid := len(arr) / 2
		leftArray, rightArray := arr[:mid], arr[mid:]

		leftArray = MergeSort(leftArray)
		rightArray = MergeSort(rightArray)

		i, j := 0, 0

		for i < len(leftArray) && j < len(rightArray) {
			if leftArray[i] <= rightArray[j] {
				result = append(result, leftArray[i])
				i += 1
			} else {
				result = append(result, rightArray[j])
				j += 1
			}
		}

		for i < len(leftArray) {
			result = append(result, leftArray[i])
			i += 1
		}

		for j < len(rightArray) {
			result = append(result, rightArray[j])
			j += 1
		}

		return result

	} else {

		return arr

	}
}
