package main

import (
	"errors"
	"fmt"
	"time"
)

func main() {
	//sudoku := [][]uint8{
	//	{5, 3, 0, 0, 7, 0, 0, 0, 0},
	//	{6, 0, 0, 1, 9, 5, 0, 0, 0},
	//	{0, 9, 8, 0, 0, 0, 0, 6, 0},
	//	{8, 0, 0, 0, 6, 0, 0, 0, 3},
	//	{4, 0, 0, 8, 0, 3, 0, 0, 1},
	//	{7, 0, 0, 0, 2, 0, 0, 0, 6},
	//	{0, 6, 0, 0, 0, 0, 2, 8, 0},
	//	{0, 0, 0, 4, 1, 9, 0, 0, 5},
	//	{0, 0, 0, 0, 8, 0, 0, 7, 9},
	//}

	sudoku := [][]uint8{
		{8, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 3, 6, 0, 0, 0, 0, 0},
		{0, 7, 0, 0, 9, 0, 2, 0, 0},
		{0, 5, 0, 0, 0, 7, 0, 0, 0},
		{0, 0, 0, 0, 4, 5, 7, 0, 0},
		{0, 0, 0, 1, 0, 0, 0, 3, 0},
		{0, 0, 1, 0, 0, 0, 0, 6, 8},
		{0, 0, 8, 5, 0, 0, 0, 1, 0},
		{0, 9, 0, 0, 0, 0, 4, 0, 0},
	}

	start := time.Now()
	solved, err := solve_sudoku(sudoku)
	if err == nil {
		for i := 0; i < len(solved); i++ {
			fmt.Println(solved[i])
		}
		t := time.Now()
		fmt.Println(t.Sub(start))
	} else {
		fmt.Println("The given sudoku does not have a solution.")
	}

}

func solve_sudoku(sudoku [][]uint8) ([][]uint8, error) {
	if is_solved(sudoku) {
		return sudoku, nil
	}
	x, y := find_zero(sudoku)

	var i uint8 = 0
	for true {
		i++
		if i == 10 {
			sudoku[y][x] = 0
			return sudoku, errors.New("No value that fits")
		} else if check_value(sudoku, int(i), x, y) {
			sudoku[y][x] = i

			solved, err := solve_sudoku(sudoku)
			if err != nil {
				sudoku[y][x] = 0
			} else {
				return solved, nil
			}
		}
	}
	return sudoku, nil
}

func check_value(sudoku [][]uint8, value int, x int, y int) bool {
	lstx := []uint8{}
	lsty := []uint8{}
	lstr := []uint8{}
	xLimU := -1
	xLimA := -1
	yLimU := -1
	yLimA := -1

	if x > 5 {
		xLimU = 5
		xLimA = 0
	} else if x > 2 {
		xLimU = 2
		xLimA = 6
	} else {
		xLimU = -1
		xLimA = 3
	}

	if y > 5 {
		yLimU = 5
		yLimA = 0
	} else if y > 2 {
		yLimU = 2
		yLimA = 6
	} else {
		yLimU = -1
		yLimA = 3
	}

	for y1 := 0; y1 < len(sudoku); y1++ {
		for x1 := 0; x1 < len(sudoku[y1]); x1++ {
			if x1 == x {
				lsty = append(lsty, sudoku[y1][x1])
			}
			if y1 == y {
				lstx = append(lstx, sudoku[y1][x1])
			}
			if (xLimU < x1) && (x1 < xLimA) && (yLimU < y1) && (y1 < yLimA) {
				lstr = append(lstr, sudoku[y1][x1])
			}
		}
	}
	present := true
	for i := 0; i < len(lstx); i++ {
		if int(lstx[i]) == value {
			present = false
		}
	}
	for i := 0; i < len(lsty); i++ {
		if int(lsty[i]) == value {
			present = false
		}
	}
	for i := 0; i < len(lstr); i++ {
		if int(lstr[i]) == value {
			present = false
		}
	}
	return present
}

func is_solved(sudoku [][]uint8) bool {
	for y := 0; y < len(sudoku); y++ {
		for x := 0; x < len(sudoku[y]); x++ {
			if sudoku[y][x] == 0 {
				return false
			}
		}
	}
	return true
}

func find_zero(sudoku [][]uint8) (int, int) {
	x := -1
	y := -1
	for y1 := 0; y1 < len(sudoku); y1++ {
		for x1 := 0; x1 < len(sudoku[y1]); x1++ {
			if sudoku[y1][x1] == 0 {
				return x1, y1
			}
		}
	}
	return x, y
}
