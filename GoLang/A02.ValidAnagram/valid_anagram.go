package valid_anagram

func ValidAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	mapS, mapT := make(map[uint8]int), make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		var ok bool

		_, ok = mapS[s[i]]
		if ok {
			mapS[s[i]] += 1
		} else {
			mapS[s[i]] = 1
		}

		_, ok = mapT[t[i]]
		if ok {
			mapT[t[i]] += 1
		} else {
			mapT[t[i]] = 1
		}

	}

	for key, value := range mapS {
		v := mapT[key]
		if v != value {
			return false
		}
	}

	return true
}
