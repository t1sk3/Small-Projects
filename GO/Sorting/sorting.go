package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	start := time.Now()
	l := []int{}
	const LIMIT = 15000
	for i := 0; i < LIMIT; i++ {
		l = append(l, rand.Intn(LIMIT))
	}
	fmt.Println(bubble_sort(l))
	t := time.Now()
	fmt.Println(t.Sub(start))
	start = time.Now()

	fmt.Println(quick_sort(l))
	t = time.Now()
	fmt.Println(t.Sub(start))
}

func bubble_sort(lst []int) []int {
	for e := 0; e < len(lst); e++ {
		for ee := 0; ee < len(lst)-1; ee++ {
			if lst[ee] > lst[ee+1] {
				lst[ee], lst[ee+1] = lst[ee+1], lst[ee]
			}
		}
	}
	return lst
}

func quick_sort(lst []int) []int {
	if len(lst) == 0 {
		return lst
	}
	spil := lst[int(len(lst)/2)]
	count := count_slice_occurence(lst, spil)
	s := []int{}
	for i := 0; i < count; i++ {
		s = append(s, spil)
	}
	l := []int{}
	r := []int{}
	for e := 0; e < len(lst); e++ {
		if lst[e] > spil {
			r = append(r, lst[e])
		} else if lst[e] < spil {
			l = append(l, lst[e])
		}
	}
	res := combine_slices(l, s)
	res = combine_slices(res, r)
	return res
}

func combine_slices(l []int, r []int) []int {
	for i := 0; i < len(r); i++ {
		l = append(l, r[i])
	}
	return l
}

func count_slice_occurence(lst []int, c int) int {
	count := 0
	for i := 0; i < len(lst); i++ {
		if lst[i] == c {
			count++
		}
	}
	return count
}
