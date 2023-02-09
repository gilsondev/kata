package {{cookiecutter.project_slug}}

import "testing"

func Test{{cookiecutter.project_slug.capitalize()}}(t *testing.T) {
	result := {{cookiecutter.project_slug.capitalize()}}()

	if result == "" {
		t.Errorf("Error")
	}
}
