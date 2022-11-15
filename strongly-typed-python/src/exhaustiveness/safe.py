from enum import Enum

class AccountStatus(Enum):
    Active = 1
    Inactive = 2

def update_user_statistics(status: AccountStatus):
    match status:
        case AccountStatus.Active: print("Perform API calls,...")
        case AccountStatus.Inactive: print("Skipping...")
