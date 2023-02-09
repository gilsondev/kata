package two_sum

import "testing"

func TestTwo_sum(t *testing.T) {
	result := Two_sum()

	if result == "" {
		t.Errorf("Error")
	}
}
