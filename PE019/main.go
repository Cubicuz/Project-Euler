package main

import "fmt"

// how many sundays fell on the first of the month during twentieth century (1.1.1901 to 31.12.2000)

type dayOfWeek int

const (
	Monday dayOfWeek = iota
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

const (
	January int = iota
	February
	March
	April
	Mai
	June
	July
	August
	Sept
	Okt
	Nov
	Dec
)

var daysPerMonth = map[int]int{
	January:  31,
	February: 28,
	March:    31,
	April:    30,
	Mai:      31,
	June:     30,
	July:     31,
	August:   31,
	Sept:     30,
	Okt:      31,
	Nov:      30,
	Dec:      31,
}

type year struct {
	days     int
	startday dayOfWeek
}

func main() {
	const nYears = 100
	const nMonths = nYears * 12
	daysPassedSinceMonday := 0
	monthsStartingOnSunday := 0
	//years
	for j := 1900; j < 2001; j++ {

		//months
		isLeapYear := (j%4 == 0 && j%400 != 0)

		for m := 0; m < 12; m++ {
			if daysPassedSinceMonday%7 == 6 && j > 1900 {
				fmt.Printf("%v %v starts on Sunday \n", j, m)
				monthsStartingOnSunday++
			}
			daysPassedSinceMonday += daysPerMonth[m]
			//is start of month on sunday?
			if m == 2 && isLeapYear {
				daysPassedSinceMonday++
				fmt.Printf("%v is a leap year\n", j)
			}

		}
	}
	fmt.Printf("total monts started on sunday: %v", monthsStartingOnSunday)

}
