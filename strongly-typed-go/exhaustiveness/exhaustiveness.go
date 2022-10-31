package exhaustiveness
import "strongly-typed-go/exhaustiveness/status"

func DoWork(s status.AccountStatus) string {
	switch s.(type) {
	case status.Active: return "Perform API calls, ..."
	case status.Inactive: return "Skipping..."
	}
}
