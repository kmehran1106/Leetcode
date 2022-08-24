package group_anagrams

import (
	"strings"
)

func GroupAnagrams(strs []string) [][]string {
	output := [][]string{}
	hashMap := make(map[string][]string)
	runeA := []rune("a")[0]

	for _, word := range strs {
		baseString := strings.Repeat("0", 26)
		baseRuneArray := []rune(baseString)

		for _, c := range word {
			baseRuneArray[c-runeA]++
		}
		hashMap[string(baseRuneArray)] = append(hashMap[string(baseRuneArray)], word)
	}

	for _, v := range hashMap {
		output = append(output, v)
	}

	return output

}
