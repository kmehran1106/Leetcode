package two_sum

import (
	"reflect"
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		nums   []int
		target int
		output []int
	}{
		{
			nums:   []int{2, 7, 11, 15},
			target: 9,
			output: []int{0, 1},
		},
		{
			nums:   []int{3, 2, 4},
			target: 6,
			output: []int{1, 2},
		},
		{
			nums:   []int{3, 2, 4},
			target: 9,
			output: []int{},
		},
	}

	for _, test := range tests {
		if got := TwoSum(test.nums, test.target); !reflect.DeepEqual(got, test.output) {
			t.Errorf(
				"Input Array=%v with Target=%v; Output %v; Got %v",
				test.nums, test.target, test.output, got,
			)
		}
	}
}
