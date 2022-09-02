package merge_sort

import (
	"reflect"
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		arr    []int
		output []int
	}{
		{
			arr:    []int{1, 2, 3, 4, 5, 6},
			output: []int{1, 2, 3, 4, 5, 6},
		},
		{
			arr:    []int{2, 4, 3, 0, 1, 9},
			output: []int{0, 1, 2, 3, 4, 9},
		},
	}

	for _, test := range tests {
		if got := MergeSort(test.arr); !reflect.DeepEqual(got, test.output) {
			t.Errorf(
				"Input Array=%v; Sorted Should be %v; Got %v",
				test.arr, test.output, got,
			)
		}
	}
}
