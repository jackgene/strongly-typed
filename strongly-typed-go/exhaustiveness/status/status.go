package status

type AccountStatus interface { isStatus() }
type Active struct{}; func (Active) isStatus() {}
type Inactive struct{}; func (Inactive) isStatus() {}
