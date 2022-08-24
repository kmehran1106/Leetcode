package common_package

import (
	"testing"
)

func TestIsSameStringSlice(t *testing.T) {
	var tests = []struct {
		x      []string
		y      []string
		output bool
	}{
		{
			x:      []string{"a", "b", "c"},
			y:      []string{"a", "c", "b"},
			output: true,
		},
		{
			x:      []string{"a", "b", "c"},
			y:      []string{"d", "b", "c"},
			output: false,
		},
	}

	for _, test := range tests {
		if got := IsSameStringSlice(test.x, test.y); got != test.output {
			t.Errorf(
				"Given Input Arrays %v and %v; Expected Output=%v; Got %v",
				test.x, test.y, test.output, got,
			)
		}
	}
}
