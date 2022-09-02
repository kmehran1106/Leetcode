package valid_anagram

import (
	"testing"
)

func TestCode(t *testing.T) {
	var tests = []struct {
		s      string
		t      string
		output bool
	}{
		{
			s:      "rat",
			t:      "car",
			output: false,
		},
		{
			s:      "anagram",
			t:      "nagaram",
			output: true,
		},
	}

	for _, test := range tests {
		if got := ValidAnagram(test.s, test.t); got != test.output {
			t.Errorf(
				"For Strings %v and %v; Expected %v; Got %v",
				test.s, test.t, test.output, got,
			)
		}
	}
}
