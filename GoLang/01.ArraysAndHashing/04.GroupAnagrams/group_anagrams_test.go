package group_anagrams

import (
	"Leetcode/CommonPackage"
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		strs   []string
		output [][]string
	}{
		{
			strs:   []string{"eat", "tea", "tan", "ate", "nat", "bat"},
			output: [][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			strs:   []string{"a"},
			output: [][]string{{"a"}},
		},
	}

	for _, test := range tests {
		isTestSuccess := true

		got := GroupAnagrams(test.strs)
		for _, v := range test.output {

			isChecked := false
			for _, g := range got {
				if common_package.IsSameStringSlice(g, v) {
					isChecked = true
					break
				}
			}

			if !isChecked {
				isTestSuccess = false
				break
			}
		}

		if !isTestSuccess {
			t.Errorf(
				"Given Input=%v; Expected Output=%v; Got %v",
				test.strs, test.output, got,
			)
		}
	}
}
