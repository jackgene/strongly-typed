from enum import Enum

class AccountStatus(Enum):
    Active = 1
    Inactive = 2

def update_user_statistics(status: AccountStatus) -> bool:
    match status:
        case AccountStatus.Active: return True
        case AccountStatus.Inactive: return False
