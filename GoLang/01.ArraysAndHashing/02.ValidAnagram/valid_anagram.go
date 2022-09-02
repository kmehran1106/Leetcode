package valid_anagram

func ValidAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	mapS, mapT := make(map[uint8]int), make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		mapS[s[i]]++
		mapT[t[i]]++
	}

	for key, value := range mapS {
		v := mapT[key]
		if v != value {
			return false
		}
	}

	return true
}
