package binary_search

import (
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		arr    []int
		value  int
		output int
	}{
		{
			arr:    []int{3, 4, 5, 6, 7, 8, 9},
			value:  4,
			output: 1,
		},
	}

	for _, test := range tests {
		if got := BinarySearch(test.arr, test.value); got != test.output {
			t.Errorf(
				"For Array=%v and SearchValue=%v; Expected Index was %v; Got %v",
				test.arr, test.value, test.output, got,
			)
		}
	}
}
