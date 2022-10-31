enum AccountStatus {
  ACTIVE,
  INACTIVE,
}

function updateUserStatistics(status: AccountStatus): string {
  switch(status) {
    case AccountStatus.ACTIVE: return "Perform API calls, ...";
    case AccountStatus.INACTIVE: return "Skipping...";
  }
}
