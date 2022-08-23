package contains_duplicate

import (
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		nums   []int
		output bool
	}{
		{
			nums:   []int{1, 2, 3, 4, 5},
			output: false,
		},
		{
			nums:   []int{1, 1, 3, 4, 5},
			output: true,
		},
	}

	for _, test := range tests {
		if got := ContainsDuplicate(test.nums); got != test.output {
			t.Errorf(
				"For Nums=%v; Expected %v; Got %v",
				test.nums, test.output, got,
			)
		}
	}
}
