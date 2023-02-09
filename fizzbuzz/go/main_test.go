package fizzbuzz

import "testing"

func TestFizzbuzz(t *testing.T) {
	result := Fizzbuzz()

	if result == "" {
		t.Errorf("Error")
	}
}
